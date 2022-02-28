FROM python:3.9.10
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5001
CMD ["flask","run"]