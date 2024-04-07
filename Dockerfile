FROM ubuntu:jammy
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install python3-pip
COPY requirements.txt /model/
RUN pip3 install -r /model/requirements.txt
COPY model.py /model/
COPY utils.py /model/
COPY rf_model.joblib /model/
RUN chmod +x /model/model.py
CMD /model/model.py --input=/data/test.csv --output=/data/aki.csv
