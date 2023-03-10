# 从仓库拉取镜像文件
FROM python:3.9
# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 设置pip源为国内源
COPY pip.conf /root/.pip/pip.conf

# 在容器内创建mysite文件夹
RUN mkdir -p /code

# 设置容器内工作目录
WORKDIR /code

# 将当前目录文件加入到容器工作目录中（. 表示当前宿主机目录）
ADD . /code

# pip安装依赖
RUN pip install -r requirements.txt

RUN pip install pip -U && pip install -r requirements.txt
