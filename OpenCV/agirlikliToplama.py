import cv2
import numpy as np

resim1 = cv2.imread("images/kousei.jpg")
resim2 = cv2.imread("images/piano.jpg")

toplam = cv2.add(resim1,resim2)
agirlikliToplam = cv2.addWeighted(resim1,0.6,resim2,0.4)

cv2.imshow("toplam",toplam)
cv2.imshow("AgirlikliToplam",agirlikliToplam)

cv2.waitKey(0)
cv2.destroyAllWindows()