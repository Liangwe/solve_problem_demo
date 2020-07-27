# iphone5 size:1136*640

from PIL import Image
import os

def get_file(path):
    photo_file = []
    result = os.listdir(path)
    for file in result:
        if '.jpg'  or '.png' or '.jpeg' in file:
            photo_file.append(file)
    return photo_file

def Image_PreProcessing(path,filename,width,height):
    im = Image.open(path + filename)
    img_size = im.size
    img_format = im.format
    w = img_size[0]
    h = img_size[1]
    if w >= width and h >= height:
        imBackground = im.resize((width,height),Image.ANTIALIAS)
        imBackground.save("result/"+ filename,img_format)
        print('完成' + filename)
    else:
        pass


if __name__ == "__main__":
    path = "photo/"
    photos = get_file(path)
    for i in range(len(photos)):
        Image_PreProcessing(path,photos[i],1136,640)

