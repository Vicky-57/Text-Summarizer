from Text_summarizer.config.configuration import ConfigurationManager
from Text_summarizer.components.model_trainer import ModelTrainer
from Text_summarizer.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()