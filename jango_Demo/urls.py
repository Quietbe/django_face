"""jango_Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from dp import views

urlpatterns = [
    path('',views.index),
    path("admin/", admin.site.urls),
    path("index/", views.index),
    path("updata/", views.updata), #上传
    path("delete/", views.delete), #删除数据
    path('people_face/', views.people_face), #人脸识别
    path('people_face_redis/', views.people_face_redis), #人脸识别redis



]
