#coding:utf-8
#画像を縦に並べる

import numpy as np
from PIL import Image

def loadimage(imagename):#画像を開く関数
	img = Image.open(imagename)#画像の読み込み
	img = np.asarray(img).astype(np.float32)#読み込んだ画像をnumpy配列として保存
	return img

def img_stack(img1, img2):
	img = np.vstack((img1, img2))
	return img

if __name__ == "__main__":
	data = np.loadtxt("result.txt", delimiter="\n", dtype="string")
	images = map(loadimage, data)
	v = np.vstack(images)
	Image.fromarray(np.uint8(v)).save("stkimage.png")
	"""check = True
	for x in data:
		img = loadimage(x)
		print(x)
		if check == True:
			v = img
			check = False
		else:
			v = img_stack(v, img)
	Image.fromarray(np.uint8(v)).save("stkimage.png")"""
