from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.data.mock_contracts import CONTRACTS, REVIEWERS
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))


@router.get("/contracts/{contract_id}/risk", response_class=HTMLResponse)
async def risk_assessment(request: Request, contract_id: str):
    contract = CONTRACTS.get(contract_id)
    if not contract:
        return HTMLResponse(content="Contract not found", status_code=404)
    return templates.TemplateResponse(
        request,
        "risk_assessment.html",
        {"contract": contract, "reviewers": REVIEWERS},
    )


@router.post("/contracts/{contract_id}/escalate", response_class=HTMLResponse)
async def escalate_contract(
    request: Request,
    contract_id: str,
    reviewer_id: str = Form(...),
    notes: str = Form(default=""),
    priority: str = Form(default="normal"),
):
    contract = CONTRACTS.get(contract_id)
    if not contract:
        return HTMLResponse(content="Contract not found", status_code=404)

    reviewer = next((r for r in REVIEWERS if r["id"] == reviewer_id), REVIEWERS[0])

    # Mutate mock state
    contract["status"] = "Escalated"
    contract["audit_trail"].append(
        {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "action": "Escalated",
            "actor": "you@company.com",
            "detail": f"Escalated to {reviewer['name']} ({reviewer['title']}) · Priority: {priority}"
            + (f" · Notes: {notes}" if notes else ""),
        }
    )

    # Return HTMX partial: updated status badge + out-of-band audit trail entry
    new_audit_entry = contract["audit_trail"][-1]
    return templates.TemplateResponse(
        request,
        "partials/escalation_result.html",
        {"contract": contract, "reviewer": reviewer, "audit_entry": new_audit_entry},
    )
