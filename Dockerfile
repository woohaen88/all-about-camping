FROM python:3.10

WORKDIR /home/

RUN git clone https://github.com/woohaen88/all-about-camping.git

WORKDIR /home/all-about-camping/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations && \
    python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]