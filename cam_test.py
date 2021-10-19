import cv2

cap = cv2.VideoCapture(0) # 0 mean first webcam

if cap.isOpened():
    while True:
        state, frame = cap.read()
        if state:
            cv2.imshow("Video",frame)
            if cv2.waitKey(1) == 27: # click on esc to quit
                break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('Camera not working')