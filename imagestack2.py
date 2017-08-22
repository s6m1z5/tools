#coding:utf-8
#画像を横に並べる

import numpy as np
from PIL import Image

def loadimage(imagename):#画像を開く関数
	img = Image.open(imagename)#画像の読み込み
	img = np.asarray(img).astype(np.float32)#読み込んだ画像をnumpy配列として保存
	return img

if __name__ == "__main__":
	data = np.loadtxt("names2.csv", delimiter=",", dtype="string")
	images = map(loadimage, data)
	a = []
	for i in range(0, len(data), 10):
		a.append(images[i:i+10])

	for k in range(len(a)):
		h = np.hstack(a[k])
		Image.fromarray(np.uint8(h)).save("stkimage_2_%03d.png"%k)