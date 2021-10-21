import cv2

cap = cv2.VideoCapture(0) # 0 mean first webcam

face_cascade = cv2.CascadeClassifier('face_classifier.xml')

if cap.isOpened():
    while True:
        state, frame = cap.read()
        if state:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) > 0:
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)
            cv2.imshow("Video",frame)
            if cv2.waitKey(1) == 27: # click on esc to quit
                break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('Camera not working')