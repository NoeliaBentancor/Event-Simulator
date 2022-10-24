from random import randrange
import uuid
import os
class Device:
    devices_types = os.getenv("DEVICE_TYPES")
    if devices_types:
        devicesTypes = devices_types.split(",")

    def __init__(self):
        self.set_random_device()

    def set_random_device(self):
        """ Set random device."""

        device_id = randrange(3)
        if self.devices_types:
            self.device_type = self.devices_types[device_id]
        self.device_id = uuid.uuid1()

    def parse_to_json(self):
        """ Format device information to json format."""
        return {"deviceType": self.device_type, "deviceId": self.device_id}
