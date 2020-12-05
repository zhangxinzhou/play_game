import cv2
import os

file_path = r'E:\gta5\collect_data\2'
file_list = os.listdir(file_path)
for file_name in file_list:
    file_full_path = os.path.join(file_path, file_name)
    mat = cv2.imread(file_full_path)
    text = file_full_path
    cv2.putText(mat, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.imshow('window', mat)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
