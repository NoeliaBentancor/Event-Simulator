import random
from File import File
from S3UPloader import S3UPloader
from Device import Device
import os
from Event import Event
from dotenv import load_dotenv
import asyncio


async def main():
    load_dotenv()
    contLimit=os.getenv("LIMIT_POSITION")
    fileType=os.getenv("FILE_EXTENSION")
    events=[]
    cont=1
    while cont>=0:
        cont=cont-1
        randomEventPosition= random.randrange(150)
        device=  Device()
        event =  Event(device=device)
        event.setRandomContentId()
        event.setRandomEventType()
        event.setTimeStamp()
        if events.__len__() <= randomEventPosition :
            events.insert(randomEventPosition, event)
        else:
            currentPosition= events[randomEventPosition].currentPosition
            if(currentPosition >= contLimit):
                events.remove(events[randomEventPosition])
            else:
                currentPosition= events[randomEventPosition].currentPosition+random.randrange(15)
                events[randomEventPosition].currentPosition= currentPosition
                events[randomEventPosition].generateRandomEvent()	
                events[randomEventPosition].setTimeStamp()
                event=events[randomEventPosition]
        print(  event.__str__())
        fileName=( event.device.deviceId.__str__() + event.timestamp.second.__str__() ) + fileType.__str__()  # type: ignore
        file= File(fileName)
        await file.write(event.parseToJson().__str__())
        await S3UPloader.upload_file(fileName)  # type: ignore
        await file.remove()
      
if __name__ == "__main__":
      asyncio.run(main())