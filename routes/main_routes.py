from flask import Blueprint, render_template, request
from services.url_service import process_urls

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def home():
    resultados = []

    if request.method == "POST":
        urls = request.form.get("url", "").splitlines()
        params_raw = request.form.get("parameter", "")
        
        resultados = process_urls(urls, params_raw)

    return render_template("index.html", resultados=resultados)
