pTime = 0
import cv2
import mediapipe as mp
import time
import handTrackingModule as htm

cTime = 0
webcam = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = webcam.read()
    img = detector.findHands(img, draw = False)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList)!=0:
        print(lmList[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 1)
        cv2.imshow("Test webcam", img)
        cv2.waitKey(1)