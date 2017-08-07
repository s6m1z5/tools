#coding:utf-8
#python2.7
#画像を縦に並べる

import numpy as np
from PIL import Image
FILENAME = "names.csv"#画像ファイル名が,区切りで縦に並べられたファイル

def loadimage(imagename):#画像を開く関数
	img = Image.open(imagename)#画像の読み込み
	img = np.asarray(img).astype(np.float32)#読み込んだ画像をnumpy配列として保存
	return img

if __name__ == "__main__":
	data = np.loadtxt(FILENAME, delimiter=",", dtype="string")
	images = map(loadimage, data)#画像をすべて開く
	v = np.vstack(images)#画像を縦に並べる
	Image.fromarray(np.uint8(v)).save("stkimage.png")
	print("img saved.")
