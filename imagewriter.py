# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2


# open any valid video stream(for e.g `myvideo.avi` file)
stream = CamGear(source='udpsrc port=9000 caps = "application/x-rtp, media=video, clock-rate=90000, encoding-name=H264, payload=96"  ! rtph264depay ! decodebin ! videoconvert ! video/x-raw, format=BGR ! appsink').start() 


output_params = {
                    "-profile:v":"main",
                    "-preset:v":"veryfast",
                    "-g":60,
                    "-keyint_min":60,
                    "-sc_threshold":0,
                    "-b:v":"2500k",
                    "-maxrate":"2500k",
                    "-bufsize":"2500k",
                    "-f":"rawvideo"
                }

o_p={
    "-f": "rawvideo",
    "-pixel_format":"rgb24",
    "-video_size": "1280x720",
    "-input_framerate":stream.framerate
}
writer = WriteGear(output_filename = 'http://localhos
t:8090/feed1.ffm', logging =True, **o_p)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    row, col = 100, 100
    # {do something with the frame here}
       
    cv2.circle(frame,(row, col), 200, (0,255,0), -1)
    # Show output window
    writer.write(frame)
    cv2.imshow("Output Frame", frame)
    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()