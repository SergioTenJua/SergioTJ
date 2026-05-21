import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_store


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(activities_store)
    yield
    activities_store.clear()
    activities_store.update(copy.deepcopy(original_activities))


@pytest.fixture
def client():
    return TestClient(app)
