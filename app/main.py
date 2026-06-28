from fastapi import FastAPI
from app.routes import landing, dashboard, contracts, risk

app = FastAPI(title="LegalAI", description="AI general counsel for SMBs")

app.include_router(landing.router)
app.include_router(dashboard.router)
app.include_router(contracts.router)
app.include_router(risk.router)
