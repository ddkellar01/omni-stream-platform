FROM python:3.11-slim

WORKDIR /app

# Install FFmpeg for HLS segmentation and video transformation
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt kafka-python pydantic

COPY . .

CMD ["python", "worker.py"]
