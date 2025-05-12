from flask import Flask, request, jsonify, render_template
import cv2
import os
import face_recognition
import pytesseract
import numpy as np
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def serve_index():
    return render_template('index.html')

def extract_frame(video_path, frame_time=2):
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        return None

    video_capture.set(cv2.CAP_PROP_POS_MSEC, frame_time * 1000)
    success, frame = video_capture.read()
    video_capture.release()
    
    if not success:
        return None

    unique_filename = f"frame_{uuid.uuid4().hex}.jpg"
    frame_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    cv2.imwrite(frame_path, frame)
    return frame_path

def check_face_match(user_image_path, id_image_path, tolerance=0.5):  # Lower tolerance for stricter matching
    try:
        # Load images
        user_image = face_recognition.load_image_file(user_image_path)
        id_image = face_recognition.load_image_file(id_image_path)

        # Detect face locations first
        user_faces = face_recognition.face_locations(user_image)
        id_faces = face_recognition.face_locations(id_image)

        # Validate exactly one face in both images
        if len(user_faces) != 1 or len(id_faces) != 1:
            app.logger.warning(f"Invalid face count - User: {len(user_faces)}, ID: {len(id_faces)}")
            return False

        # Get encodings using detected face locations
        user_encoding = face_recognition.face_encodings(user_image, known_face_locations=user_faces)[0]
        id_encoding = face_recognition.face_encodings(id_image, known_face_locations=id_faces)[0]

        # Calculate face distance and compare with threshold
        face_distance = face_recognition.face_distance([id_encoding], user_encoding)[0]
        app.logger.info(f"Face distance: {face_distance}, Tolerance: {tolerance}")

        return face_distance <= tolerance

    except Exception as e:
        app.logger.error(f"Face match error: {str(e)}")
        return False

def preprocess_image(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            return None

        # Scale while maintaining aspect ratio
        h, w = image.shape[:2]
        if w < 1000:
            new_w = 1000
            new_h = int((new_w / w) * h)
            image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_CUBIC)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        processed = cv2.adaptiveThreshold(
            blurred, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )
        return processed
    except Exception as e:
        app.logger.error(f"Image processing error: {str(e)}")
        return None

def extract_text(image_path):
    try:
        processed = preprocess_image(image_path)
        if processed is None:
            return ""

        custom_config = r'--oem 3 --psm 6 -l eng'
        text = pytesseract.image_to_string(processed, config=custom_config)
        return text.strip()
    except Exception as e:
        app.logger.error(f"OCR error: {str(e)}")
        return ""

def validate_frame(image_path):
    try:
        image = face_recognition.load_image_file(image_path)
        faces = face_recognition.face_locations(image)  # More accurate detection
        
        if len(faces) != 1:
            app.logger.warning(f"Faces detected: {len(faces)}")
            return False
            
        # Get face dimensions
        top, right, bottom, left = faces[0]
        face_height = bottom - top
        face_width = right - left
        img_height, img_width = image.shape[:2]
        
        # Adjustable thresholds (modify these as needed)
        MIN_FACE_HEIGHT_RATIO = 0.15  # 15% of image height
        MIN_FACE_WIDTH_RATIO = 0.12   # 12% of image width
        MAX_TILT = 0.3  # 30% offset from center
        
        # Calculate ratios
        height_ratio = face_height / img_height
        width_ratio = face_width / img_width
        
        # Check face size
        if height_ratio < MIN_FACE_HEIGHT_RATIO or width_ratio < MIN_FACE_WIDTH_RATIO:
            app.logger.warning(f"Face too small. H: {height_ratio:.2f}, W: {width_ratio:.2f}")
            return False
            
        # Check face position
        vertical_center = (top + bottom) / 2
        horizontal_center = (left + right) / 2
        vertical_offset = abs(0.5 - (vertical_center / img_height))
        horizontal_offset = abs(0.5 - (horizontal_center / img_width))
        
        if vertical_offset > MAX_TILT or horizontal_offset > MAX_TILT:
            app.logger.warning(f"Face off-center. V: {vertical_offset:.2f}, H: {horizontal_offset:.2f}")
            return False
            
        return True

    except Exception as e:
        app.logger.error(f"Validation error: {str(e)}")
        return False

@app.route('/upload_video', methods=['POST'])
def upload_video():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video part'}), 400

        video_file = request.files['video']
        if video_file.filename == '':
            return jsonify({'error': 'No selected video'}), 400

        # Save video with unique filename
        video_path = os.path.join(UPLOAD_FOLDER, f"vid_{uuid.uuid4().hex}{os.path.splitext(video_file.filename)[1]}")
        video_file.save(video_path)

        # Frame extraction with validation
        user_frame = extract_frame(video_path, frame_time=1)
        id_frame = extract_frame(video_path, frame_time=3)

        if not user_frame or not id_frame:
            return jsonify({'error': 'Failed to extract required frames'}), 400

        # Validate frame quality
        if not validate_frame(user_frame):
            return jsonify({'error': 'Poor frame quality - ensure clear face visibility'}), 400
        
        # Validate frame quality
        if not validate_frame(id_frame):
            return jsonify({'error': 'Poor frame quality 2 - ensure clear face visibility'}), 400

        # Face matching
        face_match = check_face_match(user_frame, id_frame)
        
        # OCR processing
        id_text = extract_text(id_frame)

        return jsonify({
            'face_match': face_match,
            'id_text': id_text if id_text else "No text detected"
        })

    except Exception as e:
        app.logger.error(f"Critical error: {str(e)}")
        return jsonify({'error': 'Internal processing error'}), 500

    finally:
        # Cleanup resources
        for path in [user_frame, id_frame, video_path]:
            try:
                if path and os.path.exists(path):
                    os.remove(path)
            except Exception as e:
                app.logger.error(f"Cleanup error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)