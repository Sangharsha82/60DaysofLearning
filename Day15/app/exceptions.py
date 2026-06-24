class AppError(Exception):
    """Base application error."""

    status_code = 500
    message = "An unexpected error occurred."

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        data = dict(self.payload or {})
        data["error"] = self.message
        data["status_code"] = self.status_code
        return data


class BadRequestError(AppError):
    status_code = 400
    message = "Bad request. Please check your input."


class UnauthorizedError(AppError):
    status_code = 401
    message = "Unauthorized. Please log in."


class ForbiddenError(AppError):
    status_code = 403
    message = "Forbidden. You don't have permission."


class NotFoundError(AppError):
    status_code = 404
    message = "The requested resource was not found."


class ValidationError(AppError):
    status_code = 422
    message = "Validation failed."


class RateLimitError(AppError):
    status_code = 429
    message = "Too many requests. Please slow down."


class ServiceUnavailableError(AppError):
    status_code = 503
    message = "Service temporarily unavailable."
