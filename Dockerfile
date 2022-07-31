FROM python:3.9
ENV SECRET_KEY django-insecure-e)+bkkb*0=9@vi7fgxg@t2usjc17&437s3vd^g+6)g192o^5y@
ENV DEBUG True
ENV ALLOWED_HOSTS *
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY ./requirments.txt /home
RUN pip install -U pip && pip install -r /home/requirments.txt
COPY . /home
WORKDIR /home/jadee
RUN DJANGO_SUPERUSER_PASSWORD=kg47CKkYk45FsKD python manage.py createsuperuser --no-input --username=userjadee  --email=info@jadee.org
# RUN python manage.py runserver
ENTRYPOINT ["python3", "manage.py"]
CMD [ "runserver", "0.0.0.0:8000" ]
