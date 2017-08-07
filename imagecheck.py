#coding:utf-8
#モノクロ画像を.csvに変換して保存

import numpy as np
from PIL import Image

def loadimage(imagename):#画像を開く関数
	img = Image.open(imagename)#画像の読み込み
	img = np.asarray(img).astype(np.float32)#読み込んだ画像をnumpy配列として保存
	return img

def zerocheck(nparray):#画素がすべて0かそうでないかを判断
	checker = (nparray==0)
	b = checker.all()
	return b 

if __name__ =="__main__":
	filename = str(raw_input("画像ファイル名を入力:"))
	im = loadimage(filename)
	np.savetxt("image.csv", im, delimiter=",")
	check = zerocheck(im)
	if check==True:#配列の全要素がTrue,すなわちimの全要素がゼロの場合
		print("dead map!")
	else:
		print("img saved.")