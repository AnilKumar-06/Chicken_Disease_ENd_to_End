from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDisease.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = 'prepare base model'
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        training_pipeline = PrepareBaseModelTrainingPipeline()
        training_pipeline.main()
        logger.info(f">>>>>> {STAGE_NAME} finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e