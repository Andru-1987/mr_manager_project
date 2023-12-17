let header = ` <div class="container-md">

<table class="table table-striped">
  <thead>
    <tr>
      <th>Cuota</th>
      <th>Vencmiento</th>
      <th>Descripción</th>
      <th>Valor Cuota</th>
      <th>Moneda</th>
      <th>Estado</th>
    </tr>
  </thead>
  <tbody>
`;

let footer = `
</tbody>
</table>
</div>
`;

function isPastDue(dueMonth, dueYear) {
    let currentMonth = new Date().getMonth() + 1;
    let currentYear = new Date().getFullYear();

    if (currentMonth < 10) {
        currentMonth = `0${currentMonth}`;
    }

    if (dueMonth < 10) {
        dueMonth = `0${dueMonth}`;
    }

    let current = Number(`${currentYear}${currentMonth}`);
    let due = Number(`${dueYear}${dueMonth}`);

    if (due > current) {
        return "🟢 No vencida";
    }
    return "🔴 Vencida";
}

const numberToMonth = (month) => {
    const months = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre",
    };

    return months[month] || null;
};

let templateToInject = (cuotas) => {
    let filledData = "";

    cuotas.forEach((cuota) => {
        const {
            mes_cuota,
            mes_cuota_vencimiento,
            anno_cuota,
            anno_cuota_vencimiento,
            descripcion,
            valor_cuota,
            moneda,
        } = cuota;

        let estado = isPastDue(mes_cuota_vencimiento, anno_cuota_vencimiento);

        let template = `
        <tr>
            <td>${numberToMonth(mes_cuota)} ${anno_cuota}</td>
            <td>${numberToMonth(
                mes_cuota_vencimiento
            )} ${anno_cuota_vencimiento}</td>
            <td>${descripcion}</td>
            <td>${valor_cuota}</td>
            <td>${moneda}</td>
            <td>${estado}</td>
        </tr>
        `;

        filledData += template;
    });

    return header + filledData + footer;
};

if (document.getElementById("cuotas")) {
    document
        .getElementById("cuotas")
        .addEventListener("click", async function (e) {
            e.preventDefault();

            let cuotas = document.getElementById("data__inject");
            cuotas.classList.remove('grilla_consultas')
            
            if (cuotas) {
                while (cuotas.firstChild) {
                    cuotas.removeChild(cuotas.firstChild);
                }
            }

            $.ajax({
                url: "/cuota/list/",
                method: "GET",
                success: function (data) {
                    if (!data || data.length == 0) {
                        console.log("Sin ningun dato");
                        cuotas.innerHTML = "<p>No hay cuotas cargadas!<p>";
                        return;
                    }

                    cuotas.innerHTML = templateToInject(data);
                },
                error: function (error) {
                    console.error(error);
                },
            });
        });
}
