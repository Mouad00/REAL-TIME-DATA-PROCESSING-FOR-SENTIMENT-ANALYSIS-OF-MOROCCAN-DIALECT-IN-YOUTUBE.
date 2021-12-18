import boto3
import json


currencies = ['USD', 'GBP', 'EUR']

class Transaction:
    username: str = "test1"
    currency: str = "test1"
    amount: str = "test1"

    def serialize(self):
        return dict(
            {
                "username": self.username,
                "currency": self.currency,
                "amount": self.amount
            }
        )
    
    
print(Transaction().serialize())



def Producer(file_string,bucket_name):
    s3_resource = boto3.resource('s3') 
    filename = file_string
    with open(filename, 'a') as file:
        json.dump(Transaction().serialize(), file)
        file.write(",\n")
    s3_resource.Bucket(bucket_name).upload_file(Filename=filename, Key=filename)

def mount_s3_bucket(access_key, secret_key, bucket_name, mount_folder):
    ACCESS_KEY_ID = access_key
    SECRET_ACCESS_KEY = secret_key
    ENCODED_SECRET_KEY = SECRET_ACCESS_KEY.replace("/", "%2F")
    print ("Mounting", bucket_name)
    dbutils.fs.unmount("/mnt/%s" % mount_folder)
    dbutils.fs.mount("s3a://%s:%s@%s" % (ACCESS_KEY_ID, ENCODED_SECRET_KEY, bucket_name), "/mnt/%s" % mount_folder) 
    print ("The bucket", bucket_name, "was mounted to", mount_folder, "\n")
    
ACCESS_KEY = "AKIAQXJ7PEDM7ZBJALF2"
SECRET_ACCESS_KEY = "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"

mount_s3_bucket(ACCESS_KEY, SECRET_ACCESS_KEY, "spark-bucket-big-data", "/s3Data")