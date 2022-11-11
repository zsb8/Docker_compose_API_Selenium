FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get update
RUN apt install net-tools
RUN apt-get update
RUN apt install iputils-ping -y
COPY . .
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]


