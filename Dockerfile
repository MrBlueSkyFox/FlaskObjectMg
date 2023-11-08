FROM python:3.10
RUN apt update

RUN apt-get install -y git
WORKDIR /app

RUN git clone https://github.com/MrBlueSkyFox/FlaskObjectMg.git
# Install the requirements.txt file
RUN pip install -r /app/FlaskObjectMg/requirements.txt
EXPOSE 5000
WORKDIR /app/FlaskObjectMg
COPY instance/config.py /app/FlaskObjectMg/instance
#RUN flask init-db
CMD ["python", "-m","flask","run","-h","0.0.0.0"]
