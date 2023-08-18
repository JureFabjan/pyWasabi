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
    initial_path = Path(".").absolute()
    os.chdir(root_path)
    s3 = boto3.resource("s3",
                        endpoint_url="https://s3.eu-west-2.wasabisys.com")
    bucket = s3.Bucket(bucket_name)

    # root_path = str(Path(root_path).absolute())
    # folder_upload(root_path, bucket, root_path)

    uploaded = [x.key for x in bucket.objects.all()]

    undownloadable = []

    for file in uploaded:
        file = Path(file)
        if not file.parent.exists():
            file.parent.mkdir(parents=True, exist_ok=True)
        try:
            bucket.download_file(str(file), str(file.absolute()))
            print(f"Downloaded: {file}")
        except:
            undownloadable.append(file)

    print("--------------------------------------------")
    print("Could not download:")
    print("\n".join(undownloadable))