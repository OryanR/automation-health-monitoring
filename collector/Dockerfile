FROM python:3.9-slim
WORKDIR /app
# We reach 'up' one level to get the same requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY collector/app.py .
EXPOSE 5000
CMD ["python", "app.py"]