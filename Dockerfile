FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update -y
RUN apt-get install default-jre -y

COPY ./ ./

CMD ./init.sh
EXPOSE 5000