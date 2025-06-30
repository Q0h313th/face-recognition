FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    git \
    vim \
    wget \
    build-essential \
    python3-pip \
    ca-certificates \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create user
RUN useradd -m -s /bin/bash guest
USER guest
WORKDIR /home/guest

# Clone LatentSync
RUN git clone https://github.com/bytedance/LatentSync.git

# Install Minicondia into /home/guest
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /home/guest/miniconda && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Set Conda path in environment
ENV PATH="/home/guest/miniconda/bin:$PATH"

SHELL ["/bin/bash", "-c"]

# Create conda environment and install required packages
RUN conda init && \
    conda create -y -n latentsync python=3.10 && \
    echo "conda activate latentsync" >> ~/.bashrc && \
    source ~/.bashrc && \
    pip install --upgrade pip && \
    pip install opencv-python==4.9.0.80 'numpy<2.0' && \
    conda install -y -c conda-forge libstdcxx-ng

RUN pwd && ls -la 
 
WORKDIR /home/guest/LatentSync

# Activate env and run setup_env.sh
RUN . /home/guest/miniconda/etc/profile.d/conda.sh && \
    conda activate latentsync && \
    ./setup_env.sh

# Default to bash shell
CMD ["bash", "--login"]

