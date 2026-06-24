from flask import Blueprint, render_template, abort, jsonify, request
from .exceptions import (
    BadRequestError,
    NotFoundError,
    ValidationError,
    ForbiddenError,
    UnauthorizedError,
    RateLimitError,
    ServiceUnavailableError,
)

main_bp = Blueprint("main", __name__)


# ── Home ─────────────────────────────────────────────────────────────────────
@main_bp.route("/")
def index():
    return render_template("index.html")


# ── Demo routes that trigger specific errors ──────────────────────────────────
@main_bp.route("/demo/400")
def demo_400():
    raise BadRequestError("You sent something we couldn't parse.")


@main_bp.route("/demo/401")
def demo_401():
    raise UnauthorizedError()


@main_bp.route("/demo/403")
def demo_403():
    raise ForbiddenError("You don't have the role required to view this.")


@main_bp.route("/demo/404")
def demo_404():
    raise NotFoundError("That item doesn't exist in our database.")


@main_bp.route("/demo/422")
def demo_422():
    raise ValidationError("The 'email' field must be a valid email address.")


@main_bp.route("/demo/429")
def demo_429():
    raise RateLimitError()


@main_bp.route("/demo/500")
def demo_500():
    # Intentional unhandled exception — caught by the 500 handler
    raise RuntimeError("Simulated internal server error.")


@main_bp.route("/demo/503")
def demo_503():
    raise ServiceUnavailableError()


# ── Flask's built-in abort() demo ────────────────────────────────────────────
@main_bp.route("/demo/abort/<int:code>")
def demo_abort(code):
    abort(code)


# ── JSON demo (Accept: application/json) ─────────────────────────────────────
@main_bp.route("/api/demo/404")
def api_demo_404():
    raise NotFoundError("Resource with id=42 not found.")
