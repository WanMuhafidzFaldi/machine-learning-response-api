# Use AWS Lambda Python 3.9 base image
FROM public.ecr.aws/lambda/python:3.13

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /var/task

# Copy dependencies file
COPY requirements.txt ./

# Install dependencies directly with pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .
COPY start.sh /var/task/start.sh
RUN chmod +x /var/task/start.sh

# Expose port for EC2
EXPOSE 5000

# Add AWS Lambda Runtime Interface Emulator
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/local/bin/aws-lambda-rie
RUN chmod +x /usr/local/bin/aws-lambda-rie

# Add an environment variable to control the mode
ENV RUN_MODE=lambda

# Use the startup script as the entrypoint
ENTRYPOINT ["/var/task/start.sh"]

# Specify the handler directly for Lambda runtime
CMD ["main.lambda_handler"]
