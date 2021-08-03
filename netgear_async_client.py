# import libraries
from vidgear.gears.asyncio import NetGear_Async
import cv2, asyncio

#define and launch Client with `receive_mode=True`. #change following IP address '192.168.x.xxx' with yours
# client=NetGear_Async(address='192.168.0.100', port='5454', protocol='tcp',  pattern=2, receive_mode=True, logging=True).launch()
NetGear_Async(source='udpsrc port=9000 caps = "application/x-rtp, media=video, clock-rate=90000, encoding-name=H264, payload=96" ! rtph264depay ! avdec_h264 ! autovideosink')
# client=NetGear_Async(source='192.168.0.107',port='8160',protocol='tcp',pattern=2,receive_mode=True,logging=True).launch()
# client=NetGear_Async(source='http://192.168.0.107:8160/').launch()
# client=NetGear_Async(source='')



#Create a async function where you want to show/manipulate your received frames
async def main():
    # loop over Client's Asynchronous Frame Generator
    async for frame in client.recv_generator():


        # do something with received frames here


        # Show output window
        cv2.imshow("Output Frame", frame)
        key=cv2.waitKey(1) & 0xFF
        if key == ord("q"):
        #if 'q' key-pressed break out
            raise KeyboardInterrupt
        #await before continuing
        await asyncio.sleep(0.00001)


if __name__ == '__main__':
    #Set event loop to client's
    asyncio.set_event_loop(client.loop)
    try:
        #run your main function task until it is complete
        client.loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        #wait for interrupts
        pass

    # close all output window
    cv2.destroyAllWindows()
    # safely close client
    client.close()