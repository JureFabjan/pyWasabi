import boto3
import botocore
import sys
import os
from pathlib import Path

"""def folder_upload(folder_path, bucket, root):
    for subobject in os.listdir(folder_path):
        subobject_path = Path(folder_path) / subobject
        if os.path.isdir(subobject_path):
            folder_upload(str(subobject_path.absolute()), bucket, root)
        else:
            bucket.upload_file(str(subobject_path.absolute()), str((Path(root).name / subobject_path.relative_to(root)).absolute()))
"""

if __name__ == "__main__":
    root_path, bucket_name, *_ = sys.argv[1:]
    s3 = boto3.resource("s3",
                        endpoint_url="https://s3.eu-west-2.wasabisys.com")
    bucket = s3.Bucket(bucket_name)

    # root_path = str(Path(root_path).absolute())
    # folder_upload(root_path, bucket, root_path)

    already_uploaded = [x.key for x in bucket.objects.all()]

    unaploadable = []

    for subdir, dirs, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(subdir, file)
            upload_path = full_path[len(root_path)+1:]
            if upload_path not in already_uploaded:
                try:
                    with open(full_path, 'rb') as data:
                        bucket.put_object(Key=upload_path, Body=data)
                    print(f"Uploaded: {full_path}")
                except botocore.exceptions.ClientError as e:
                    unaploadable.append(full_path)
    print("--------------------------------------------")
    print("Could not upload:")
    print("\n".join(unaploadable))