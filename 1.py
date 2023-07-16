import numpy as np

F = open("/home/adryian/api-datasets/SRTM_BLR.tif", "r")

A = np.array(F.read())


print(A)
