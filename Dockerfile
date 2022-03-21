FROM python:3.10.3-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHON_ENV production

EXPOSE 8000

CMD ["python", "main.py"]
