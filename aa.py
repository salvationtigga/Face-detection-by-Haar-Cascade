import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Salvation\python\computer vision\face detection\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    """
    detectMultiScale() - scan & detect faces
    1.1 balance, not too slow, blind

    mineNeighbors = 5
    
    """

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)

        """
        x,y - top left corner of rectangle

        (x+w, y+h) - bottom right corner of rectangle

        face=[
        (90,100,150,80,80) face1
        (250,120,90,90) face2
        ]
        x- how far from left
        y- how far from top
        w- width of face
        h- height of face
        """

    cv2.imshow("Webcame Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

cap.release()
cv2.destroyAllWindows()
 