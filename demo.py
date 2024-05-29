from hate.logger import logging
from hate.exception import CustomException
import sys
from hate.configuration.s3_syncer import S3Operation

if __name__ == "__main__":
    try:
        logging.info("Starting the S3 file download operation")
        obj = S3Operation()
        obj.sync_folder_from_s3(bucket_name="hate-speech2024", bucket_folder_name="dataset.zip", folder="download")
        logging.info("S3 file download operation completed successfully")
    except CustomException as ce:
        logging.error(f"An error occurred: {ce}")


