# Dockerfile for building environment for django-file-upload demo
# This is to test uploading of huge files

FROM python:3.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

LABEL author=gisat.cz
LABEL description="QC tool environment, big file upload"

ENV PYTHONPATH=/usr/local/src/django-jquery-file-upload/src

# Upgrade the base system.
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y python3-pip \
    && pip3 install --upgrade pip \
    && apt-get install -y git

# Install application from GitHub
RUN cd /usr/local/src \
    && git clone https://github.com/jirikadlec2/django-jquery-file-upload \
    && cd django-jquery-file-upload/src \
    && pip3 install -r ./requirements.txt

# Run frontend application.
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]
