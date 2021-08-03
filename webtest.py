# import libs
import uvicorn
from vidgear.gears.asyncio import WebGear

# initialize WebGear app  
web=WebGear(source="output.mp4",logging=True)

# run this app on Uvicorn server
uvicorn.run(web(), host='localhost', port=8000)

# close app safely
web.shutdown()