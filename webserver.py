from flask import Flask, render_template, Response, request
from camera import VideoCamera
from thread import start_new_thread

StreamStatus = "0"
start = 0

def Stream():
    while(True):
        global StreamStatus
        readStreamStatus = open("Stream.txt").read()
        StreamStatus = readStreamStatus
        

app = Flask("main")

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        global StreamStatus
        if(StreamStatus == "1"):
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            camera.__del__()
            continue

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def runWeb():
    start_new_thread(Stream, ())
    app.run(host='0.0.0.0', debug=True)
    
runWeb()

