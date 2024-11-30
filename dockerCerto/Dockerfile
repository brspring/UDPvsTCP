FROM ubuntu:latest

# Define o frontend do apt como não interativo
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes e instala Python 3, Vim e outros utilitários necessários
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    vim \
    && apt-get clean

# Cria o diretório de trabalho
WORKDIR /scripts

# Configura o container para permanecer ativo
CMD ["/bin/bash"]
