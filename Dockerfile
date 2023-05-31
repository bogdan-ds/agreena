FROM python:3.8

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

ENV SCI_HUB_USER=hummingbirdtech
ENV SCI_HUB_PASS=AqVcjl2AqbXy6mnE03qk

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]
