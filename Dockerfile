FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install .

ENTRYPOINT ["python3", "-m", "src.parser"]

CMD ["--help"]
