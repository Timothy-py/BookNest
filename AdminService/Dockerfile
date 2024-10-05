FROM python:3.10-slim

WORKDIR /admin

COPY ./requirements.txt /admin/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /admin/requirements.txt

COPY ./app /admin/app
COPY ./main.py /admin/main.py

EXPOSE 8080

CMD [ "fastapi", "run", "/admin/main.py", "--port", "8080" ]