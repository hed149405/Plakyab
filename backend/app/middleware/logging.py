"""Logging Configuration"""

import logging
import logging.handlers
from pathlib import Path

from app.config import settings


def setup_logging() -> logging.Logger:
    """Setup logging configuration"""
    # Create logs directory
    logs_dir = Path(settings.LOG_FILE).parent
    logs_dir.mkdir(parents=True, exist_ok=True)

    # Root logger
    logger = logging.getLogger("app")
    logger.setLevel(settings.LOG_LEVEL)

    # Formatter
    formatter = logging.Formatter(
        settings.LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        settings.LOG_FILE,
        maxBytes=settings.LOG_MAX_BYTES,
        backupCount=settings.LOG_BACKUP_COUNT,
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
