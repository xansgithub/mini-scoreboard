FROM ubuntu

COPY . .

WORKDIR /src

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3" "-m" "flask" "run" "main.py" ]