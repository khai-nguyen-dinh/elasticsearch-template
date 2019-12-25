FROM python:alpine3.7
COPY .. /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python main.py