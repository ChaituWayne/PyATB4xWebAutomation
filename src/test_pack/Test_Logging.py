# # Logging
# info
# warn
# error
# fatal

import logging


def sample_test(self):
        logger = logging.getLogger()
        logger.info("Information")
        logger.warning("Warning")
        logger.error("Error")
        logger.debug("Debug")
