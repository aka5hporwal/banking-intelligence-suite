from intelligentBanking import logger
from intelligentBanking.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# This script is the entry point for the Intelligent Banking project.
if __name__ == "__main__":
    try:
        logger.info("Starting the Intelligent Banking pipeline...")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info("Intelligent Banking pipeline completed successfully.")
    except Exception as e:
        logger.exception("An error occurred in the Intelligent Banking pipeline.")
        raise e



