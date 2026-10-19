FROM python:3.12-slim

WORKDIR /app

copy requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

copy app.py .

EXPOSE 5000

CMD ["python", "app.py"]

