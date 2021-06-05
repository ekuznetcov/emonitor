FROM python:3.8.3-alpine
LABEL maintainer='ekuznetcov'

WORKDIR /app

# COPY requirements.txt .
# RUN apk upgrade
# RUN pip install -r requirements.txt
# COPY . . 
RUN apk add --no-cache gcc musl-dev linux-headers
        
ADD . /app
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# run the command to start uWSGI

EXPOSE 5000
CMD ["uwsgi", "app.ini"]