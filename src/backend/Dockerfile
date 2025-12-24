# UV Python base image
FROM ghcr.io/astral-sh/uv:python3.10-trixie AS base

# Working directory inside the container
WORKDIR /app

# Copy the configuration files
COPY pyproject.toml uv.lock .python-version ./

# Set environment variables
ENV UV_COMPILE_BYTECODES=1 UV_LINK_MODE=copy

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.look,target=/app/uv.look \
    --mount=type=bind,source=pyproject.toml,target=/app/pyproject.toml \
    uv sync --frozen --no-dev

# Copy the source code
COPY src /app/src

# Copy flask source code
COPY main.py /app

# Python final image
FROM python:3.10-slim-bookworm AS final

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 

# Set environment variables
ARG VERSION=0.1.0
ENV APP_VERSION=$VERSION

# Set working directory inside the container
WORKDIR /app

# Copy the virtual environment from the base image
COPY --from=base /app /app
COPY --from=base /root/.local /root/.local

# Add the virtual environment to the PATH
ENV PATH=/app/.venv/bin:$PATH

# Expose the port
EXPOSE 2020

# Run the application
CMD ["python", "main.py"]


