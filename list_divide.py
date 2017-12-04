#coding:utf-8
#.csvの内容を奇数番の要素と偶数番の要素に分割する

import numpy as np

def main():
	data = np.loadtxt("./data.csv", delimiter=",", dtype="string")
	
	data_a = data[0::2]#偶数番目の要素
	data_b = data[1::2]#奇数番目の要素
	np.savetxt("./data_a.csv", data_a, fmt="%s", delimiter=",")
	np.savetxt("./data_a.csv", data_b, fmt="%s", delimiter=",")

if __name__ == "__main__":
	main()