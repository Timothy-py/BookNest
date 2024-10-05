FROM python:3.10-slim

WORKDIR /frontend

COPY ./requirements.txt /frontend/requirements.txt

RUN pip install --no-cache-dir  --upgrade -r /frontend/requirements.txt

COPY ./app /frontend/app
COPY ./main.py /frontend/main.py

EXPOSE 8081

CMD [ "fastapi", "run", "/frontend/main.py", "--port", "8081" ]