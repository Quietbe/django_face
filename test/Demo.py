# import cv2
# import sys
# import importlib
#
# #入门图片操作方法
# def test_base(self):
#     cv2 = self.cv2
#     #读图
#     img = cv2.imread("E:\Pycharm\Works\人脸\img.png")
#     #创建并展示图片
#     cv2.namedWindow("Image")
#     #显示图片
#     cv2.imshow("Image",img)
#     #延迟窗口显示时间
#     cv2.waitKey(0)
#     #释放窗口
#     cv2.destroyAllWindows()
#
# #图片操作方法
# def test_do_img(self):
#     cv2 = self.cv2
#     #读取原图
#     img = cv2.imread("E:\Pycharm\Works\人脸\img.png")
#
#     #降噪操作
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
#     #改变图片尺寸
#     img_copy = cv2.resize(gray,(600,600))
#
#     #写入新图
#     cv2.imwrite("love2.jpg",img_copy)
#
#     #压缩图片 压缩jpg 阈值范围 是0-100
#     cv2.imwrite("E:\Pycharm\Works\人脸\img.png",img,[int(cv2.IMWRITE_JPEG_QUALITY),20])
#     #显示图片
#     cv2.imshow("Image",img_copy)
#
#     #延迟窗口
#     cv2.waitKey(0)
#
#     #释放窗口
#     cv2.destroyAllWindows()
#
# test_do_img(cv2)
#
# import cv2
# import sys
# import importlib
#
# #重置系统模块
# importlib.reload(sys)
#
#
# class TestCv2(object):
#     def init(self, cv2):
#         self.cv2 = cv2
#         #声明初始化 cv2模块
#         cv2.namedWindow("shibie")
#         #1调用摄像头
#         cap=cv2.VideoCapture(0)
#         #2人脸识别器分类器 里面有很多种
#         classfier=cv2.CascadeClassifier("C:/Users/ww/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#
#         while cap.isOpened():
#             ok,frame=cap.read() #读取一帧数据
#             if not ok:
#                 break
#
#         #2灰度转换
#         grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#
#         #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
#         faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
#         classfier.detectMultiScale() #即是完成实际人脸识别工作的函数，该函数参数说明如下：
#         #grey：要识别的图像数据（即使不转换成灰度也能识别，但是灰度图可以降低计算强度，因为检测的依据是哈尔特征，转换后每个点的RGB数据变成了一维的灰度，这样计算强度就减少很多）
#         #scaleFactor：图像缩放比例，可以理解为同一个物体与相机距离不同，其大小亦不同，必须将其缩放到一定大小才方便识别，该参数指定每次缩放的比例






import cv2

filepath = "img.png"
#法读取出的图片格式为BGR格式，并不是通常的RGB格式。imread()方法的两个返回值，ret为布尔类型，表示是否正确打开图片；image为图片的三维矩阵
image = cv2.imread(filepath)
#cvtColor(p1,p2)方法用来改变色彩空间，参数p1是需要转换的图片，参数p2是转换成的格式。
# 对于BGR—>灰色转换，我们使用标志cv2.COLOR_BGR2GRAY;同样，对于BGR —>HSV，我们使用标志cv2.COLOR_BGR2HSV。
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#加载分类器  cv自带的有 安装cv后就有了
classfier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#调用detectMultiScale()函数进行检测，调整参数可以使检测结果更加准确；
#scaleFactor：每次图像尺寸减小的比例
#minNeighbors：每一个目标至少被检测到3次才算检测到目标
#minSize：目标的最小尺寸
#maxSize：目标的最大尺寸
faceRect = classfier.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=3,minSize=(50,50))

if len(faceRect):
    for face in faceRect:
        x, y, w, h = face
        #对识别的人脸进行画框
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("frame0", image)
c = cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()





