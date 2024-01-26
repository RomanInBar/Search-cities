FROM python:3.10
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN alembic upgrade head
CMD gunicorn main:app --bind=0.0.0.0:8000
