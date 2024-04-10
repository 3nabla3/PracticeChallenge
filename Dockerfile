FROM python:3.10

WORKDIR /app
RUN apt-get update && apt-get upgrade
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN rm db.sqlite3
RUN chmod +x ./scripts/entrypoint.sh

CMD "./scripts/entrypoint.sh"