import os
import urllib.request as request
import zipfile
from Text_summarizer.logging import logger
from dataclasses import dataclass
from pathlib import Path

from Text_summarizer.constants import *
from Text_summarizer.utilities.common import read_yaml, create_directories, get_size

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        return data_ingestion_config

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

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    logger.error(f"Data ingestion failed. Error: {e}")
    raise e
