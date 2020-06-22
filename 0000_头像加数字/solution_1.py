'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。
'''

from PIL import Image, ImageFont, ImageDraw  # 从PIL库导入所需模块
def add_num(file,num):
    image = Image.open(headFile, 'r')
    w,h = image.size #得到图片长宽
    font = ImageFont.truetype(font=r'C:/Windows/Fonts/arial.ttf',size=int(h/7))  #不同系统的字体位置视情况而定
    ImageDraw.Draw(image).text((w*0.76,h*0.02), num ,font = font, fill = 'red')

    image.show() #展示绘制结果
    image.save('result.jpg') #保存绘制结果
    print('保存成功')

if __name__ == "__main__":
    num = input("请输入信息数目：")
    headFile = "head_pic.jpg"  # 头像文件
    headFile2 = "head_pic2.jpg"  # 头像文件

    add_num(headFile,num)