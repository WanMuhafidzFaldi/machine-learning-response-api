# Gunakan image Python sebagai base image
FROM python:3.13

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Buat direktori kerja di dalam container
WORKDIR /app

# Salin file Pipfile dan Pipfile.lock ke dalam container
COPY Pipfile Pipfile.lock /app/

# Install pipenv dan dependencies dari Pipfile dengan timeout yang lebih tinggi
RUN pip install pipenv --default-timeout=100 && pipenv install --deploy --ignore-pipfile --default-timeout=100

# Salin seluruh source code ke dalam container
COPY . /app/

# Set environment variable untuk Flask
ENV FLASK_APP=main.py

# Expose port 5000
EXPOSE 5000

# Jalankan aplikasi
CMD ["pipenv", "run", "python", "main.py"]