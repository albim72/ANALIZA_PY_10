# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np

arr = np.array([[1.,2.,3.],[6.,8.,9.]])
arr

arr*arr

arr**2

arr-arr

1/arr

arr**0.5

arr2 = np.array([[0.,4.,1.],[7.,5.,14.]])
arr2

arr2>arr

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[2]

arr2d[0][2]

arr2d[0,2]

zl = [[1,2,3],[4,5,6],[7,8,9]]

zl[0][2]

#tensor  - tablica 3d
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d

arr3d[0]

arr3d[1]

old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d

arr3d[0] = old_values
arr3d

arr3d[1,0,1]

arr3d.shape

names = np.array(['Ola','Anna','Piotr','Leon','Kinga','Jan','Jan'])
data = np.random.randn(7,4)
names

data

names == 'Jan'

data[names=="Jan"]

data[names=="Jan",2:]

data[names=="Jan",3]

names != "Jan"

data[~(names=='Jan')]

