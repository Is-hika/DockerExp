FROM ubuntu:20.04

# Update package lists and install Python 3.9 and related tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3.9-venv \
    python3.9-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the default command to run when the container starts
CMD ["python3.9"]