// ===== Montar a Tabela Resultados na página ===== //
document.getElementById("form-url-param").addEventListener("submit", async function(event) {
    event.preventDefault(); // não deixar a página recarregar

    const formData = new FormData(this);

    document.querySelector("thead").className = "";
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

