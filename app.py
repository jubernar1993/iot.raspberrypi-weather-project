######1.Python Code to Fetch the Certificate from Secrets Manager: Use boto3 in your Python application to retrieve the certificate from AWS Secrets Manager when the container starts.
############################################################


import boto3
import json
import os

def fetch_iot_certificate(secret_name):
    """Fetch the certificate from AWS Secrets Manager"""
    # Initialize the AWS SDK client for Secrets Manager
    client = boto3.client('secretsmanager', region_name='us-east-1')

    try:
        # Retrieve the secret value
        response = client.get_secret_value(SecretId=secret_name)

        # Secrets can be in string or binary format
        secret = response.get('SecretString', None)

        if secret is None:
            print("Secret not found!")
            exit(1)

        # Parse the secret JSON to get the certificate and key
        secret_json = json.loads(secret)
        certificate = secret_json['cert']
        private_key = secret_json['key']

        # Optionally save it to files or use directly
        with open("/app/iot_cert.pem", "w") as cert_file:
            cert_file.write(certificate)

        with open("/app/iot_key.pem", "w") as key_file:
            key_file.write(private_key)

        print("Certificate and private key successfully fetched!")

    except Exception as e:
        print(f"Error fetching secret: {e}")
        exit(1)

# Define the secret name you stored in AWS Secrets Manager
secret_name = "your-secret-name"

# Fetch certificate and key
fetch_iot_certificate(secret_name)

# Now, proceed with your application logic, e.g., connecting to AWS IoT
