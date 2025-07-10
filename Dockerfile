FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/reports

CMD ["pytest", "Pytest/concepts/tests/first_test.py", "--html=reports/report-$(date +%Y%m%d%H%M%S).html", "--self-contained-html"]
