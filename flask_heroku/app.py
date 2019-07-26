# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:48:20 2019

@author: rays
"""

from flask import Flask
import cv2
import numpy as np
#from matplotlib import pyplot as plt
 
img=cv2.imread(r'C:\Users\rays\Desktop\Bdiameter\s1.jpg')
#print(img.shape)
cropped = img[530:1250, 710:2000]  # 剪裁座標為[y0:y1, x0:x1]

#plt.imshow(cropped,'gray')
#plt.show()

edges=cv2.Canny(cropped,190,255)		#canny
#print (img.shape)
#print (img.dtype)
#print (img.size)
#print (type(img))
#print (edges.shape)
#
#plt.imshow(edges,'gray')
#plt.savefig('test')
#plt.show() 


img_array = np.array(edges)

#X-direction pixel measure
x=1500		#x > image_size
y=0

for i in range (0,720): 		#range(Y-dir sum of pixel) ->> column from top 
    u = edges[i]
    for j in range(0,1290):	    #range(X-dir sum of pixel) ->> pixel from left
        if (u[j]>0 and j<x):
           x=j
        if (u[j]>0 and j>y):
           y=j
print(x)
print(y)


#Y_direction pixel measure
a=1500		#a > image_size
b=0
for i in range (0,1290):		#range(X-dir sum of pixel) ->> row from left
    v = edges[:,i]
    for j in range(0,720):	    #range(Y-dir sum of pixel) ->> pixel from top
        if (v[j]>0 and j<a):
           a=j
        if (v[j]>0 and j>b):
           b=j
print(a)
print(b)


#pixel*pixel_size = diameter           
size1=(y-x)*0.0183			
size2=(b-a)*0.0183
#print("x直徑為",size1,"mm")    
#print("y直徑為",size2,"mm")


app = Flask(__name__)

@app.route("/")
def home():
    return "x直徑為%f mm, y直徑為%f mm" %(size1,size2)

if __name__ == "__main__":
    app.run()