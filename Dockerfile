FROM python:3.11-slim

WORKDIR /src

RUN apt-get update && \
    apt-get install -y default-jre-headless wget git curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /src/
RUN pip install --upgrade pip && \
    pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . /src

EXPOSE 8501 8888

CMD ["streamlit", "run", "view/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
