from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from dp.models import DataInfo
import os
import cv2
import time
from django.conf import settings

BASE_DIR = settings.BASE_DIR
STATIC_URL = settings.STATIC_URL


# 文档打分系统
def index(req):
    if req.method == 'POST':
        # data = req.POST
        file_name = req.POST.get('file_name')
        try:
            file = req.FILES['file']
        except:
            return redirect('/index/?error=请选择文件')
        # file = req.FILES.get('file')
        fraction = req.POST.get('fraction')
        people_name = req.POST.get('people_name')

        print(file_name, file, fraction, people_name)
        print("文件类型", type(file))
        print(file)
        try:
            DataInfo.objects.create(file_name=file_name, file=file, fraction=fraction, people_name=people_name)
            return redirect('/index/?error=存入成功')
        except:
            return render(req, 'index.html', {'error': '存入失败'})
    if req.method == 'GET':

        error = req.GET.get('error') if req.GET.get('error') != None else ''
        print('error:', error)
        data_list = DataInfo.objects.all()
        list_data = []
        for i in data_list:
            list_data.append([i.id,
                              i.file_name,
                              i.file,
                              i.fraction,
                              i.people_name
                              ])
        print(list_data)
        return render(req, 'index.html', {'error': error, 'data_list': list_data})


# 未用，上传接口
def updata(req):
    # data = req.POST
    file_name = req.POST.get('file_name')

    file = req.FILES['file']
    # file = req.FILES.get('file')
    fraction = req.POST.get('fraction')
    people_name = req.POST.get('people_name')

    print(file_name, file, fraction, people_name)
    print("文件类型", type(file))
    print(file)

    try:
        DataInfo.objects.create(file_name=file_name, file=file, fraction=fraction, people_name=people_name)
        return render(req, 'index.html', {'error': '存入成功'})
    except:
        return render(req, 'index.html', {'error': '存入失败'})
    # print(data)


# 文档打分系统删除接口
def delete(req):
    if req.method == "POST":
        id = req.POST.get('id')
        DataInfo.objects.filter(id=id).delete()
        if DataInfo.objects.filter(id=id).exists() == False:
            return redirect('/index/?error=删除成功')
        else:
            return render(req, 'index.html', {'error': '删除失败'})
    else:
        return redirect('/index/?error=删除成功')


# 人脸识别
from dp.face import People_face
def people_face(rq):
    if rq.method == 'POST':
        try:
            file = rq.FILES['file']
        except:
            return redirect('/index/?error=请选择图像')
        filename, face_name = People_face.getpath(file)
        return render(rq, 'index.html', {'people_face': f"img/{file.name}", 'face': f"img/{face_name}"})
    else:
        return redirect('/index/?error=未知错误')


# 人脸识别 redis
# from dp.models import People_face
# import base64
# import numpy as np
from django.core.cache import cache
#人脸识别 存储在数据redis中
def people_face_redis(rq):
    if rq.method == "POST":
        try:
            file = rq.FILES['file']
        except:
            render(rq, 'index.html', {'error': '请选择图片'})
        # 获取图片的格式
        # up_file_base64, face_base64 = People_face.getpath_redis(file, time.time())

        name = People_face.getpath_redis(file, time.time())
        up_file_base64 = cache.get(name)
        face_base64 = cache.get(f'{name}_')

        # print('----------------------------------')
        # print(up_file_base64, face_base64)
        # print(type(file))
        # print(face_base64)
        return render(rq, 'index.html', {'up_file_base64': up_file_base64, 'face_base64': face_base64})

        # except:
        #     return redirect('/index/?error=请选择图像')


