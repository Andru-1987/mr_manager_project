const modalItem = (data) => {
    const {
        id,
        titulo_consulta = "Aigasra mensaje",
        fecha_consulta,
        temas_relacionados = "Sin tema relacionado",
        receptor_consulta = "Sin nombre",
        consulta_texto,
        file_info,
    } = data;

    const template = `
        <div class="consulta">
            <div type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal_${id}">
                ${titulo_consulta} <br> Desde: ${receptor_consulta}
            </div>

            <div class="modal fade" id="modal_${id}" tabindex="0" aria-labelledby="modal_${id}Label" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
                <div class="modal-dialog modal-dialog-centered modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="modal_${id}Label">${temas_relacionados}</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <p>Fecha de mensaje: ${fecha_consulta}</p>
                            <p><b>Consulta realizada a: ${receptor_consulta}</b></p>
                            <i>${consulta_texto}</i>
                            <div class="files__uploaded">
                                ${file_info
                                    .map(
                                        (file) => `
                                    <details>
                                        <summary>${file.name}</summary>
                                        <div>
                                            <p>${file.type}</p>
                                            <a href='${file.path}' download="filename">Descargar el archivo</a>
                                        </div>
                                    </details>
                                `
                                    )
                                    .join("")}
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    return template;
};

const consultas = document.getElementById("data__inject");

if (consultas) {
    const consulta = document.getElementById('consultas')
    consulta.addEventListener("click", async function (e) {
        e.preventDefault();

        while (consultas.firstChild) {
            consultas.removeChild(consultas.firstChild);
        }

        consultas.classList.add("grilla_consultas");

        try {
            const response = await fetch("/consulta/all_by_user/");
            const data = await response.json();

            if (!data || data.length === 0) {
                consultas.innerHTML = "<p>No hay consultas cargadas!</p>";
                return;
            }

            const { data: consultas_api } = data;
            const fragment = document.createDocumentFragment();

            for (const consulta of consultas_api) {
                const modalContent = modalItem(consulta);
                const temp = document.createElement("template");
                temp.innerHTML = modalContent.trim();
                fragment.appendChild(temp.content);
            }

            consultas.appendChild(fragment);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    });
}
