from fastapi import FastAPI
from app.routes import blog, contracts, dashboard, landing, risk

app = FastAPI(title="LegalAI", description="AI general counsel for SMBs")

app.include_router(landing.router)
app.include_router(dashboard.router)
app.include_router(contracts.router)
app.include_router(risk.router)
app.include_router(blog.router)
