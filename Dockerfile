FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mkdir static
EXPOSE 80
CMD ["python", "app.py"]
