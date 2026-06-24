from flask import render_template, request, jsonify
from app.exceptions import AppError
import logging

logger = logging.getLogger(__name__)


def wants_json(req):
    """Check if the client prefers a JSON response."""
    best = req.accept_mimetypes.best_match(["application/json", "text/html"])
    return best == "application/json"


def register_error_handlers(app):
    """Register all error handlers on the Flask app."""

    # ── Custom AppError (and subclasses) ──────────────────────────────────
    @app.errorhandler(AppError)
    def handle_app_error(error):
        logger.warning(
            "AppError %s: %s", error.status_code, error.message, exc_info=True
        )
        if wants_json(request):
            return jsonify(error.to_dict()), error.status_code
        return (
            render_template(
                "error.html",
                status_code=error.status_code,
                message=error.message,
                title=f"{error.status_code} Error",
            ),
            error.status_code,
        )

    # ── 400 Bad Request ───────────────────────────────────────────────────
    @app.errorhandler(400)
    def bad_request(e):
        logger.warning("400 Bad Request: %s", request.url)
        if wants_json(request):
            return jsonify(error="Bad request", status_code=400), 400
        return render_template(
            "error.html",
            status_code=400,
            message="Your request could not be understood. Please check what you sent and try again.",
            title="400 — Bad Request",
        ), 400

    # ── 401 Unauthorized ─────────────────────────────────────────────────
    @app.errorhandler(401)
    def unauthorized(e):
        logger.warning("401 Unauthorized: %s", request.url)
        if wants_json(request):
            return jsonify(error="Unauthorized", status_code=401), 401
        return render_template(
            "error.html",
            status_code=401,
            message="You need to be logged in to access this page.",
            title="401 — Unauthorized",
        ), 401

    # ── 403 Forbidden ────────────────────────────────────────────────────
    @app.errorhandler(403)
    def forbidden(e):
        logger.warning("403 Forbidden: %s", request.url)
        if wants_json(request):
            return jsonify(error="Forbidden", status_code=403), 403
        return render_template(
            "error.html",
            status_code=403,
            message="You don't have permission to view this resource.",
            title="403 — Forbidden",
        ), 403

    # ── 404 Not Found ────────────────────────────────────────────────────
    @app.errorhandler(404)
    def not_found(e):
        logger.info("404 Not Found: %s", request.url)
        if wants_json(request):
            return jsonify(error="Not found", status_code=404), 404
        return render_template(
            "error.html",
            status_code=404,
            message="We couldn't find the page you were looking for.",
            title="404 — Not Found",
        ), 404

    # ── 405 Method Not Allowed ───────────────────────────────────────────
    @app.errorhandler(405)
    def method_not_allowed(e):
        logger.warning("405 Method Not Allowed: %s %s", request.method, request.url)
        if wants_json(request):
            return jsonify(error="Method not allowed", status_code=405), 405
        return render_template(
            "error.html",
            status_code=405,
            message=f"The {request.method} method is not allowed for this endpoint.",
            title="405 — Method Not Allowed",
        ), 405

    # ── 429 Too Many Requests ────────────────────────────────────────────
    @app.errorhandler(429)
    def too_many_requests(e):
        logger.warning("429 Too Many Requests: %s", request.remote_addr)
        if wants_json(request):
            return jsonify(error="Rate limit exceeded", status_code=429), 429
        return render_template(
            "error.html",
            status_code=429,
            message="You've made too many requests. Please wait a moment and try again.",
            title="429 — Too Many Requests",
        ), 429

    # ── 500 Internal Server Error ─────────────────────────────────────────
    @app.errorhandler(500)
    def internal_server_error(e):
        logger.error("500 Internal Server Error: %s", request.url, exc_info=True)
        if wants_json(request):
            return jsonify(error="Internal server error", status_code=500), 500
        return render_template(
            "error.html",
            status_code=500,
            message="Something went wrong on our end. We've been notified and are looking into it.",
            title="500 — Server Error",
        ), 500

    # ── 503 Service Unavailable ───────────────────────────────────────────
    @app.errorhandler(503)
    def service_unavailable(e):
        logger.error("503 Service Unavailable: %s", request.url)
        if wants_json(request):
            return jsonify(error="Service unavailable", status_code=503), 503
        return render_template(
            "error.html",
            status_code=503,
            message="The service is temporarily unavailable. Please try again shortly.",
            title="503 — Service Unavailable",
        ), 503
