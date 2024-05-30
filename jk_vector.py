def extract_vector(keypoints):

    # vector 지점(23,25, 24,26, 11,13, 12,14)
    
    #[23.lhip] 11-23-25
    lhip_vec1 = [keypoints["11. left_shoulder"][0]-keypoints["23. left_hip"][0],
                 keypoints["11. left_shoulder"][1]-keypoints["23. left_hip"][1],
                 keypoints["11. left_shoulder"][2]-keypoints["23. left_hip"][2]]
    
    lhip_vec2 = [keypoints["25. left_knee"][0]-keypoints["23. left_hip"][0],
                 keypoints["25. left_knee"][1]-keypoints["23. left_hip"][1],
                 keypoints["25. left_knee"][2]-keypoints["23. left_hip"][2]]
    #[25.lknee] 23-25-27
    lknee_vec1 = [keypoints["23. left_hip"][0]-keypoints["25. left_knee"][0],
                  keypoints["23. left_hip"][1]-keypoints["25. left_knee"][1],
                  keypoints["23. left_hip"][2]-keypoints["25. left_knee"][2]]
    
    lknee_vec2 = [keypoints["27. left_ankle"][0]-keypoints["25. left_knee"][0],
                  keypoints["27. left_ankle"][1]-keypoints["25. left_knee"][1],
                  keypoints["27. left_ankle"][2]-keypoints["25. left_knee"][2]]
    

    #[24.rhip] 12-24-26
    rhip_vec1 = [keypoints["12. right_shoulder"][0]-keypoints["24. right_hip"][0],
                 keypoints["12. right_shoulder"][1]-keypoints["24. right_hip"][1],
                 keypoints["12. right_shoulder"][2]-keypoints["24. right_hip"][2]]
    
    rhip_vec2 = [keypoints["26. right_knee"][0]-keypoints["24. right_hip"][0],
                 keypoints["26. right_knee"][1]-keypoints["24. right_hip"][1],
                 keypoints["26. right_knee"][2]-keypoints["24. right_hip"][2]]
    #[26.rknee] 24-26-28
    rknee_vec1 = [keypoints["24. right_hip"][0]-keypoints["26. right_knee"][0],
                  keypoints["24. right_hip"][1]-keypoints["26. right_knee"][1],
                  keypoints["24. right_hip"][2]-keypoints["26. right_knee"][2]]
    
    rknee_vec2 = [keypoints["28. right_ankle"][0]-keypoints["26. right_knee"][0],
                  keypoints["28. right_ankle"][1]-keypoints["26. right_knee"][1],
                  keypoints["28. right_ankle"][2]-keypoints["26. right_knee"][2]]

    
    #[11.lsh] 13-11-23
    lsh_vec1 = [keypoints["13. left_elbow"][0]-keypoints["11. left_shoulder"][0],
                keypoints["13. left_elbow"][1]-keypoints["11. left_shoulder"][1],
                keypoints["13. left_elbow"][2]-keypoints["11. left_shoulder"][2]]
    
    lsh_vec2 = [keypoints["23. left_hip"][0]-keypoints["11. left_shoulder"][0],
                keypoints["23. left_hip"][1]-keypoints["11. left_shoulder"][1],
                keypoints["23. left_hip"][2]-keypoints["11. left_shoulder"][2]]
    #[13.lelb] 15-13-11
    lelb_vec1 = [keypoints["15. left_wrist"][0]-keypoints["13. left_elbow"][0],
                 keypoints["15. left_wrist"][1]-keypoints["13. left_elbow"][1],
                 keypoints["15. left_wrist"][2]-keypoints["13. left_elbow"][2]]
    
    lelb_vec2 = [keypoints["11. left_shoulder"][0]-keypoints["13. left_elbow"][0],
                 keypoints["11. left_shoulder"][1]-keypoints["13. left_elbow"][1],
                 keypoints["11. left_shoulder"][2]-keypoints["13. left_elbow"][2]]
    

    #[12.rsh] 14-12-24
    rsh_vec1 = [keypoints["14. right_elbow"][0]-keypoints["12. right_shoulder"][0],
                keypoints["14. right_elbow"][1]-keypoints["12. right_shoulder"][1],
                keypoints["14. right_elbow"][2]-keypoints["12. right_shoulder"][2]]
    
    rsh_vec2 = [keypoints["24. right_hip"][0]-keypoints["12. right_shoulder"][0],
                keypoints["24. right_hip"][1]-keypoints["12. right_shoulder"][1],
                keypoints["24. right_hip"][2]-keypoints["12. right_shoulder"][2]]
    #[14.relb] 16-14-12
    relb_vec1 = [keypoints["16. right_wrist"][0]-keypoints["14. right_elbow"][0],
                 keypoints["16. right_wrist"][1]-keypoints["14. right_elbow"][1],
                 keypoints["16. right_wrist"][2]-keypoints["14. right_elbow"][2]]
     
    relb_vec2 = [keypoints["12. right_shoulder"][0]-keypoints["14. right_elbow"][0],
                 keypoints["12. right_shoulder"][1]-keypoints["14. right_elbow"][1],
                 keypoints["12. right_shoulder"][2]-keypoints["14. right_elbow"][2]]


    vectors = {"lhip_vec1(23_1)": lhip_vec1,  
              "lhip_vec2(23_2)": lhip_vec2,
              "lknee_vec1(25_1)": lknee_vec1, 
              "lknee_vec2(25_2)": lknee_vec2,
              
              "rhip_vec1(24_1)": rhip_vec1,  
              "rhip_vec2(24_2)": rhip_vec2,
              "rknee_vec1(26_1)": rknee_vec1 , 
              "rknee_vec2(26_2)": rknee_vec2,
              
              "lsh_vec1(11_1)":lsh_vec1, 
              "lsh_vec2(11_2)":lsh_vec2,
              "lelb_vec1(13_1)":lelb_vec1,
              "lelb_vec2(13_2)":lelb_vec2,
              
              "rsh_vec1(12_1)":rsh_vec1, 
              "rsh_vec2(12_2)":rsh_vec2,
              "relb_vec1(14_1)":relb_vec1,
              "relb_vec2(14_2)":relb_vec2}

    return vectors