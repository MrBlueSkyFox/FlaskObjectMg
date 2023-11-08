FROM python:3.10
RUN apt update

RUN apt-get install -y git
WORKDIR /app

COPY . /app/FlaskObjectMg
# Install the requirements.txt file
RUN pip install -r /app/FlaskObjectMg/requirements.txt
WORKDIR /app/FlaskObjectMg
COPY instance/config.py /app/FlaskObjectMg/instance
CMD ["python", "-m","flask","run","-h","0.0.0.0"]
