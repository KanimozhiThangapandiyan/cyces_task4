FROM python:3.10

WORKDIR /task4

COPY . /task4

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]