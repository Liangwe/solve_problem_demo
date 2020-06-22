import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

with open("../0001_生成优惠券/Coupon.txt", 'r', encoding='utf-8') as f:
    fp = f.readlines()

for i in range(len(fp)):
    r.set(i+1, fp[i].replace('\n',''))

print(r.get(5))