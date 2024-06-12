FROM flink:1.17.1

# Set environment variables
ENV CONDA_INSTALLER_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    MINICONDA_DIR=/opt/miniconda \
    CONDA=/opt/miniconda/bin/conda \
    PYTHON=/opt/miniconda/envs/env/bin/python

# environment variables
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=all
ENV NVIDIA_REQUIRE_CUDA "cuda>=12.2"

# Update and install dependencies
RUN apt-get update -y && \
    apt-get install -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Download and install Miniconda
RUN wget $CONDA_INSTALLER_URL -O miniconda.sh && \
    /bin/bash miniconda.sh -b -p $MINICONDA_DIR && \
    rm miniconda.sh

# Create a new environment named 'env'
COPY environment.yml .
RUN $CONDA env create -f environment.yml && \
    $CONDA clean -afy

# Ensure conda is on PATH
ENV PATH="$MINICONDA_DIR/bin:$PATH"

# Activate the 'env' environment
SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint-ollama.sh /entrypoint-ollama.sh
RUN chmod +x /entrypoint-ollama.sh

ENV LD_LIBRARY_PATH="$MINICONDA_DIR/envs/env/lib:${LD_LIBRARY_PATH}"

CMD ["/opt/miniconda/envs/env/bin/python", "main.py"]