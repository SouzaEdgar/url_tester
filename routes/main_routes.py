from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.url_service import process_urls_async

import re

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "resultados": []}
    )

# passando a rota para ajax
@router.post("/verificar", response_class=HTMLResponse) 
async def process_form(
    request: Request,
    url: str = Form(...),
    parameter: str = Form("")
):
    # ===== URLs =====
    urls = []
    for linha in url.splitlines():
        if linha.strip():
            urls.append(linha.strip())
    
    # ===== Parametros =====
    params = []
    for p in re.split(r"[;\n,]+", parameter):
        if p.strip():
            params.append(p.strip())
    
    # ===== Resultados (async) =====
    resultados = await process_urls_async(urls, params)

    return templates.TemplateResponse(
        "tabela.html", 
        {"request": request, "resultados": resultados}
    )
