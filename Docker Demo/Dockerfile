FROM python:3.12.3

#Setting a working directory in the container
WORKDIR /app

# Copying the pyfile and everything else into the /app folder
COPY . /app

# Installing dependencies
RUN pip install -r requirements.txt

# Running the application
ENTRYPOINT ["python", "Dockerdemo.py"]