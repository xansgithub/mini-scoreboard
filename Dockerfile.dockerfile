FROM ubuntu

WORKDIR /src

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install requirements.txt

COPY . . 

CMD [ "python3" "-m" "flask" "run" "main.py" ]