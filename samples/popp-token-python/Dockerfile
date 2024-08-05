FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./popp /app/popp
COPY ./server.py /app/server.py

CMD ["fastapi", "run", "server.py", "--port", "80"]