#UPDATE COMPONENT
import os
import urllib.request as request
import zipfile
from pathlib import Path
from Text_summarizer.logging import logger
from Text_summarizer.entity import (DataIngestionConfig)
from Text_summarizer.utilities.common import read_yaml, create_directories, get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} download! with following info: \n{headers}")
                if headers.get_content_type() != 'application/zip':
                    logger.error("Downloaded file is not a zip file")
                    raise ValueError("Downloaded file is not a zip file")
            except Exception as e:
                logger.error(f"Failed to download the file from {self.config.source_URL}. Error: {e}")
                raise e
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted files to {unzip_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"File is not a zip file. Error: {e}")
            raise e
        except Exception as e:
            logger.error(f"An error occurred while extracting the zip file. Error: {e}")
            raise e
