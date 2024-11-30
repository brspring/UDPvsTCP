#!/bin/bash

apt-get update -y && apt-get upgrade -y

apt install -y python3 python3-pip
apt install -y vim nano curl wget iproute2 net-tools
pip3 install --no-cache-dir --upgrade pip
pip3 install --no-cache-dir requests

echo "Ambiente configurado com sucesso!"

# Adicione este comando ao final para manter o container ativo
/bin/bash