from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.data.mock_contracts import CONTRACTS

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))


@router.get("/contracts/upload", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse(request, "contract_upload.html")


@router.post("/contracts/upload")
async def upload_contract(request: Request):
    # In the prototype, uploading always lands on contract #1 (Acme NDA)
    # with a "just_uploaded" flag so the UI can show a success message
    return RedirectResponse(url="/contracts/1?just_uploaded=1", status_code=303)


@router.get("/contracts/{contract_id}", response_class=HTMLResponse)
async def contract_review(request: Request, contract_id: str, just_uploaded: int = 0):
    contract = CONTRACTS.get(contract_id)
    if not contract:
        return HTMLResponse(content="Contract not found", status_code=404)
    return templates.TemplateResponse(
        request,
        "contract_review.html",
        {"contract": contract, "just_uploaded": bool(just_uploaded)},
    )
