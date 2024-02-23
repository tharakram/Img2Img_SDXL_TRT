FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

ENV PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 \
    python3 python3-venv \
    git \
    wget \
    vim \
    net-tools \
    iproute2 \
    ca-certificates \
    libgomp1 \
    libopenblas-dev \
    liblapack-dev \
    build-essential autoconf libtool pkg-config \
    ssh \
    python3-dev \
    python3-pip \
    python-is-python3 \
    cmake && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN mkdir /.cache
RUN chmod 777 /.cache
RUN chmod -R 777 /app

RUN pip3 install --no-cache-dir -r /app/requirements.txt

RUN pip3 install polygraphy==v0.47.1 onnx_graphsurgeon --extra-index-url https://pypi.ngc.nvidia.com

COPY . /app/

WORKDIR /app

CMD ["python", "gradio_app.py"]