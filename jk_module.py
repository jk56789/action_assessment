import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils 
mp_pose = mp.solutions.pose

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results



def extract_main_landmark(landmarks, frame_time):
    # Get coordinate
    # ex) mp_pose.PoseLandmark.LEFT_HIP.value == 23
    left_hip = [
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].visibility,
    ]
    left_knee = [
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].visibility,
    ]
    left_ankle = [
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].visibility,
    ]
    right_hip = [
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].visibility,
    ]
    right_knee = [
        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].visibility,
    ]
    right_ankle = [
        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].visibility,
    ]
    left_shoulder = [
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].visibility,
    ]
    left_elbow = [
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].visibility,
    ]
    left_wrist = [
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].visibility,
    ]
    right_shoulder = [
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].visibility,
    ]
    right_elbow = [
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].visibility,
    ]
    right_wrist = [
        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].visibility,
    ]
    nose = [
        landmarks[mp_pose.PoseLandmark.NOSE.value].x,
        landmarks[mp_pose.PoseLandmark.NOSE.value].y,
        landmarks[mp_pose.PoseLandmark.NOSE.value].z,
        landmarks[mp_pose.PoseLandmark.NOSE.value].visibility,
    ]
    left_eye = [
        landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].visibility,
    ]
    right_eye = [
        landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].visibility,
    ]
    left_ear = [
        landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].z,
        landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].visibility,
    ]
    right_ear = [
        landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x,
        landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y,
        landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].z,
        landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].visibility,
    ]
    
    # save keypoints
    keypoints = {
        "23. left_hip": left_hip,
        "25. left_knee": left_knee,
        "27. left_ankle": left_ankle,
        
        "24. right_hip": right_hip,
        "26. right_knee": right_knee,
        "28. right_ankle": right_ankle,
        
        "11. left_shoulder": left_shoulder,
        "13. left_elbow": left_elbow,
        "15. left_wrist": left_wrist,
        
        "12. right_shoulder": right_shoulder,
        "14. right_elbow": right_elbow,
        "16. right_wrist": right_wrist,
        
        "0. nose": nose,
        "2. left_eye": left_eye,
        "5. right_eye": right_eye,
        "7. left_ear": left_ear,
        "8. right_ear": right_ear,
        
        "time stamp": frame_time,
    }

    return keypoints 

import csv
def landmarks_save(root, results, row):
    with open(root, 'a', newline='') as file:
            writer = csv.writer(file)
            if row == 0:  # Write header only for the first frame
                headers = []
                for i in range(len(results.pose_landmarks.landmark)):
                    headers.extend([f'landmark_{i}_x', f'landmark_{i}_y', f'landmark_{i}_z', f'landmark_{i}_visibility'])
                writer.writerow(headers)
            landmarks_data = []
            for landmark in results.pose_landmarks.landmark:
                landmarks_data.extend([landmark.x, landmark.y, landmark.z, landmark.visibility])
            writer.writerow(landmarks_data)

def world_landmarks_save(root, results, row):
    with open(root, 'a', newline='') as file:
            writer = csv.writer(file)
            if row == 0:  # Write header only for the first frame
                headers = []
                for i in range(len(results.pose_world_landmarks.landmark)):
                    headers.extend([f'world_landmark_{i}_x', f'world_landmark_{i}_y', f'world_landmark_{i}_z', f'world_andmark_{i}_visibility'])
                writer.writerow(headers)
            landmarks_data = []
            for landmark in results.pose_world_landmarks.landmark:
                landmarks_data.extend([landmark.x, landmark.y, landmark.z, landmark.visibility])
            writer.writerow(landmarks_data)

