FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "5000", "--debug"]
CMD ["python", "app.py", "--host", "10.0.0.125", "--port", "5000", "--debug"]
