import cv2

legCascade= cv2.CascadeClassifier("resources/legs_haarcascade.xml")
faceCascade= cv2.CascadeClassifier("resources/face_cascade.xml")
#faceCascade= cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
#faceCascade= cv2.CascadeClassifier("resources/cascade_arms_update_white_background.xml")
torsoCascade= cv2.CascadeClassifier("resources/torso_cascade.xml")

path = 'resources/images/05.jpg'
img = cv2.imread(path)
'''
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", imgGray)
'''
faces = faceCascade.detectMultiScale(img,1.1,4)#1.1,4 for the face, #1.2,4 for eye ,#1.02,4, #1.01,5 lowerbody, 1.005,4 upper body, TORSO 1.1,6

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
'''
cv2.imshow("Result", img)
    
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''
####################################
torso = torsoCascade.detectMultiScale(img,1.5,6)#1.1,4 for the face, #1.2,4 for eye ,#1.02,4, #1.01,5 lowerbody, 1.005,4 upper body, TORSO 1.1,6

for (x,y,w,h) in torso:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

########################################
legs = legCascade.detectMultiScale(img,1.1,5)#1.1,4 for the face, #1.2,4 for eye ,#1.02,4, #1.01,5 lowerbody, 1.005,4 upper body, TORSO 1.1,6

for (x,y,w,h) in legs:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

########################################
cv2.imshow("Result", img)
cv2.waitKey(0)