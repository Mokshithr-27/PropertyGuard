import uuid
from types import SimpleNamespace

import pytest

from app.services.project_service import add_unit


def make_project(
    *,
    builder_id,
):
    return SimpleNamespace(
        id=uuid.uuid4(),
        builder_id=builder_id,
    )


def make_version(
    *,
    project_id,
    status="DRAFT",
):
    return SimpleNamespace(
        id=uuid.uuid4(),
        project_id=project_id,
        status=status,
    )


def make_building(
    *,
    version_id,
):
    return SimpleNamespace(
        id=uuid.uuid4(),
        project_version_id=version_id,
    )


class FakeDB:
    def __init__(
        self,
        building,
        version,
        project,
    ):
        self.building = building
        self.version = version
        self.project = project

        self.added = None
        self.committed = False
        self.refreshed = False
        self.scalar_calls = 0

    def scalar(self, statement):
        self.scalar_calls += 1

        if self.scalar_calls == 1:
            return self.building

        if self.scalar_calls == 2:
            return self.version

        if self.scalar_calls == 3:
            # Simulate the ownership check performed by:
            #
            # Project.id == version.project_id
            # Project.builder_id == builder_profile_id
            #
            # The fake DB cannot execute the SQL expression itself,
            # so the test controls whether the project is returned.
            return self.project

        return None

    def add(self, obj):
        self.added = obj

    def commit(self):
        self.committed = True

    def refresh(self, obj):
        self.refreshed = True


class OwnershipAwareFakeDB(FakeDB):
    """
    Fake database that can simulate whether the supplied builder
    owns the project.
    """

    def __init__(
        self,
        building,
        version,
        project,
        builder_profile_id,
    ):
        super().__init__(
            building=building,
            version=version,
            project=project,
        )
        self.builder_profile_id = builder_profile_id

    def scalar(self, statement):
        self.scalar_calls += 1

        if self.scalar_calls == 1:
            return self.building

        if self.scalar_calls == 2:
            return self.version

        if self.scalar_calls == 3:
            if (
                self.project is not None
                and self.project.builder_id
                == self.builder_profile_id
            ):
                return self.project

            return None

        return None


def test_add_unit_owner_builder_succeeds():
    builder_id = uuid.uuid4()

    project = make_project(
        builder_id=builder_id,
    )

    version = make_version(
        project_id=project.id,
    )

    building = make_building(
        version_id=version.id,
    )

    db = OwnershipAwareFakeDB(
        building=building,
        version=version,
        project=project,
        builder_profile_id=builder_id,
    )

    unit = add_unit(
        db=db,
        building_id=building.id,
        builder_profile_id=builder_id,
        unit_number="101",
        floor_number=1,
        unit_type="2BHK",
        area_sqft=1200,
    )

    assert unit.building_id == building.id
    assert unit.unit_number == "101"
    assert unit.floor_number == 1
    assert unit.unit_type == "2BHK"
    assert unit.area_sqft == 1200

    assert db.added is unit
    assert db.committed is True
    assert db.refreshed is True


def test_add_unit_different_builder_is_rejected():
    owner_builder_id = uuid.uuid4()
    different_builder_id = uuid.uuid4()

    project = make_project(
        builder_id=owner_builder_id,
    )

    version = make_version(
        project_id=project.id,
    )

    building = make_building(
        version_id=version.id,
    )

    db = OwnershipAwareFakeDB(
        building=building,
        version=version,
        project=project,
        builder_profile_id=different_builder_id,
    )

    with pytest.raises(
        ValueError,
        match="Builder does not own this project",
    ):
        add_unit(
            db=db,
            building_id=building.id,
            builder_profile_id=different_builder_id,
            unit_number="101",
            floor_number=1,
            unit_type="2BHK",
            area_sqft=1200,
        )

    assert db.added is None
    assert db.committed is False


def test_add_unit_non_draft_version_is_rejected():
    builder_id = uuid.uuid4()

    project = make_project(
        builder_id=builder_id,
    )

    version = make_version(
        project_id=project.id,
        status="PENDING_APPROVAL",
    )

    building = make_building(
        version_id=version.id,
    )

    db = OwnershipAwareFakeDB(
        building=building,
        version=version,
        project=project,
        builder_profile_id=builder_id,
    )

    with pytest.raises(
        ValueError,
        match="Units can only be added to a DRAFT version",
    ):
        add_unit(
            db=db,
            building_id=building.id,
            builder_profile_id=builder_id,
            unit_number="101",
            floor_number=1,
            unit_type="2BHK",
            area_sqft=1200,
        )

    assert db.added is None
    assert db.committed is False


def test_add_unit_building_not_found():
    builder_id = uuid.uuid4()

    db = OwnershipAwareFakeDB(
        building=None,
        version=None,
        project=None,
        builder_profile_id=builder_id,
    )

    with pytest.raises(
        ValueError,
        match="Building not found",
    ):
        add_unit(
            db=db,
            building_id=uuid.uuid4(),
            builder_profile_id=builder_id,
            unit_number="101",
            floor_number=1,
            unit_type="2BHK",
            area_sqft=1200,
        )

    assert db.added is None
    assert db.committed is False


def test_add_unit_project_version_not_found():
    builder_id = uuid.uuid4()

    project = make_project(
        builder_id=builder_id,
    )

    building = make_building(
        version_id=uuid.uuid4(),
    )

    db = OwnershipAwareFakeDB(
        building=building,
        version=None,
        project=project,
        builder_profile_id=builder_id,
    )

    with pytest.raises(
        ValueError,
        match="Project version not found",
    ):
        add_unit(
            db=db,
            building_id=building.id,
            builder_profile_id=builder_id,
            unit_number="101",
            floor_number=1,
            unit_type="2BHK",
            area_sqft=1200,
        )

    assert db.added is None
    assert db.committed is False