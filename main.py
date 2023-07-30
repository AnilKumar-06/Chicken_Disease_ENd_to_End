from src.ChickenDisease import logger
from src.ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ChickenDisease.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline
from src.ChickenDisease.pipeline.stage_03_training import ModelTrainingPipeline


STAGE_NAME = 'Data Ingestion stage'


try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = 'prepare base model'
    
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    training_pipeline = PrepareBaseModelTrainingPipeline()
    training_pipeline.main()
    logger.info(f">>>>>> {STAGE_NAME} finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = "Training"
try: 
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e