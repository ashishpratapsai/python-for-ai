import logging
logging.basicConfig(
    level=logging.WARNING,
    format ="%(asctime)s - %(levelname)s - %(message)s" 
)

logger =logging.getLogger(__name__)

logger.debug("Debug message - very detailed")
logger.info("Application Started")
logger.warning("Something unexpecter happened")
logger.error("Something failed")
logger.critical("System is broken")