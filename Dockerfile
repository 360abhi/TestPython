FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y chromium chromium-driver wget unzip && \
    apt-get clean

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN playwright install

CMD ["python", "Playwright/jobs/test_job.py"]
