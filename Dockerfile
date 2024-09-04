FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]