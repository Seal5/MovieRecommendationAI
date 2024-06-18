import boto3
import joblib

def save_model_to_s3(model, bucket_name, model_path):
    "aws upload"
    s3 = boto3.client('s3')
    local_model_path = 'model.pkl'
    joblib.dump(model, local_model_path)
    s3.upload_file(local_model_path, bucket_name, model_path)
    print(f"Model saved to S3 bucket {bucket_name} at {model_path}")