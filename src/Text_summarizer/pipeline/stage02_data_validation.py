from Text_summarizer.config.configuration import ConfigurationManager
from Text_summarizer.components.data_validation import DataValidtion
from Text_summarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidtion(config=data_validation_config)
        data_validation.validate_all_files_exist()