import os
from firebase_functions import https_fn
from google.cloud import storage

@https_fn.on_request()
def upload_file(req: https_fn.Request) -> https_fn.Response:
    """HTTP Cloud Function that uploads a file to Cloud Storage."""
    if req.method != "POST":
        return https_fn.Response("Only POST method is allowed", status=405)
    
    try:
        data = req.get_json()
        filename = data.get("filename")
        content = data.get("content")
        
        if not filename or not content:
            return https_fn.Response(
                "Missing 'filename' or 'content' in request body", 
                status=400
            )
        
        bucket_name = os.getenv("STORAGE_BUCKET", "demo-bucket")
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(filename)
        blob.upload_from_string(content)
        
        return https_fn.Response(
            f"File '{filename}' uploaded to '{bucket_name}'",
            status=200
        )
    except Exception as e:
        return https_fn.Response(f"Error: {str(e)}", status=500)
