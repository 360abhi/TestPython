FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/reports

CMD ["pytest", "Pytest/concepts/first_test.py", "--html=reports/report.html", "--self-contained-html"]
