from http import HTTPStatus

from flask import Blueprint, jsonify, request

from app.services.task_store import task_store

tasks_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")


@tasks_bp.get("")
def list_tasks():
    tasks = task_store.list_tasks()
    return jsonify(tasks), HTTPStatus.OK


@tasks_bp.get("/<int:task_id>")
def get_task(task_id: int):
    task = task_store.get_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), HTTPStatus.NOT_FOUND
    return jsonify(task), HTTPStatus.OK


@tasks_bp.post("")
def create_task():
    payload = request.get_json(silent=True) or {}
    title = payload.get("title", "").strip()

    if not title:
        return jsonify({"error": "'title' is required"}), HTTPStatus.BAD_REQUEST

    task = task_store.create_task(title=title)
    return jsonify(task), HTTPStatus.CREATED


@tasks_bp.put("/<int:task_id>")
def update_task(task_id: int):
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    completed = payload.get("completed")

    if title is not None and not str(title).strip():
        return jsonify({"error": "'title' cannot be empty"}), HTTPStatus.BAD_REQUEST

    if completed is not None and not isinstance(completed, bool):
        return jsonify({"error": "'completed' must be true or false"}), HTTPStatus.BAD_REQUEST

    task = task_store.update_task(
        task_id=task_id,
        title=str(title).strip() if title is not None else None,
        completed=completed,
    )

    if task is None:
        return jsonify({"error": "Task not found"}), HTTPStatus.NOT_FOUND

    return jsonify(task), HTTPStatus.OK


@tasks_bp.delete("/<int:task_id>")
def delete_task(task_id: int):
    deleted = task_store.delete_task(task_id)
    if not deleted:
        return jsonify({"error": "Task not found"}), HTTPStatus.NOT_FOUND

    return "", HTTPStatus.NO_CONTENT
