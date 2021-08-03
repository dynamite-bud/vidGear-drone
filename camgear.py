# import required libraries
from vidgear.gears import CamGear
import cv2


# open any valid video stream(for e.g `myvideo.avi` file)
stream = CamGear(source='udpsrc port=9000 caps = "application/x-rtp, media=video, clock-rate=90000, encoding-name=H264, payload=96"  ! rtph264depay ! decodebin ! videoconvert ! video/x-raw, format=BGR ! appsink').start()
# stream = CamGear(source='udpsrc port=9000 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96"  ! rtph264depay ! decodebin ! videoconvert ! video/x-raw, format=BGR ! appsink').start()
# stream = CamGear(source='udpsrc port=9000 caps = "application/x-rtp, media=video, clock-rate=90000, encoding-name=H264, payload=96" ! rtph264depay ! avdec_h264 ! autovideosink').start() 
# stream = CamGear(source='udpsrc port=9000 caps = "application/x-rtp, media=video, clock-rate=90000, encoding-name=H264, payload=96"  ! rtph264depay ! avdec_h264 ! autovideosink ! appsink').start() 

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        # break
        continue

    row, col = 100, 100
    # {do something with the frame here}
    cv2.circle(frame,(row, col), 200, (0,255,0), -1)
    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()