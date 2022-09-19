import cv2

"""
Summary
-------
A function used to display the video stream from a given encoder.

Arguments
---------
src (str) - URL of the RTSP stream from the streaming encoder.
room (str) - Name of the room the streaming encoder resides.

Returns
-------
RTSP stream from encoder.
"""

def livestream(src, room):
    rtsp = src + "?resolution=1920x1080"

    stream = cv2.VideoCapture(rtsp)
    
    while(True):
        ret, frame = stream.read()
        cv2.imshow(room, frame)
        if cv2.waitKey(1) == ord("q"):
            break
        
    stream.release()
    cv2.destroyAllWindows()