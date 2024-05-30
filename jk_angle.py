import math
import csv
import os

def angle_between_vectors(vector1, vector2):
    dot_product_val = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    magnitude_product = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2 + vector1[2] ** 2) * math.sqrt(vector2[0] ** 2 + vector2[1] ** 2 + vector2[2] ** 2)
    if magnitude_product == 0:
        return 0
    angle_radians = math.acos(dot_product_val / magnitude_product)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees


def extract_angle(vectors):
    lhip_angle = angle_between_vectors(vectors["lhip_vec1(23_1)"], vectors["lhip_vec2(23_2)"])
    lknee_angle = angle_between_vectors(vectors["lknee_vec1(25_1)"], vectors["lknee_vec2(25_2)"])

    rhip_angle = angle_between_vectors(vectors["rhip_vec1(24_1)"], vectors["rhip_vec2(24_2)"])
    rknee_angle = angle_between_vectors(vectors["rknee_vec1(26_1)"], vectors["rknee_vec2(26_2)"])

    lsh_angle = angle_between_vectors(vectors["lsh_vec1(11_1)"],vectors["lsh_vec2(11_2)"])
    lelb_angle = angle_between_vectors(vectors["lelb_vec1(13_1)"],vectors["lelb_vec2(13_2)"])

    rsh_angle = angle_between_vectors(vectors["rsh_vec1(12_1)"],vectors["rsh_vec2(12_2)"])
    relb_angle = angle_between_vectors(vectors["relb_vec1(14_1)"],vectors["relb_vec2(14_2)"])


    angles = {"lhip_angle(23)": lhip_angle,
              "lknee_angle(25)": lknee_angle,
              
              "rhip_angle(24)": rhip_angle,
              "rknee_angle(26)": rknee_angle,
              
              "lsh_angle(11)": lsh_angle, 
              "lelb_angle(13)": lelb_angle,
              
              "rsh_angle(12)": rsh_angle, 
              "relb_angle(14)": relb_angle,}
    return angles


def write_json_to_csv(csv_path, json_value):
    file_exists = os.path.isfile(csv_path) and os.path.getsize(csv_path) > 0
    with open(csv_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, json_value.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(json_value)