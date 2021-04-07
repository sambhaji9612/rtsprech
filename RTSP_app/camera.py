import numpy
import cv2
import mysql.connector
import  time
class StartCamera(object):
    def __init__(self):

        self.url = cv2.VideoCapture(0)  # replace 0 with RTSP Link

    def __del__(self):

        cv2.destroyAllWindows()

    def get_frame(self):
        success, imgNp = self.url.read()
        resize = cv2.resize(imgNp, (640, 480), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', resize)

        return jpeg.tobytes()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
date_time = time.strftime("recording %H-%M -%d %m %y")  # set current time as video name
output = cv2.VideoWriter('RTSP_app/footages/' + date_time + '.avi', fourcc, 20.0, (640, 480))

# conn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "RTSP_DATA")
# curs = conn.cursor()
#
# q = "INSERT INTO video(strem) values (?),"
# v = output
# curs.execute(q,v)
#
#
#














