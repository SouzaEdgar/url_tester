// ===== Montar a Tabela Resultados na página ===== //
document.getElementById("form-url-param").addEventListener("submit", async function(event) {
    event.preventDefault(); // não deixar a página recarregar

    const formData = new FormData(this);

    document.querySelector("thead").className = "";
    document.getElementById("btns-container").style.display = "flex";
    const tabelinha = document.querySelector("#results_body");

    // ----- Loading da Tabela *-* ----- //
    tabelinha.innerHTML = `
        <tr>
            <td colspan="4" style="text-align:center; padding:20px;">
                <div class="spinner"></div>
                <div>Processando... </div>
            </td>
        </tr>
    `;

    try {
        // usar a rota ajax
        const response = await fetch("/ajax", {
            method: "POST",
            body: formData
        });

        const html = await response.text();

        // injeta os resultados
        tabelinha.innerHTML = html;
        // move a tela para a tabela quando aparecer
        tabelinha.scrollIntoView({ behavior: "smooth", block: "start" });

    } catch (error) {
        tabelinha.innerHTML = `
            <tr>
                <td colspan="4" style="text-align:center; color:red;">
                    Ocorreu um erro: ${error}
                </td>
            </tr>
        `;
    }
});

// ===== Mover a tabela ao clicar no botão UP/DOWN =====
const tabela = document.querySelector("table");
document.getElementById("btn_up").addEventListener("click", () => {
    tabela.scrollIntoView({ behavior: "smooth", block: "start" });
});

document.getElementById("btn_down").addEventListener("click", () => {
    tabela.scrollIntoView({ behavior: "smooth", block: "end" });
});
