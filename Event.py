import datetime
import random
import uuid
import os
from dotenv import load_dotenv

class Event:
 
  load_dotenv()
  eventTypes = os.getenv("EVENT_TYPE")
  if eventTypes :
    eventTypes= eventTypes.split(",")
  playEvent=os.getenv("PLAY_EVENT")
  playingEvent=os.getenv("PLAYING_EVENT")
  stopEvent=os.getenv("STOP_EVENT")

  def __init__(self, device):
    self.device=device
    self.currentPosition= random.randrange(15)
    
  def setTimeStamp(self):
    self.timestamp= datetime.datetime.now()
        
  def setRandomEventType(self):
    if self.eventTypes:
      self.eventType= self.eventTypes[random.randrange(0,3)]
  
  def getTimeStamp(self):
    return self.timestamp

  def generateRandomEvent(self):
    if self.eventType == self.playEvent:
      self.setRandomEventType()
    elif self.eventType== self.playingEvent:
      if self.eventTypes:
        self.eventType= self.eventTypes[random.randrange(1,3)]
    elif self.eventType== self.stopEvent:
      if self.eventTypes:
        self.eventType= self.eventTypes[random.choice([0,2])]

  def setRandomContentId(self):
    self.contentId=uuid.uuid1()
  
  def parseToJson(self):
    return {
      "timestamp": self.timestamp,
      "eventType": self.eventType,
      "contentId": self.contentId,
      "device":  self.device.parseToJson(),
      "currentPosition": self.currentPosition
    }

  def __str__(self):
    return "Event: " + str(self.timestamp) + " " + str(self.eventType) + " " + str(self.contentId) + " " + str(self.device.deviceType)+ " " + str(self.device.deviceId) + " " +str(self.currentPosition)