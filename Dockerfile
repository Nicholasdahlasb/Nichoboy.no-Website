FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade Jinja2
RUN pip install --upgrade Flask
EXPOSE 80
ENV NAME World
CMD ["python", "app.py"]
