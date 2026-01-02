from fastapi import FastAPI
from app.routes.avaliacao import router as avaliacao_router
from app.database.database import engine
from app.database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Psicossociais - NR01")

app.include_router(avaliacao_router)
