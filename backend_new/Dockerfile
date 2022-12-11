FROM python:3.9
ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip install pyaudio
RUN pip install tensorflow
RUN pip install google-cloud-speech
RUN pip install google-cloud-vision
RUN pip install -r requirements.txt # Write Flask in this file
RUN pip install protobuf==3.20.*
RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
RUN apt-get update
RUN	apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 5000
CMD [ "python", "app.py" ]
