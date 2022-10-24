import datetime
import random
import uuid
import os

class Event:

    event_types = os.getenv("EVENT_TYPE")
    if event_types:
        event_types = event_types.split(",")
    play_event = os.getenv("PLAY_EVENT")
    playing_event = os.getenv("PLAYING_EVENT")
    stop_event = os.getenv("STOP_EVENT")

    def __init__(self, device):
        self.device = device
        self.current_position = random.randrange(15)
        self.set_random_content_id()
        self.event_type= self.random_event_type()
        self.timestamp=datetime.datetime.now()

    
    def random_event_type(self):
        if self.event_types:
            return self.event_types[random.randrange(0, 3)]

    def get_time_stamp(self):
        """ Get timestamp."""
        return self.timestamp

    def generate_random_event(self):
        """Generates a random event depending of current event type ."""
        if self.event_type == self.play_event:
            self.event_type= self.random_event_type()
        elif self.event_type == self.playing_event:
            if self.event_types:
                self.event_type = self.event_types[random.randrange(1, 3)]
        else:
            if self.event_types:
                self.event_type = self.event_types[random.choice([0, 2])]

    def set_random_content_id(self):
        """ Set random content id."""
        self.content_id = uuid.uuid1()

    def parse_to_json(self):
        """ Format event information to json format."""
        return {
            "timestamp": self.timestamp,
            "eventType": self.event_type,
            "contentId": self.content_id,
            "device": self.device.parse_to_json(),
            "currentPosition": self.current_position,
        }

    def __str__(self):
        """ Format event information to string format."""
        return (
            f"Event: { str(self.timestamp)} { str(self.event_types)}{ str(self.content_id)}{ str(self.device.device_type)}{ str(self.device.device_id)}{ str(self.current_position)}"
        )
