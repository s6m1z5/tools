#coding:utf-8
#画像ファイル名が並んだ.csvの画像名を変更する

import numpy as np

def main():
	data = np.loadtxt("./data2.csv", delimiter=",", dtype="string")
	names = data[:, 0]
	labels = data[:, 1]
	data2 = []
	for i in range(len(names)):
		rename = names[i].replace("./", "./datasets/")
		data2.append([rename, labels[i]])

	np.savetxt('./data2.csv',data2,fmt="%s",delimiter=',')
	"""data2_a = data2[0::2]#偶数番目の要素
				data2_b = data2[1::2]#奇数番目の要素
				np.savetxt("./data_train.csv", data2_a, fmt="%s", delimiter=",")
				np.savetxt("./data_test.csv", data2_b, fmt="%s", delimiter=",")"""

if __name__ == "__main__":
	main()