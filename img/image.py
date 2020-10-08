# 两个图片拼接
from os import listdir
from PIL import Image


def pinjie(width, height):
    # 获取当前文件夹中所有JPG图像
    im_list = [Image.open(fn) for fn in listdir() if fn.endswith('.jpg')]
    # 图片转化为相同的尺寸
    ims = []
    for i in im_list:
        new_img = i.resize((width, height), Image.BILINEAR)
        ims.append(new_img)
    # 单幅图像尺寸
    width, height = ims[0].size
    # 创建空白长图,横向拼接
    # result = Image.new(ims[0].mode, (width, height * len(ims)))
    result = Image.new(ims[0].mode, (width * len(ims), height))
    # 拼接图片
    for i, im in enumerate(ims):
        # result.paste(im, box=(0, i * height))
        result.paste(im, box=(i * width, 0))
    # 保存图片
    result.save('res1.jpg')


if __name__ == '__main__':
    pinjie(828, 1792)
