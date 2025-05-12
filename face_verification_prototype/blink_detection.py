# import cv2
# import mediapipe as mp

# mp_face_mesh = mp.solutions.face_mesh
# LEFT_EYE = [362, 385, 387, 263, 373, 380]
# RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# def get_blink_ratio(eye_landmarks, landmarks, frame_width, frame_height):
#     points = [(int(landmarks.landmark[p].x * frame_width), int(landmarks.landmark[p].y * frame_height)) for p in eye_landmarks]
#     hor_line = cv2.norm((points[0][0] - points[3][0], points[0][1] - points[3][1]))
#     ver_line = cv2.norm((points[1][0] - points[5][0], points[1][1] - points[5][1]))
#     return ver_line / hor_line

# cap = cv2.VideoCapture("test_video.mp4")

# with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1) as face_mesh:
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = face_mesh.process(frame_rgb)

#         if results.multi_face_landmarks:
#             for landmarks in results.multi_face_landmarks:
#                 h, w, _ = frame.shape
#                 left_ratio = get_blink_ratio(LEFT_EYE, landmarks, w, h)
#                 right_ratio = get_blink_ratio(RIGHT_EYE, landmarks, w, h)
#                 blink_ratio = (left_ratio + right_ratio) / 2

#                 if blink_ratio < 0.25:
#                     cv2.putText(frame, "Blink Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

#         cv2.imshow("Blink Detection", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()
