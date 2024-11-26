#!/bin/bash

if [ "$RUN_MODE" = "ec2" ]; then
    echo "Starting in EC2 mode..."
    python main.py
elif [ "$RUN_MODE" = "lamda-local" ]; then
    echo "Starting in Lambda mode with handler: $@"
    exec /usr/local/bin/aws-lambda-rie python -m awslambdaric "$@"
else
    echo "Starting in Lambda mode with handler: $@"
    exec python -m awslambdaric "$@"
fi