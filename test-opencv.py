import cv2 

img = cv2.imread("D:\\Test\\test.jpg") 
cv2.namedWindow("Image") 
cv2.imshow("Image", img) 
cv2.waitKey (0)
cv2.destroyAllWindows()
cv2.imwrite("D:\\Test\\test2.jpg",img)
