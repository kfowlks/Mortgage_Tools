FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN mkdir /static
WORKDIR /static
COPY /static .

RUN mkdir /templates
WORKDIR /templates
COPY /templates .

RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]