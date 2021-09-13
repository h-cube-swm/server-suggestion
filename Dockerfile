FROM python:3.9


WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y default-jre

COPY ./ ./

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

CMD [ "flask", "run" ]
EXPOSE 5000