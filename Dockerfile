FROM python:3.6
EXPOSE 8000
EXPOSE 5432
ENV PYTHON_UNBUFFERED=1

RUN mkdir /code
WORKDIR /code


RUN apt-get update && apt-get install -y python-pip python-dev \
    libpq-dev postgresql postgresql-contrib

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./src /code/

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
