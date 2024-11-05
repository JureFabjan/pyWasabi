# pyWasabi
Interface for transfer to and from Wasabi S3 buckets using the command line.

Note:
- the scripts are very bare-bones and they require the setup of Wasabi credentials that can be read by boto3 library.
- the scripts assume that the endpoint bucket is located at eu-west-2; in case you have your buckets elsewhere, you should adjust the corresponding lines in both upload and download scripts.

## Usage

The scripts make a recursive upload/download of the whole path tree that is given. 

### Upload

To upload one should call the 'crawl_upload.py' script with additional parameters:

```
python path_to/crawl_upload.py path_to_files bucket_name
```

Where `path_to_files` is the path to the files that should be uploaded and `bucket_name` is the name of the Wasabi bucket that should be used.

### Download

To download one should call the 'crawl_download.py' script with additional parameters:

```
python crawl_download.py root_folder bucket_name
```

Where `root_folder` is the path to the folder in which the data will be deposited, while `bucket_name` is the name of the Wasabi bucket that should be used.

