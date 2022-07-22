FROM williambutcherbot/python:latest

RUN apt-get install -y neofetch ffmpeg sudo

RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3", "-m", "KiritoRobot"]
