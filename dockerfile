FROM python:alpine3.15

WORKDIR /usr/src/app

COPY temp_big.txt ./

COPY lineReader.py ./

CMD ["python","./lineReader.py"]