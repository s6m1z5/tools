#coding:utf-8
#python2.7
#現在のディレクトリに存在するファイル名を取得する

import numpy as np
import glob

a = glob.glob("./*")#*.jpgのように拡張子を指定できる, *のみにすればすべてのファイル名を抽出
np.savetxt("filenames.csv", np.array(a), delimiter=",", fmt="%s")
