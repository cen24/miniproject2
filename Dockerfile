FROM python:3

ADD . .

RUN pip3 install pandas

CMD [ "python", "../src/Cal2Test.py" ]