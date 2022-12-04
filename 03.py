import cv2
import numpy as np

main_img = cv2.imread("main.jpg", cv2.IMREAD_UNCHANGED)
bul_img = cv2.imread("find.jpg", cv2.IMREAD_UNCHANGED)



mainGray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
findobject_gray1 = cv2.cvtColor(bul_img, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(mainGray, findobject_gray1, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


w = bul_img.shape[1]
h = bul_img.shape[0]
cv2.rectangle(main_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)

print(w,h)  #image size fotoğraf boyutu
print(max_loc)  #kordinat x, y


cv2.imshow("ogo", main_img)
cv2.waitKey()
cv2.destroyWindow()

#fotografın icinde fotografı bul isaretle cıktı al