#coding:utf-8

from captcha.image import ImageCaptcha
import numpy as np
from PIL import Image
import random
import sys

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def random_captcha_text(char_set = number,char = alphabet, captcha_size = 4):
    captcha_text = []
    for i in range(captcha_size):
        # ch = char_set+char
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text

def gen_captcha_text_and_image():
    image = ImageCaptcha(width=120)
    captcha_text = random_captcha_text()
    captcha_text = ''.join(captcha_text)
    captcha = image.generate(captcha_text)
    image.write(captcha_text,'D:/WorkSpace/data/imageDatas/numberimage/'+captcha_text + '.jpg')
num = 10000
if __name__ == '__main__':
    for i in range(num):
        gen_captcha_text_and_image()
        sys.stdout.write('\>> Creating image %d/%d' % (i+1,num))
    sys.stdout.write('\n')
    sys.stdout.flush()
    print("生成完毕")
