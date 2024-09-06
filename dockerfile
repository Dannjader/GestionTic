FROM python:3.11-alpine3.18

ENV PYTHONUMBUFFERED=1

WORKDIR /sige_app

COPY requeriments.txt /sige_app/

RUN pip install --no-cache-dir -r requeriments.txt

COPY . /sige_app/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]