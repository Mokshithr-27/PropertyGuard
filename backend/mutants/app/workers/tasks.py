"""
PropertyGuard General Worker Tasks
----------------------------------
Contains baseline asynchronous health check tasks for verifying Celery worker
liveness and task queue processing.
"""

from app.workers.celery_app import celery_app


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@celery_app.task
def health_check_task() -> str:
    return "PropertyGuard worker is alive"