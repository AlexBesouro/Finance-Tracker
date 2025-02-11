
FROM python:3.12

WORKDIR usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main.app:app", "--host", "0.0.0.0", "--port", "--reload"]