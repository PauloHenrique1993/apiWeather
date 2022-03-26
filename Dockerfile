# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /app

# copy current project app to /app
COPY web-app/src /app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# install pip libs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "/app/app.py"] 
