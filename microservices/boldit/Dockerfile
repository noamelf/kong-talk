FROM python:3.5
RUN pip install flask
COPY . /app
WORKDIR /app

EXPOSE 5001

CMD python wsgi.py
