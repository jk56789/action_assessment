import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils 
mp_pose = mp.solutions.pose


def draw_person(image, person_df, row, frame_width, frame_height, color_keypoint=(245, 117, 66), color_connection=(245, 66, 230)):
    """
    Draws keypoints and connections on the given image based on the person_df data.

    Parameters:
    - image: The image on which to draw.
    - person_df: DataFrame containing the keypoints and visibility data.
    - row: The row index in the DataFrame to use for drawing.
    - frame_width: The width of the frame.
    - frame_height: The height of the frame.
    - color_keypoint: Color for the keypoints (default is (245, 117, 66)).
    - color_connection: Color for the connections (default is (245, 66, 230)).
    """
    person_list = person_df.iloc[row]
    keypoints = {}
    

    for idx in range(0, len(person_df.columns), 4):
        visibility_idx = idx + 3
        if person_list.iloc[visibility_idx] > 0.5:
            x = int(person_list.iloc[idx] * frame_width)
            y = int(person_list.iloc[idx + 1] * frame_height)
            keypoints[person_df.columns[idx].split('_')[1]] = (x, y)
            image = cv2.circle(image, (x, y), 5, color_keypoint, -1)

    for connection in mp_pose.POSE_CONNECTIONS:
        start_idx, end_idx = connection
        start_key = f"{start_idx}"
        end_key = f"{end_idx}"
        if start_key in keypoints and end_key in keypoints:
            start_point = keypoints[start_key]
            end_point = keypoints[end_key]
            image = cv2.line(image, start_point, end_point, color_connection, 2)

    return image

# Example usage:
# image3 = draw_person(image3, trainer_results_df, row, frame_width, frame_height)




mp_drawing = mp.solutions.drawing_utils 
mp_pose = mp.solutions.pose

def draw_person2(image, keypoints_list, frame_width, frame_height, color_keypoint=(245, 117, 66), color_connection=(245, 66, 230)):
    """
    Draws keypoints and connections on the given image based on the keypoints_list data.

    Parameters:
    - image: The image on which to draw.
    - keypoints_list: List containing the keypoints and visibility data.
    - frame_width: The width of the frame.
    - frame_height: The height of the frame.
    - color_keypoint: Color for the keypoints (default is (245, 117, 66)).
    - color_connection: Color for the connections (default is (245, 66, 230)).
    """
    keypoints = {}

    for idx in range(0, len(keypoints_list), 4):
        visibility = keypoints_list[idx + 3]
        if visibility > 0.5:
            x = int(keypoints_list[idx] * frame_width)
            y = int(keypoints_list[idx + 1] * frame_height)
            keypoints[idx // 4] = (x, y)
            image = cv2.circle(image, (x, y), 10, color_keypoint, -1)

    for connection in mp_pose.POSE_CONNECTIONS:
        start_idx, end_idx = connection
        if start_idx in keypoints and end_idx in keypoints:
            start_point = keypoints[start_idx]
            end_point = keypoints[end_idx]
            image = cv2.line(image, start_point, end_point, color_connection, 8)

    return image

def draw_person2_world(image, keypoints_list, frame_width, frame_height, color_keypoint=(245, 117, 66), color_connection=(245, 66, 230)):
    """
    Draws keypoints and connections on the given image based on the keypoints_list data.

    Parameters:
    - image: The image on which to draw.
    - keypoints_list: List containing the keypoints and visibility data.
    - frame_width: The width of the frame.
    - frame_height: The height of the frame.
    - color_keypoint: Color for the keypoints (default is (245, 117, 66)).
    - color_connection: Color for the connections (default is (245, 66, 230)).
    """
    keypoints = {}

    for idx in range(0, len(keypoints_list), 4):
        visibility = keypoints_list[idx + 3]
        if visibility > 0.5:
            x = int(keypoints_list[idx]* frame_width) + int(frame_width/2)
            y = int(keypoints_list[idx + 1] * frame_height)+ int(frame_height/2)
            keypoints[idx // 4] = (x, y)
            image = cv2.circle(image, (x, y), 5, color_keypoint, -1)

    for connection in mp_pose.POSE_CONNECTIONS:
        start_idx, end_idx = connection
        if start_idx in keypoints and end_idx in keypoints:
            start_point = keypoints[start_idx]
            end_point = keypoints[end_idx]
            image = cv2.line(image, start_point, end_point, color_connection, 2)

    return image

'''def move_points(list,frame_width,frame_height):
    # Calculate the center of the ankles
    left_ankle_x = list[27*4+0]
    left_ankle_y = list[27*4+1]

    right_ankle_x = list[28*4+0]
    right_ankle_y = list[28*4+1]

    center_x = (left_ankle_x + right_ankle_x) / 2
    center_y = (left_ankle_y + right_ankle_y) / 2

    # Convert normalized coordinates to pixel coordinates
    center_x_pixel = int(center_x * frame_width)
    center_y_pixel = int(center_y * frame_height)

    # Calculate the offset to move the center to (600, 1700)
    offset_x = 600 - center_x_pixel
    offset_y = 1700 - center_y_pixel

    # Move all landmarks by the calculated offset
    for landmark in list:
        landmark.x = (landmark.x * frame_width + offset_x) / frame_width
        landmark.y = (landmark.y * frame_height + offset_y) / frame_height'''