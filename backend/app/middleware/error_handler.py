"""Error Handler Middleware"""

import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

logger = logging.getLogger(__name__)


class APIError(Exception):
    """Base API Error"""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ValidationError(APIError):
    def __init__(self, message: str):
        super().__init__(message, 422)


class AuthenticationError(APIError):
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, 401)


class AuthorizationError(APIError):
    def __init__(self, message: str = "Not authorized"):
        super().__init__(message, 403)


class NotFoundError(APIError):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)


class ConflictError(APIError):
    def __init__(self, message: str = "Resource already exists"):
        super().__init__(message, 409)


class InternalServerError(APIError):
    def __init__(self, message: str = "Internal server error"):
        super().__init__(message, 500)


async def error_handler_middleware(request: Request, call_next):
    """Global error handler middleware"""
    try:
        response = await call_next(request)
        return response
    except APIError as e:
        logger.error(f"API Error: {e.message}", exc_info=True)
        return JSONResponse(
            status_code=e.status_code,
            content={"status": "error", "message": e.message},
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Internal server error",
            },
        )
