import cv2
import copy
#import numpy as np

colorImage = cv2.imread('sd.png')
I = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY)

cv2.imshow('GRI',I)
cv2.waitKey(0)

blur = cv2.GaussianBlur(I,(5,5),0)

cv2.imshow('BLUR',blur)
cv2.waitKey(0)

#kernel = np.ones((5,5),np.uint8)

#opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)

#cv2.imshow('homie',opening)
#cv2.waitKey(0)

gaus = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 45, 22)
cv2.imshow('THRESHOLD',gaus)
cv2.waitKey(0)

#closing = cv2.morphologyEx(gaus, cv2.MORPH_CLOSE, kernel)
#cv2.imshow('son',closing)
#cv2.waitKey(0)

contour, hierarchy = cv2.findContours(gaus, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

gausKopya = copy.copy(gaus)

cevrit = cv2.drawContours(gausKopya,contour, -1, (0,255,0),3)
cv2.imshow('Filtre oncesi cevritler',cevrit)
cv2.waitKey(0)


#areas = 0
for contours in contour:
    if (75 < cv2.contourArea(contours) < 25000):
#       areas = cv2.contourArea(contours) + areas
        x,y,w,h = cv2.boundingRect(contours)
        occupyRate = cv2.contourArea(contours) / (w * h)
        if (0.2 < occupyRate <= 0.9):
            aspectRatio = float(w)/h
            if(aspectRatio <= 3):
                perimeter = cv2.arcLength(contours,True)
                compactness = cv2.contourArea(contours) / (perimeter * perimeter)
                if(0.008 < compactness <= 0.95):
                    image = cv2.drawContours(gaus, [contours], -1, (0, 255, 0), cv2.FILLED, 8)
                    S = cv2.fillPoly(colorImage,pts=[contours],color=(255,255,255))

#print(areas,'Toplam Contour Alanı')


#occupyRate = areas / (w * h)


cv2.imshow('Son cevritler',image)
cv2.waitKey(0)

cv2.imshow('Son Görsel',S)
cv2.waitKey(0)
