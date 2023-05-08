FROM python:latest

WORKDIR /usr/app/src

# take all files located in the current dir and copy them into the image
COPY . .

# install modules into the image
RUN pip install -r requirements.txt

CMD ["python", "/main.py"]