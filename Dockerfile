FROM python:3.10-alpine

COPY . .

RUN pip install flask

CMD python main.py