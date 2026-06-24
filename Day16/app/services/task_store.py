from dataclasses import dataclass, asdict


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TaskStore:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def list_tasks(self) -> list[dict]:
        return [asdict(task) for task in self._tasks.values()]

    def get_task(self, task_id: int) -> dict | None:
        task = self._tasks.get(task_id)
        return asdict(task) if task else None

    def create_task(self, title: str) -> dict:
        task = Task(id=self._next_id, title=title)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return asdict(task)

    def update_task(self, task_id: int, title: str | None, completed: bool | None) -> dict | None:
        task = self._tasks.get(task_id)
        if task is None:
            return None

        if title is not None:
            task.title = title

        if completed is not None:
            task.completed = completed

        return asdict(task)

    def delete_task(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True


task_store = TaskStore()
