# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import StreamGear
import cv2
from cv2 import VideoWriter


# open any valid video stream(for e.g `myvideo.avi` file)
stream = CamGear(source='udpsrc port=9000 caps = "application/x-rtp, media=video, clock-rate=90000, encoding-name=H264, payload=96"  ! rtph264depay ! decodebin ! videoconvert ! video/x-raw, format=BGR ! appsink').start()
##streamer = StreamGear(output="D:/downloads/Real-Time-Violence-Detection-in-Video--master/voilence_detect_temp/dash_out.mpd")
# loop over
framerate = 25.0
#'tcpserversink host=192.168.48.15 port=5000 sync=false'
#"appsrc ! videoconvert ! x264enc noise-reduction=10000 tune=zerolatency byte-stream=true threads=4 " \
 #             " ! h264parse ! mpegtsmux ! rtpmp2tpay ! udpsink host=127.0.0.1 port=5000"
##out = cv2.VideoWriter('appsrc ! videoconvert ! '
  ##                    'rtpmp4vpay send-config = true noise-reduction=10000 speed-preset=ultrafast tune=zerolatency ! '
  ##                    'udpserversink host=192.168.0.106 port=5000 sync=false',
  ##                    0, framerate, (640, 480))
##out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc ! mpegtsmux ! tcpserversink  port=8554 host=0.0.0.0', cv2.CAP_GSTREAMER,0, 20, (f_width,f_height), True)
streamer = StreamGear(output="./voilence_detect_temp/dash_out.mpd")
i=0
while i<50000:
    i+=1
    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break


    # {do something with the frame here}


    #send frame to streamer
    streamer.stream(frame)
    # Show output window
    # cv2.imshow("Output Frame", frame)
    #out.write(frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()
#out.release()
streamer.terminate()
