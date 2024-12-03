FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install .

# Run cli_parser specified in setup when the container launches
ENTRYPOINT ["cli_parser"]

CMD ["--help"]
