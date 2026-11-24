import numpy as np
import face_recognition_models
from sklearn.svm import SVC
from src.database.db import get_all_students
import dlib
import streamlit as st


@st.cache_resource
def load_dlib_model():
    detector=dlib.get_frontal_face_detector() #it shows how much faces in the image

    sp=dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
        )#it gives landmarks of the face(location of eyes, nose, mouth etc)

    facerec=dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
        )#it gives 128D vector for each face which is unique for each face

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_model()#loading all models
    faces=detector(image_np, 1) #detecting faces in the image

    encoding=[]

    for face in faces:
        shape=sp(image_np, face) #getting landmarks of the face
        face_descriptor=facerec.compute_face_descriptor(image_np, shape,1) #getting 128D vector for the face
        encoding.append(np.array(face_descriptor)) #appending the vector to the list
    return encoding

def get_trained_model():
    X=[]
    y=[]

    student_db=get_all_students() #getting all students from the database
    if not student_db:
        return None

    for student in student_db:
        embedding=student.get("face_embedding")
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get("student_id"))

    if len(X) == 0:
        return 0

    
    clf = SVC(kernel='linear', probability=True,class_weight='balanced') #using SVM classifier with linear kernel
    
    try:
        clf.fit(X, y)
    except ValueError:
        pass

    return {"clf": clf, "X": X, "y": y} #returning the trained model and the data used for training

def train_classifier():
    st.cache_resource.clear()
    model_data=get_trained_model()# getting the trained model
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings=get_face_embeddings(class_image_np) #getting the embeddings of the faces in the image
    detected_student={}
    model_data=get_trained_model()# getting the trained model

    if not model_data:
        return detected_student,[],len(encodings) # returning empty dictionary and list if no model is found

    clf=model_data['clf']
    X_train=model_data['X']
    y_train=model_data['y']

    all_students = sorted(list(set(y_train))) #getting all unique student ids

    for encoding in encodings:
        if len(all_students)>=2:
            predicted_id=int(clf.predict([encoding][0]))
        else:
            predicted_id=int(all_students[0])

        student_embedding=X_train[y_train.index(predicted_id)]

        best_match_score=np.linalg.norm(student_embedding-encoding)

        resemblance_threshold=0.6

        if best_match_score <=resemblance_threshold:
            detected_student[predicted_id] =True
    return detected_student,all_students,len(encodings)

    