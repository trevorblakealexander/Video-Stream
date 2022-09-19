import cv2

def livestream():
    # Replace "address" with RTSP stream address.
    stream = cv2.VideoCapture("address")
    
    # Replace "name" with the name of the stream.
    while(True):
        _, frame = stream.read()
        cv2.imshow("name", frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    stream.release()
    cv2.destroyAllWindows()

livestream()