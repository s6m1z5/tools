#coding:utf-8
#python2.7
#モノクロ画像を.csvに変換して保存する

import numpy as np
from PIL import Image

def loadimage(imagename):#画像を開く関数
	img = Image.open(imagename)#画像の読み込み
	img = np.asarray(img).astype(np.float32)#読み込んだ画像をnumpy配列として保存
	return img

if __name__ =="__main__":
	filename = str(raw_input("input image file name:"))
	im = loadimage(filename)
	np.savetxt("image.csv", im, delimiter=",")
	print("img saved.")
