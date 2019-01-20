FROM python:3.8.5-slim

WORKDIR /srv/ltcoe
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "src.cli"]
