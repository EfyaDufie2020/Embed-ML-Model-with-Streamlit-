# Use a specific version of Ubuntu for stability
FROM ubuntu:20.04
 
# Set working directory
WORKDIR /usr/app/src
 
# Set environment variables
ENV LANG="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8" \
    DEBIAN_FRONTEND=noninteractive
 
# Install necessary packages and Python 3.12
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    locales \
    software-properties-common \
    sudo \
    build-essential \
    cmake \
    libboost-all-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    wget \
    gnupg \
&& add-apt-repository ppa:deadsnakes/ppa \
&& apt-get update \
&& apt-get install -y python3.12 python3.12-distutils python3.12-venv \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
 
# Install pip for Python 3.12
RUN wget https://bootstrap.pypa.io/get-pip.py \
&& python3.12 get-pip.py \
&& rm get-pip.py
 
# Set Python 3.12 as the default python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
 
# Copy requirements file and install Python packages
COPY v_requirements.txt ./
 
# Upgrade pip and install packages
RUN python3.12 -m pip install --upgrade pip \
&& python3.12 -m pip install -r v_requirements.txt
 
# Copy the rest of the application code
COPY ./ ./
 
# Specify the command to run the application
CMD ["streamlit", "run", "1_Home.py"]