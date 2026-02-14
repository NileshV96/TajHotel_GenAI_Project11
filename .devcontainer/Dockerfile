FROM python:3.11-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    build-essential \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for development
RUN useradd -m -s /bin/bash vscode

# Set working directory
WORKDIR /workspace

# Install Docker CLI (for Docker-in-Docker)
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

# Set user
USER vscode

ENTRYPOINT ["/bin/bash"]
