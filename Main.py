import random
from file import File
from s3uploader import S3UPloader
from device import Device
import os
from event import Event
import asyncio


async def main():
    position_limit = os.getenv("LIMIT_POSITION")
    file_type = os.getenv("FILE_EXTENSION")
    events = []
    while True:
        random_event_position = random.randrange(int(os.getenv("RANDOM_EVENT_POSITION")))
        device = Device()
        event = Event(device=device)
        if len(events) <= random_event_position:
            events.insert(random_event_position, event)
        else:
            current_position = events[random_event_position].currentPosition
            if current_position >= position_limit:
                events.remove(events[random_event_position])
            else:
                current_position = events[
                    random_event_position
                ].currentPosition + random.randrange(15)
                events[random_event_position].currentPosition = current_position
                events[random_event_position].generateRandomEvent()
                events[random_event_position].setTimeStamp()
                event = events[random_event_position]
        print(str(event))
        file_name = f"({str(event.device.device_id)}  {str(event.timestamp.second)} {str(file_type)}"  
        file = File(file_name)
        await file.write(str(event.parse_to_json()))
        await S3UPloader.upload_file(file_name)    # type: ignore
        await file.remove()


if __name__ == "__main__":
    asyncio.run(main())
