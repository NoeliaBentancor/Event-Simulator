
FROM python:3.7

WORKDIR .

RUN pip install boto3 && pip install python-dotenv  

COPY . .

CMD [ "python", "Main.py" ]