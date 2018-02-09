#coding:utf-8
#.csvの行と列を入れ替えて保存

import numpy as np

def main():
	csv = np.loadtxt("data.csv", delimiter=",", dtype=float)
	csv = csv.T
	np.savetxt("data_tranpose.csv", csv, delimiter=",")

if __name__ == '__main__':
	main()