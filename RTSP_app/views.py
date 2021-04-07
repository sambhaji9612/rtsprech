import cv2
import os

from django.shortcuts import render
from RTSP_app.camera import StartCamera

from django.http.response import StreamingHttpResponse

def showIndex(request):
    return render(request,'index.html')

def startRec(request):
    msg = 'camera Started'
    return render(request,'index.html',{'message':msg})
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b''
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')






def startCamera(request):
    return StreamingHttpResponse(gen(StartCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def showRecording(request):

    path = r'C:\Users\sambh\PycharmProjects\Django\RTSP_Recorder\RTSP_app\footages'

    l = os.listdir(path)

    return  render(request , 'index.html',{'recordin':l})
