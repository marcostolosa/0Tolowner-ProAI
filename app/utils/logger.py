import logging

def setup_logger():
    """Configura o logger da aplicação."""
    logger = logging.getLogger("TolownerProAI")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger