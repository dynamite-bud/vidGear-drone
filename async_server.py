# import libraries
from vidgear.gears.asyncio import NetGear_Async
import asyncio

#initialize Server with suitable source and enable stabilization
# server=NetGear_Async(source='/home/foo/foo1.mp4', stabilize=True, logging=True).launch()
server=NetGear_Async(source=0, address='192.168.0.100', port='5454', protocol='tcp',  pattern=2, logging=True).launch()

if __name__ == '__main__':
    #set event loop
    asyncio.set_event_loop(server.loop)
    try:
        #run your main function task until it is complete
        server.loop.run_until_complete(server.task)
    except (KeyboardInterrupt, SystemExit):
        #wait for interrupts
        pass
    finally:
        # finally close the server
        server.close()