# aws_utils.py
import os
from datetime import datetime

import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


def upload_text_to_s3(key: str, text: str) -> bool:
    """
    Uploads a text string as a file to S3.
    key example: 'resume-logs/analysis_20251125_120045.txt'
    """
    try:
        s3_client.put_object(
            Bucket=AWS_S3_BUCKET_NAME,
            Key=key,
            Body=text.encode("utf-8"),
        )
        return True
    except Exception as e:
        print(f"[S3 ERROR] {e}")
        return False


def generate_resume_log_key(prefix: str = "resume-logs") -> str:
    """
    Generate a unique S3 key based on current timestamp.
    """
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}/analysis_{ts}.txt"
