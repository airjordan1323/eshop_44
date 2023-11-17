FROM python:3.10.8

WORKDIR /django_44

COPY . /django_44

EXPOSE 8000

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]