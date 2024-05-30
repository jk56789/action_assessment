import numpy as np
import ast
import cv2

def OKS(row, columns, teacher_points_df, now_stu_results):
    columns_OKS = [col+"_OKS" for col in columns]
    
    OKS_list = []
    num_columns = len(columns)
    now_teacher_list = teacher_points_df.iloc[row]

    OKS = {"hip": 0.107,
        "ankle": 0.089,
        "knee": 0.087,
        "shoulder": 0.079,
        "elbow": 0.072,
        "wrist": 0.062,
        "ear": 0.035,
        "nose": 0.026,
        "eye": 0.025
        }
    
    for _, column in enumerate(columns):
        
        col = int(column.split('.')[0])
        stu_x, stu_y, stu_z = now_stu_results.pose_world_landmarks.landmark[col].x, now_stu_results.pose_world_landmarks.landmark[col].y, now_stu_results.pose_world_landmarks.landmark[col].z
        teacher_x, teacher_y, teacher_z = ast.literal_eval(now_teacher_list[column])[0], ast.literal_eval(now_teacher_list[column])[1], ast.literal_eval(now_teacher_list[column])[2]

        col_dist = (teacher_x-stu_x)**2 + (teacher_y-stu_y)**2 + (teacher_z-stu_z)**2

        k = OKS[column.split('_')[1]]

        col_score = np.exp(-col_dist/k)
        OKS_list.append(col_score)

    keypoints_OKS = {columns_OKS[i]: OKS_list[i] for i in range(num_columns)}

    return keypoints_OKS


keypoints_labels = {
            "15. left_wrist_OKS": ("(L)wr", (840, 700)),
            "13. left_elbow_OKS": ("(L)elb", (660, 750)),
            "11. left_shoulder_OKS": ("(L)sh", (620, 430)),
            "23. left_hip_OKS": ("(L)hip", (700, 1000)),
            "25. left_knee_OKS": ("(L)knee", (700, 1400)),
            "27. left_ankle_OKS": ("(L)ankle", (700, 1750))
        }

def text_OKS(image, keypoints_labels, keypoints_OKS):
    for key, (label, position) in keypoints_labels.items():
        score = keypoints_OKS[key]
        if 0 <= score <= 0.25:
            color = (0, 0, 255)  # Red
        elif 0.26 <= score <= 0.50:
            color = (0, 165, 255)  # Orange
        elif 0.51 <= score <= 0.75:
            color = (0, 255, 255)  # Yellow
        elif 0.76 <= score <= 1.00:
            color = (0, 0, 0)  # Black
        cv2.putText(image, f'{label}: {score:.2f}', position, cv2.FONT_ITALIC, 1.3, color, 3)






def OKS_score(list1, list2, columns):
    OKS_list = [0] * 32  # Initialize OKS_list with 32 zeros

    score_constant = {
            #"23": 0.107,
            #"24": 0.107,
            "23": 2.707,
            "24": 2.707,
            "27": 0.089,
            #"27": 0.150,
            "28": 0.089,
            "25": 0.087,
            "26": 0.087,
            "11": 0.079,
            "12": 0.079,
            "13": 0.072,
            "14": 0.072,
            "15": 0.062,
            "16": 0.062,
            "7": 0.035,
            "8": 0.035,
            "0": 0.026,
            "2": 0.025,
            "5": 0.025,
        }
    
    for col in columns:
        if col == 23 :
            '''x1, y1, z1 = list1[col*4], list1[col*4+1], list1[col*4+2]
            x2, y2, z2 = list2[col+3*4], list2[col+3*4+1], list2[col+3*4+2]
            distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            k = score_constant[str(col)]
            col_score = np.exp(-distance/k)
            OKS_list[col] = col_score '''

            x1, y1, z1 = list1[col*4], list1[col*4+1], list1[col*4+2]
            x2, y2, z2 = list2[col*4], list2[col*4+1], list2[col*4+2]
            
            distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            k = score_constant[str(col)]
            col_score = np.exp(-distance/k)

            OKS_list[col] = col_score 

        elif col == 24 :

            x1, y1, z1 = list1[col*4], list1[col*4+1], list1[col*4+2]
            x2, y2, z2 = list2[col+3*4], list2[col+3*4+1], list2[col+3*4+2]
            distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            k = score_constant[str(col)]
            col_score = np.exp(-distance/k)
            OKS_list[col] = col_score 

        else:    
            x1, y1, z1 = list1[col*4], list1[col*4+1], list1[col*4+2]
            x2, y2, z2 = list2[col*4], list2[col*4+1], list2[col*4+2]
            
            distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            k = score_constant[str(col)]
            col_score = np.exp(-distance/k)

            OKS_list[col] = col_score 
    return OKS_list



def OKS_2d_score(list1, list2, columns):
    OKS_list = [0] * 32  # Initialize OKS_list with 32 zeros

    score_constant = {
            "23": 0.107,
            "24": 0.107,

            "27": 0.150,
            "28": 0.089,
            "25": 0.087,
            "26": 0.087,
            "11": 0.079,
            "12": 0.079,
            "13": 0.072,
            "14": 0.072,
            "15": 0.062,
            "16": 0.062,
            "7": 0.035,
            "8": 0.035,
            "0": 0.026,
            "2": 0.025,
            "5": 0.025,
        }
    
    for col in columns:

            x1, y1, _ = list1[col*4], list1[col*4+1], list1[col*4+2]
            x2, y2, _ = list2[col*4], list2[col*4+1], list2[col*4+2]
            
            distance = (x1 - x2)**2 + (y1 - y2)**2
            k = score_constant[str(col)]
            col_score = np.exp(-distance/((k**2)))

            OKS_list[col] = col_score 
            #OKS_list[col] = distance * 10000
    return OKS_list





def OkS_text(image, score_list):

    text_position = {
            "23": (1200, 600), #
            "24": (20,10),
            "27": (1300, 950), #
            "28": (40,10),
            "25": (1400, 800), #
            "26": (60,10),
            "11": (1200, 230), #
            "12": (80,10),
            "13": (1400, 450), #
            "14": (10,10),
            "15": (1600, 400), #
            "16": (10,30),
            "7": (10,40),
            "8": (10,50),
            "0": (10,60),
            "2": (10,70),
            "5": (10,80),
    }   



    for key, position in text_position.items():
        score = score_list[int(key)]
        color = (255, 255, 255)  

        if 0 <= score <= 0.01:
            color =(0, 0, 255)  
        elif 0.02 <= score <= 0.25:
            color = (0, 0, 255) # Red
        elif 0.26 <= score <= 0.50:
            color = (0, 165, 255)  # Orange
        elif 0.51 <= score <= 0.75:
            color = (128, 128, 128)   # Yellow
        elif 0.76 <= score <= 1.00:
            color = (0, 0, 0)    # Black
        cv2.putText(image, f' {score:.4f}', position, cv2.FONT_ITALIC, 2, color, 4)




    
def OkS_text_base(image, score_list):

    text_position = {
            "23": (1200, 600), #
            "24": (20,10),
            "27": (1300, 950), #
            "28": (40,10),
            "25": (1400, 800), #
            "26": (60,10),
            "11": (1200, 230), #
            "12": (80,10),
            "13": (1400, 450), #
            "14": (10,10),
            "15": (1600, 430), #
            "16": (10,30),
            "7": (10,40),
            "8": (10,50),
            "0": (10,60),
            "2": (10,70),
            "5": (10,80),
    }   




    for key, position in text_position.items():
        score = score_list[int(key)]
        color = (0, 0, 0) 

        if 0 <= score <= 0.01:
            color =(0, 0, 255)  
        elif 0.02 <= score <= 0.25:
            color = (0, 0, 255) # Red
        elif 0.26 <= score <= 0.50:
            color = (0, 165, 255)  # Orange
        elif 0.51 <= score <= 0.75:
            color = (128, 128, 128)   # Yellow
        elif 0.76 <= score <= 1.00:
            color = (0, 0, 0)    # Black
        cv2.putText(image, f' {score:.4f}', position, cv2.FONT_ITALIC, 1.3, color, 3)