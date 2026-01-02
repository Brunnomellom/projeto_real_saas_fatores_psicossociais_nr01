from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.avaliacao import router as avaliacao_router
from app.database.database import engine
from app.database import models

# Cria as tabelas no banco
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Psicossociais - NR-01")

# Libera acesso do frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(avaliacao_router)
