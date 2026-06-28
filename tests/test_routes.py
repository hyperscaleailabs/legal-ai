from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_landing_page():
    r = client.get("/")
    assert r.status_code == 200
    assert "LegalAI" in r.text


def test_dashboard_all():
    r = client.get("/dashboard")
    assert r.status_code == 200
    assert "Contract Inbox" in r.text


def test_dashboard_filter_high_risk():
    r = client.get("/dashboard?filter=high-risk")
    assert r.status_code == 200
    assert r.status_code == 200


def test_dashboard_filter_pending():
    r = client.get("/dashboard?filter=pending")
    assert r.status_code == 200


def test_dashboard_filter_approved():
    r = client.get("/dashboard?filter=approved")
    assert r.status_code == 200


def test_upload_form():
    r = client.get("/contracts/upload")
    assert r.status_code == 200
    assert "Upload" in r.text


def test_upload_post_redirects():
    r = client.post("/contracts/upload", data={}, follow_redirects=False)
    assert r.status_code == 303
    assert r.headers["location"].startswith("/contracts/1")


def test_contract_review_known():
    for contract_id in ["1", "2", "3", "4", "5"]:
        r = client.get(f"/contracts/{contract_id}")
        assert r.status_code == 200, f"contract {contract_id} failed"


def test_contract_review_unknown():
    r = client.get("/contracts/999")
    assert r.status_code == 404


def test_contract_review_just_uploaded_banner():
    r = client.get("/contracts/1?just_uploaded=1")
    assert r.status_code == 200
    assert "AI review complete" in r.text


def test_risk_assessment_known():
    for contract_id in ["1", "2", "3", "4", "5"]:
        r = client.get(f"/contracts/{contract_id}/risk")
        assert r.status_code == 200, f"risk for contract {contract_id} failed"


def test_risk_assessment_unknown():
    r = client.get("/contracts/999/risk")
    assert r.status_code == 404


def test_escalate_contract():
    r = client.post(
        "/contracts/1/escalate",
        data={"reviewer_id": "r1", "notes": "Urgent review needed", "priority": "high"},
    )
    assert r.status_code == 200
    assert "Escalated" in r.text
    assert "Maya Chen" in r.text
