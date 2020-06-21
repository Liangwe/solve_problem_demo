'''
作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（
或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
此处加入检测重复的步骤
'''

import string
import random

coupon = []
def getCoupon(length):
    chars = string.ascii_letters + string.digits
    result = ''.join([random.choice(chars) for i in range(length)])
    if result not in coupon:
        coupon.append(result)
        return result
    else:
        return getCoupon(length)

def SaveCoupon(content):
    with open('Coupon.txt', 'w', encoding='utf-8') as f:
        f.write(content+'\n')

if __name__ == '__main__':
    tmp = ''
    for i in range(200):       #生成优惠码的数量
        value = getCoupon(25)  #指定优惠码长度
        tmp += value +'\n'

    SaveCoupon(tmp)

