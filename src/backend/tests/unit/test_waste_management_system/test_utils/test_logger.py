from src.waste_management_system.utils.logger import logger


def test_logger():
    logger.debug("Test message")
    logger.info("Test message")
    logger.warning("Test message")
    logger.error("Test message")
    logger.critical("Test message")
