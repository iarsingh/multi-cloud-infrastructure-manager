from fastapi.testclient import TestClient
from mcinfra.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'cloud': 'gcp', 'action': 'plan'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'cloud': 'gcp', 'action': 'apply'}).json()
    assert bad["passed"] is False
    assert "action" in bad["failed"]
