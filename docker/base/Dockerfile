FROM flink:1.16.0

#docker build -t flink-base --platform linux/amd64 .
# install python3: it has updated Python to 3.9 in Debian 11 and so install Python 3.7 from source
# it currently only supports Python 3.6, 3.7 and 3.8 in PyFlink officially.

RUN apt-get update -y && \
apt-get install -y git vim build-essential liblzma-dev libssl-dev zlib1g-dev libbz2-dev libffi-dev && \
wget https://www.python.org/ftp/python/3.8.16/Python-3.8.16.tgz && \
tar -xvf Python-3.8.16.tgz && \
cd Python-3.8.16 && \
./configure --without-tests --enable-shared && \
make -j6 && \
make install && \
ldconfig /usr/local/lib && \
cd .. && rm -f Python-3.8.16.tgz && rm -rf Python-3.8.16 && \
ln -s /usr/local/bin/python3 /usr/local/bin/python && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

echo "state.checkpoints.dir: file:///tmp/checkpoints" >> /opt/flink/conf/flink-conf.yaml
echo "execution.checkpointing.interval: 10s" >> /opt/flink/conf/flink-conf.yaml

# install PyFlink
RUN pip3 install apache-flink==1.16.0