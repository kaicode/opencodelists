from pathlib import Path

import pytest
from django.conf import settings
from django.core.management import call_command

from codelists.tests.factories import CodelistFactory


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="function")
def tennis_elbow():
    fixtures_path = Path(settings.BASE_DIR, "coding_systems", "snomedct", "fixtures")
    call_command("loaddata", fixtures_path / "core-model-components.json")
    call_command("loaddata", fixtures_path / "tennis-elbow.json")

    with open(fixtures_path / "disorder-of-elbow.csv") as f:
        yield f.read()


@pytest.fixture(scope="function")
def tennis_elbow_codelist(tennis_elbow):
    return CodelistFactory(csv_data=tennis_elbow)
