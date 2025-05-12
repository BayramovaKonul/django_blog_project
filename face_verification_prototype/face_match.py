# import face_recognition

# # Load known image (ID photo)
# known_image = face_recognition.load_image_file("id_photo.jpeg")
# known_encoding = face_recognition.face_encodings(known_image)[0]

# # Load unknown image (selfie or from video)
# unknown_image = face_recognition.load_image_file("user_photo.jpeg")
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# # Compare
# results = face_recognition.compare_faces([known_encoding], unknown_encoding)
# print("Match found:" if results[0] else "No match.")
