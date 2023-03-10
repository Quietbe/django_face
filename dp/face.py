# 人脸识别modle
import os
import cv2
from jango_Demo.settings import BASE_DIR
from django.core.cache import cache
import base64
import numpy as np


class People_face():

    # 得到图像地址本地版本
    def getpath(file):

        # # up_path = BASE_DIR,'/dp/files/people_face.png'
        # # up_path = os.path.join(BASE_DIR, 'dp/file', file.name)
        up_path = os.path.join(BASE_DIR, 'static/img', file.name)
        # print('----------------------')
        # print(up_path)
        with open(up_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
            # f.write(rq.FILES['file'].read())
        # 人脸识别
        # 法读取出的图片格式为BGR格式，并不是通常的RGB格式。imread()方法的两个返回值，ret为布尔类型，表示是否正确打开图片；image为图片的三维矩阵
        image = cv2.imread(up_path)
        # cvtColor(p1,p2)方法用来改变色彩空间，参数p1是需要转换的图片，参数p2是转换成的格式。
        # 对于BGR—>灰色转换，我们使用标志cv2.COLOR_BGR2GRAY;同样，对于BGR —>HSV，我们使用标志cv2.COLOR_BGR2HSV。
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 加载分类器  cv自带的有 安装cv后就有了
        xml_path = os.path.join(BASE_DIR, 'dp/files', "haarcascade_frontalface_default.xml")
        classfier = cv2.CascadeClassifier(xml_path)
        # 调用detectMultiScale()函数进行检测，调整参数可以使检测结果更加准确；
        # scaleFactor：每次图像尺寸减小的比例
        # minNeighbors：每一个目标至少被检测到3次才算检测到目标
        # minSize：目标的最小尺寸
        # maxSize：目标的最大尺寸
        faceRect = classfier.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=2, minSize=(50, 50))

        if len(faceRect):
            for face in faceRect:
                x, y, w, h = face
                # 对识别的人脸进行画框
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 写入文件
        # face_path = os.path.join(BASE_DIR, 'dp/files, 'face.jpg')
        # face_name = f"{time.time()}.jpg"
        face_name = "face.jpg"

        face_path = os.path.join(BASE_DIR, 'static/img', face_name)
        cv2.imwrite(face_path, image)

        # cv2.imshow("frame0", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # print(up_path, face_path)
        return [file.name, face_name]

    # 得到图像地址redis版本
    # import redis
    # from django.core.cache import cache
    # import base64dao
    # import numpy as np
    # import cv2
    def getpath_redis(self, ti):
        # 上传文件地址
        # r = redis.Redis(host='localhost', port=3679, password='970209', db=0)
        # r.set('up_file', file.read())
        # file = r.get('up_file')
        # print(file)
        # print('type:',type(file))

        data = self.read()
        # print('data:', data)
        # print('type:', type(data)) #bytes
        cache.set('up_file', data)
        file__ = cache.get('up_file')
        # print(file)
        # print('type:',type(file))
        # 将 bytes 编码为 base64 字符串
        file_ = base64.b64encode(file__).decode('utf-8')
        # print(file)
        # print(type(file))

        ### 将 base64字符串 解码为 字节数据，然后读取图片
        file_im = base64.b64decode(file_)
        # 将 字节数据 解码为 OpenCV 图像
        image_array = np.frombuffer(file_im, np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        # 检查图像是否为空
        if image is None:
            print("读取图像失败！")
        else:
            # 将图像转为灰度图
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # # 显示图像
        # cv2.imshow('Image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 进行图像人脸识别
        xml_path = os.path.join(BASE_DIR, 'dp/files', "haarcascade_frontalface_default.xml")
        classfier = cv2.CascadeClassifier(xml_path)
        faceRect = classfier.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=2, minSize=(50, 50))

        if len(faceRect):
            for face in faceRect:
                x, y, w, h = face
                # 对识别的人脸进行画框
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        ### 将图片存在本地
        # face_name = "aaa.jpg"
        # face_path = os.path.join(BASE_DIR, 'static/img', face_name)
        # cv2.imwrite(face_path, image)

        # 将图像转换为字符串
        retval, buffer = cv2.imencode('.jpg', image)
        face_bs64 = base64.b64encode(buffer).decode('utf-8')
        # print("face:",face_bs64)

        cache.set(f'{ti}', file_)
        cache.set(f'{ti}_', face_bs64)
        # return file_, face_bs64
        return ti
