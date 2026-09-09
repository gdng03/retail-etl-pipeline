FROM python:3.12-slim

WORKDIR /app

# install uv
RUN pip install --no-cache-dir uv

# file dependency 
COPY pyproject.toml uv.lock ./

# package
RUN uv sync --frozen --no-dev

# copy source code
COPY . .

CMD ["uv", "run", "python", "main.py"]