from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import main_routes
from services.url_service import init_client, close_client
from contextlib import asynccontextmanager

# ===== Client - Lifespan (substitui o on_event startup/shutdown) =====
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await init_client()
    yield
    # shutdown
    await close_client()

# ===== Cria app com lifespan =====
app = FastAPI(lifespan=lifespan)

# ===== Monta - Static / Templates =====
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ===== Rotas =====
app.include_router(main_routes.router)

