import pytest

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(currentdir)
sys.path.append(parentdir)

from app import app


@pytest.fixture(scope='module')
def lunch_app():
    with app.test_client() as client:
        yield client
