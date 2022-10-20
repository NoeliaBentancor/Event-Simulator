from random import randrange
import uuid
from dotenv import load_dotenv
import os
import asyncio

class Device:
    load_dotenv()
    devicesTypes = os.getenv("DEVICE_TYPES")
    if devicesTypes :
        devicesTypes= devicesTypes.split(",")
    def __init__(self) :
         self.setRandomDevice()

    def setRandomDevice(self):
        deviceId= randrange(3)
        if self.devicesTypes:
            self.deviceType= self.devicesTypes[deviceId]
        self.deviceId= uuid.uuid1()
   
    def parseToJson(self):
        return {
            "deviceType": self.deviceType,
            "deviceId": self.deviceId
    }