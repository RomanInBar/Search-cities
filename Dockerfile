FROM python:3.10
RUN mkdir src
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN alembic upgrade head
CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicronWorker
