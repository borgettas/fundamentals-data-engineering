import logging

def setup_logging() -> logging:
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler()],
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    return logging.getLogger(__name__)
