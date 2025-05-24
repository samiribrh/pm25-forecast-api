import secrets

from fastapi import Header, HTTPException

from backend.app.core.config import settings
from backend.app.core.logger import logger


def verify_api_key(x_api_key: str = Header(...)):
    if not settings.API_KEY or not secrets.compare_digest(x_api_key, settings.API_KEY):
        logger.warning("Unauthorized access attempt")
        raise HTTPException(status_code=401, detail="Unauthorized")
    logger.info("API key verified successfully")
