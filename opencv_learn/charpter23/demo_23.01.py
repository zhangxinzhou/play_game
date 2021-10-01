import cv2

# 读取待检测的图像
image = cv2.imread(r'aaa.jpg')
# 获取xml文件,加载人脸检测器
faceCascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
# 色彩转换,转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 调用函数detectMultiScale
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5)
)
print(faces)
# 打印输出的测试结果
print("发现{0}个人脸!".format(len(faces)))
# 逐个标注人脸
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)  # 矩形标注
    # cv2.circle(image, (int((w + w + w) / 2), int((y + y + h) / 2)), int(w / 2), (0, 255, 0), 2)
# 显示结果
cv2.imshow("dect", image)
# 保存检测结果
cv2.imwrite("re.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
