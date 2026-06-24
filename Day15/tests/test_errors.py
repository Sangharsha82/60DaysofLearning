import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app("testing")
    app.config["PROPAGATE_EXCEPTIONS"] = False
    with app.test_client() as c:
        yield c


# ── HTML responses ────────────────────────────────────────────────────────────

def test_index(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"ErrorLab" in r.data


def test_404_html(client):
    r = client.get("/no-such-page")
    assert r.status_code == 404
    assert b"404" in r.data


def test_demo_400(client):
    r = client.get("/demo/400")
    assert r.status_code == 400
    assert b"400" in r.data


def test_demo_401(client):
    r = client.get("/demo/401")
    assert r.status_code == 401


def test_demo_403(client):
    r = client.get("/demo/403")
    assert r.status_code == 403


def test_demo_404(client):
    r = client.get("/demo/404")
    assert r.status_code == 404


def test_demo_422(client):
    r = client.get("/demo/422")
    assert r.status_code == 422


def test_demo_429(client):
    r = client.get("/demo/429")
    assert r.status_code == 429


def test_demo_500(client):
    r = client.get("/demo/500")
    assert r.status_code == 500


def test_demo_503(client):
    r = client.get("/demo/503")
    assert r.status_code == 503


# ── JSON responses ────────────────────────────────────────────────────────────

def test_api_404_returns_json(client):
    r = client.get("/api/demo/404", headers={"Accept": "application/json"})
    assert r.status_code == 404
    data = r.get_json()
    assert data["status_code"] == 404
    assert "error" in data


def test_demo_400_json(client):
    r = client.get("/demo/400", headers={"Accept": "application/json"})
    assert r.status_code == 400
    assert r.get_json()["status_code"] == 400
