from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import blog, contracts, dashboard, landing, risk

app = FastAPI(title="LegalAI", description="AI general counsel for SMBs")

app.mount("/static", StaticFiles(directory="public"), name="static")

app.include_router(landing.router)
app.include_router(dashboard.router)
app.include_router(contracts.router)
app.include_router(risk.router)
app.include_router(blog.router)
