# Event Simulator

Event Simulator is an application which simulates events and then uploads those events in json format to AWS S3.

# Environment Variables

```
EVENT_TYPE="PLAY,PLAYING,STOP"
LIMIT_POSITION=120
DEVICE_TYPES= "ANDROID,IOS, TV,DESKTOP"
EVENT_PLAY="PLAY"
EVENT_PLAYING="PLAYING"
EVENT_STOP="STOP"
FILE_EXTENSION=".json"
AWS_ACCESS_KEYS=""
AWS_SECRET_ACCESS_KEYS=""
S3_BUCKET="nbentancor"
AWS_SERVICE="s3"
```

AWS Access Keys and AWS Secret Access Keys should not be shared by any means in order so as to not compromise them.

## Run the project locally

```
python Main.py
```
## Docker Container

A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. 

### Build an image

```
docker build --tag event-simulator .
```

### Run a container based on the images built before

```
docker run event-simulator
```

