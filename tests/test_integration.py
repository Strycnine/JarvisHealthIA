import pytest


@pytest.mark.parametrize(
    "route, status",
    [
        ("/", 200),
        ("/result", 200),
        ("/poisson", 404),
    ])
def test_homepage(lunch_app, route, status):
    response = lunch_app.get(route)
    assert response.status_code == status
