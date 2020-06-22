'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
要求过于简单，在此加入一些细节，统计中英混合文件中 中文和英文 以及符号 的出现次数
'''
# -*- coding: utf-8 -*-
import re  # 正则模块

class judge():
    '''
    判断是什么类型的符号
    '''
    def is_chinese(self, uchar):
        if (uchar >= u'\u4e00' and uchar <= u'\u9fa5'):
            return True
        else:
            return False

    def is_number(self, uchar):
        if (uchar >= u'\u0030' and uchar <= u'\u0039'):
            return True
        else:
            return False

    def is_english(self, uchar):
        if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
            return True
        else:
            return False

    def is_other(self, uchar):
        if not (self.is_chinese(uchar) or self.is_number(uchar) or self.is_english(uchar)):
            return True
        else:
            return False

def num(List):
    tmpdict = {}
    for b in List:
        tmpdict[b] = tmpdict.get(b, 0) + 1  # 统计次数
    result = list(tmpdict.items())  # 将字典转换为list  列表里面为元组类型
    result.sort(key=lambda x: x[1], reverse=True)
    return result

def out(result, n):
    try:
        for j in range(n):
            word, counts = result[j]
            print(word, counts)
    except:
        pass

if __name__ == "__main__":
    path = "test.txt"  #文件路径
    chinese = []
    english_word = []
    number = []
    other = []
    total = []
    with open(path, 'r', encoding="utf-8") as f:
        fp = f.read()
    data = fp.replace('\n', '').replace('\'s',' is').strip()

    english_word = re.findall('[a-zA-Z]+', data)
    number = re.findall('[0-9]+', data)
    j = judge()
    for i in data:
        if (j.is_chinese(i) == True):
            chinese.append(i)
        elif (j.is_other(i) == True):
            other.append(i)
    # print(chinese)
    # print(english_word)
    n = int(input('请输出要输出前几位次数最多的字（词）：'))
    if num(chinese)==[]:
        print('该文件没有汉字')
    else:
        print('出现次数最多的%d个汉字是：' % n)
        out(num(chinese),n)
    if num(english_word)==[]:
        print('该文件没有英文')
    else:
        print('出现次数最多的%d个英文单词是：' % n)
        out(num(english_word),n)
    if num(number)==[]:
        print('该文件没有数字')
    else:
        print('出现次数最多的%d个数字是：' % n)
        out(num(number),n)
    if other:
        print('出现的符号有：')
        for i in list(set(other)):
            if i != '':
                print(i)
    else:
        print('本文没有标点符号')

