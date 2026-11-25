FROM python:3.11-slim

# Install package reqs
COPY /src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest
COPY . .

# Change working directory to source code
WORKDIR /src

# Flask magic
ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0

CMD [ "python", "-m", "flask", "run"]