import cv2

#faceCascade= cv2.CascadeClassifier("resources/haarcascade_eye.xml")
#faceCascade= cv2.CascadeClassifier("resources/haarcascade_upperbody.xml")
#faceCascade= cv2.CascadeClassifier("resources/haarcascade_lowerbody.xml")
#faceCascade= cv2.CascadeClassifier("resources/haarcascade_fullbody.xml")
#faceCascade= cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")



#faceCascade= cv2.CascadeClassifier("resources/legs_haarcascade.xml")
faceCascade= cv2.CascadeClassifier("resourcesface_cascade.xml")
#faceCascade= cv2.CascadeClassifier("resources/cascade_arms_update_white_background.xml")
#faceCascade= cv2.CascadeClassifier("resources/torso_cascade.xml")


img = cv2.imread('resources/images/person5.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", imgGray)
#imgBlur = cv2.GaussianBlur(img,(5,5),0)
#cv2.imshow("Blur Image", imgBlur)
faces = faceCascade.detectMultiScale(img,1.1,4)#1.1,4 for the face, #1.2,4 for eye ,#1.02,4, #1.01,5 lowerbody, 1.005,4 upper body, TORSO 1.1,6

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", img)
cv2.waitKey(0)




'''

cascade= cv2.CascadeClassifier("resources/haarcascade_upperbody.xml")
imgPath = 'resources/img_big_03.png'
img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

body = cascade.detectMultiScale(
    gray,
    scaleFactor = 1.01,
    minNeighbors = 5,
    minSize = (30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in body:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Upper Body',img)
cv2.waitKey(0)'''