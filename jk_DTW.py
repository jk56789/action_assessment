from dtaidistance import dtw
import numpy as np

def extract_distance_dtw(teacher_df, student_df, column, step):
    distance = []

    trainer_arr = teacher_df[column][::step].reset_index(drop=True).to_numpy()
    student_arr = student_df[column][::step].reset_index(drop=True).to_numpy()

    distance = dtw.distance(trainer_arr, student_arr)
    normalized_distance = distance / len(student_arr)

    return distance, normalized_distance


def distances_append(distances_empty_list, user_empty_list, teacher_arr, new_user_json, new_key_column, 
                    row, step):

    if row % step == 0:
        data_num = int(row/step)
        user_empty_list[data_num] = new_user_json[new_key_column]
        student_arr = np.array(user_empty_list)

        if not (len(teacher_arr) == 0 or len(student_arr) == 0):
            distance = dtw.distance(teacher_arr, student_arr)
            distances_empty_list.append(distance)


    return distances_empty_list




def extract_distance_dtw2(teacher_df, student_df, columns):
    def extract_points(df, columns):
        points = []
        for i in range(len(df)):
            frame_points = []
            for col in columns:
                x = df.iloc[i, col]
                y = df.iloc[i, col + 1]
                z = df.iloc[i, col + 2]
                frame_points.extend([x, y, z])
            points.append(frame_points)
        return np.array(points)

    teacher_points = extract_points(teacher_df, columns)
    student_points = extract_points(student_df, columns)

    # Calculate DTW distance

    distance = dtw.distance(teacher_points, student_points)
    normalized_distance = distance / len(student_points)

    return distance, normalized_distance


def extract_distance_dtw3(teacher_df, student_df, columns):
    # Extract 3D points for each frame based on specified columns
    def extract_points(df, columns):
        points = []
        for i in range(len(df)):
            frame_points = []
            for col in columns:
                x = df.iloc[i, col]
                y = df.iloc[i, col + 1]
                z = df.iloc[i, col + 2]
                frame_points.extend([x, y, z])
            points.append(frame_points)
        return np.array(points)

    teacher_points = extract_points(teacher_df, columns)
    student_points = extract_points(student_df, columns)

    # Calculate DTW distance for each dimension separately
    distances = []
    for dim in range(teacher_points.shape[1]):
        distance = dtw.distance(teacher_points[:, dim], student_points[:, dim])
        distances.append(distance)
    
    # Combine distances (e.g., sum or average)
    total_distance = sum(distances)
    normalized_distance = total_distance / len(student_points)

    return total_distance, normalized_distance

# Example usage:
# columns = [0, 3]
# distance, normalized_distance = extract_distance_dtw2(trainer_world_results_df, user_world_results_df, columns)



def extract_distance_dtw4(teacher_df, student_df, columns):
    # Extract 3D points for each frame based on specified columns
    def extract_points(df, columns):
        points = []
        for i in range(len(df)):
            frame_points = []
            for col in columns:
                x = df.iloc[i, col * 4]     # x coordinate
                y = df.iloc[i, col * 4 + 1] # y coordinate
                z = df.iloc[i, col * 4 + 2] # z coordinate
                frame_points.extend([x, y, z])
                #frame_points.extend([x, y])
            points.append(frame_points)
        return np.array(points)

    teacher_points = extract_points(teacher_df, columns)
    student_points = extract_points(student_df, columns)

    # Calculate DTW distance for each dimension separately
    distances = {}
    for i, col in enumerate(columns):
        #distance = dtw.distance(teacher_points[:, i * 3], student_points[:, i * 3])
        '''distance_x = dtw.distance(teacher_points[:, i * 2], student_points[:, i * 2])
        distance_y = dtw.distance(teacher_points[:, i * 2 + 1], student_points[:, i * 2 + 1])
        '''
        distance_x = dtw.distance(teacher_points[:, i * 3 + 0], student_points[:, i * 3 + 0])
        distance_y = dtw.distance(teacher_points[:, i * 3 + 1], student_points[:, i * 3 + 1])
        distance_z = dtw.distance(teacher_points[:, i * 3 + 2], student_points[:, i * 3 + 2])
        
        #distances[col] = (distance_x + distance_y ) / 2
        distances[col] = (distance_x + distance_y + distance_z) / 3
        
    
    return distances


# Example usage:
# columns = [0, 3]
# distances = extract_distance_dtw3(trainer_world_results_df, user_world_results_df, columns)
# print(distances)