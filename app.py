from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import main_routes

app = FastAPI()

# ===== Monta - Static / Templates =====
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ===== Rotas =====
app.include_router(main_routes.router)
