from intelligentBanking import logger
from intelligentBanking.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from intelligentBanking.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


# This script is the entry point for the Intelligent Banking project.
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_pipeline = PrepareBaseModelTrainingPipeline()
    prepare_pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e




