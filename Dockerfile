FROM python:3-alpine3.23

WORKDIR /app

RUN mkdir -p /home/data /home/output

COPY scripts.py /app/scripts.py

COPY ./data/IF-1.txt /home/data/IF.txt
COPY ./data/AlwaysRememberUsThisWay-2.txt /home/data/AlwaysRememberUsThisWay.txt

CMD ["python", "scripts.py"]