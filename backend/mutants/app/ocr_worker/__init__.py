"""
PropertyGuard OCR Worker Subpackage
-----------------------------------
Contains the standalone Celery application and background worker tasks dedicated
to running resource-intensive PaddleOCR extraction jobs asynchronously.
"""


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
