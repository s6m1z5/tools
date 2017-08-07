#coding:utf-8

import numpy as np
import glob

a = glob.glob("./*.jpg")
np.savetxt("filenames.csv", np.array(a), delimiter=",", fmt="%s")