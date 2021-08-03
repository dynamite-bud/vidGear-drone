#import necessary libs
import uvicorn, asyncio, cv2
import numpy as np
from starlette.routing import Route
from vidgear.gears.asyncio import WebGear
from vidgear.gears.asyncio.helper import reducer
from starlette.responses import StreamingResponse

#initialize WebGear app with a valid source you want to use
# web = WebGear(source = "output.mp4", logging = True) #also enable `logging` for debugging 
web = WebGear(source='udpsrc port=9000 caps = "application/x-rtp, media=video, clock-rate=90000, encoding-name=H264, payload=96"  ! rtph264depay ! decodebin ! videoconvert ! video/x-raw, format=BGR ! appsink')


#create your own frame producer
async def my_frame_producer():
        # loop over frames
        while True:
                #read frame from provided source
                frame = web.stream.read()
                #break if NoneType
                if frame is None: break


                #do something with frame here
                row, col = 100, 100
                cv2.circle(frame,(row, col), 200, (0,255,0), -1)
                #reducer frames size if you want more performance otherwise comment this line
                # frame = reducer(frame, percentage = 50) #reduce frame by 50%
                # print(type(frame))
                # #handle JPEG encoding
                encodedImage = cv2.imencode('.jpg', frame)[1].tobytes()
                # #yield frame in byte format
                yield  (b'--frame\r\nContent-Type:image/jpeg\r\n\r\n'+encodedImage+b'\r\n')
                await asyncio.sleep(0.01)
                # yield 5


#now create your own streaming response server
async def video_server(scope):
        assert scope['type'] == 'http'
        return StreamingResponse(my_frame_producer(), media_type='multipart/x-mixed-replace; boundary=frame') #add your frame producer



#append new route to point your own streaming response server created above
web.routes.append(Route('/my_frames', endpoint=video_server)) #new route for your frames producer will be `{address}/my_frames`

#run this app on Uvicorn server at address http://0.0.0.0:8000/
uvicorn.run(web(), host='192.168.0.103', port=8000)

#close app safely
web.shutdown()
