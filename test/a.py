import redis

r = redis.Redis(host='localhost', port=6379, db=0, password='')
r.set('data', '这是一个测试值')




data = r.get('data')
print(data.decode('utf8'))
print(type(data))