FROM python:3.12-slim



ENV DEBIAN_FRONTEND=noninteractive

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1



RUN apt-get update && apt-get install -y --no-install-recommends \

  git \

  build-essential \

  && rm -rf /var/lib/apt/lists/*



WORKDIR /app



RUN git clone https://github.com/sunpy/sunpy.git . && \

  git checkout a1a081a



RUN pip install --no-cache-dir \

  setuptools>=62.1 \

  setuptools_scm[toml]>=6.2 \

  wheel \

  extension-helpers \

  "numpy>=2.0.0rc1,<2.3" \

  pytest



RUN pip install --no-cache-dir \

  astropy>=5.3.0 \

  packaging>=23.0 \

  parfive[ftp]>=2.0.0 \

  pyerfa>=2.0.0.1 \

  requests>=2.28.0 \

  fsspec>=2023.3.0



RUN pip install --no-cache-dir .



CMD ["pytest", "sunpy/time/tests/test_time.py"]