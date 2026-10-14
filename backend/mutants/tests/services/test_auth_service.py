"""
PropertyGuard Auth Service Unit Test Suite
------------------------------------------
Validates user registration workflows, builder profile initialization with PENDING status,
and duplicate account checks.
"""

from types import SimpleNamespace

from app.models.builder import BuilderProfile
from app.models.role import Role
from app.services.auth_service import register_user


class FakeDB:
    def __init__(self):
        self.scalar_calls = 0
        self.added = []
        self.committed = False
        self.refreshed = False

    def scalar(self, statement):
        self.scalar_calls += 1
        if self.scalar_calls == 1:
            return None  # no existing user
        if self.scalar_calls == 2:
            return SimpleNamespace(id="buyer-role-id", name="BUYER")
        if self.scalar_calls == 3:
            return SimpleNamespace(id="builder-role-id", name="BUILDER")
        return None

    def add(self, obj):
        self.added.append(obj)

    def flush(self):
        return None

    def commit(self):
        self.committed = True

    def refresh(self, obj):
        self.refreshed = True


def test_builder_registration_starts_pending_verification():
    db = FakeDB()

    user = register_user(
        db=db,
        email="builder@example.com",
        password="StrongPassword123!",
        full_name="Example Builder",
        role="BUILDER",
    )

    profiles = [obj for obj in db.added if isinstance(obj, BuilderProfile)]

    assert len(profiles) == 1
    assert profiles[0].verification_status == "PENDING"
    assert db.committed is True
    assert db.refreshed is True
    assert user.email == "builder@example.com"
