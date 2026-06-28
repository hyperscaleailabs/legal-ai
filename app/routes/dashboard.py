from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.data.mock_contracts import CONTRACTS

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

RISK_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, filter: str = Query(default="all")):
    contracts = list(CONTRACTS.values())

    if filter == "high-risk":
        contracts = [c for c in contracts if c["risk_level"] in ("Critical", "High")]
    elif filter == "pending":
        contracts = [c for c in contracts if c["status"] == "Pending Review"]
    elif filter == "approved":
        contracts = [c for c in contracts if c["status"] == "Approved"]

    contracts.sort(key=lambda c: RISK_ORDER.get(c["risk_level"], 99))

    all_contracts = list(CONTRACTS.values())
    stats = {
        "total": len(all_contracts),
        "high_risk": sum(
            1 for c in all_contracts if c["risk_level"] in ("Critical", "High")
        ),
        "pending": sum(1 for c in all_contracts if c["status"] == "Pending Review"),
        "approved": sum(1 for c in all_contracts if c["status"] == "Approved"),
    }

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {"contracts": contracts, "stats": stats, "active_filter": filter},
    )
