import pytest


@pytest.mark.asyncio
async def test_create_application_returns_201(client):
    response = await client.post(
        "/api/v1/applications/",
        json={
            "company": "Acme Corp",
            "role": "Backend Engineer",
            "status": "applied",
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["company"] == "Acme Corp"
    assert body["role"] == "Backend Engineer"
    assert body["status"] == "applied"
    assert "id" in body
