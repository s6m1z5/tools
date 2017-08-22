#coding:utf-8
#画像を横に並べる

import numpy as np
from PIL import Image

num = 10#画像を一度に並べる枚数

def loadimage(imagename):#画像を開く関数
	img = Image.open(imagename)#画像の読み込み
	img = np.asarray(img).astype(np.float32)#読み込んだ画像をnumpy配列として保存
	return img

if __name__ == "__main__":
	data = np.loadtxt("names.csv", delimiter=",", dtype="string")#names.csvは並べたい画像名がカンマ区切りで並べられたファイル
	images = map(loadimage, data)
	a = []
	for i in range(0, len(data), num):#画像をnum枚ごとの配列に格納する
		a.append(images[i:i+num])

	for k in range(len(a)):#配列に含まれる画像を連結
		h = np.hstack(a[k])#横に連結,縦の場合はvstack
		Image.fromarray(np.uint8(h)).save("stkimage_2_%03d.png"%k)
