
const autoridad_data_render = data => {
    const {
        nombre
        , apellido
        , email
        , telefono
        , imagen
        , cargo
        , biografia
    } = data;

    let pattern = `
            <div class="circle_container">
                <span>
                    <h3>${nombre.toUpperCase()} ${apellido.toUpperCase()}</h3>
                    <h5>${cargo.toUpperCase()}</h5>
                    <h5>${cargo == "otro" ? cargo : ''}</h5>
                </span>
                <img class="circle" src="${imagen}" alt="${imagen}"/>
            </div>
            <div>
                <h5>email</h5>
                <h2>${email}</h2>
            </div>
            <div>
                <h2>Contacto</h2>
                <h3>tel: ${telefono}</h3>
            </div>
            <div class="bio__detail">
                <h2>Info</h2>
                <p>${biografia}</p>
            </div>
        `

    return pattern

}



$(document).ready(function () {
    $('.autoridad').click(function () {
        var itemId = $(this).data('item-id');

        $.ajax({
            url: itemId + '/',
            type: 'GET',
            success: function (data) {

                $('#specific-item').html(
                    autoridad_data_render(data)
                );

            }
        });
    });
});



const formatTimestamp = timestamp => {
    const date = new Date(timestamp);

    const monthNames = [
        "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.",
        "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."
    ];

    const month = monthNames[date.getMonth()];
    const day = date.getDate();
    const year = date.getFullYear();
    let hours = date.getHours();
    const minutes = date.getMinutes();

    const amOrPm = hours >= 12 ? 'p.m.' : 'a.m.';
    hours = hours % 12;
    hours = hours ? hours : 12;

    const formattedDate = `${month} ${day}, ${year}, ${hours}:${minutes.toString().padStart(2, '0')} ${amOrPm}`;
    return formattedDate;
}



const novedad_data_render = data => {
    let {

        largo
        , corto
        , edicion
        , creado
        , imagen
        , bio
    } = data;



    let pattern = `
            <div class="banner_container">
                <h1>${largo.toUpperCase()}</h1>
                <h4>${corto.toUpperCase()}</h4>
                <div>
                <img class="banner" src="${imagen}" alt="${imagen}"/>
                </div>
            </div>
            <div>
                <p>${bio}</p>
            </div>
            <div class="editor__footer">
                <h5>Fecha de edicion: ${formatTimestamp(edicion)}</h5>
                <h5>Articulo creado por: ${creado.toUpperCase()}</h5>
            </div>
            
        `

    return pattern

}

$(document).ready(function () {

    $('.novedad').click(function () {
        var itemId = $(this).data('item-id');

        $.ajax({
            url: itemId + '/',
            type: 'GET',
            success: function (data) {

                $('#specific-item').html(
                    novedad_data_render(data)
                );

            }
        });
    });
});



$(document).ready(
    function () {

        if ($('.novedad')[0]) {
            $.ajax({
                url: 1 + '/',
                type: 'GET',
                success: function (data) {

                    $('#specific-item').html(
                        novedad_data_render(data)
                    );

                }
            });
            return
        }

        if ($('.autoridad')[0]) {
            $.ajax({
                url: 1 + '/',
                type: 'GET',
                success: function (data) {

                    $('#specific-item').html(
                        autoridad_data_render(data)
                    );

                }
            });
            return
        }


    }
)





function getCSRFToken() {
    let cookies = document.cookie.split(';');

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.split('=')[1];
        }
    }

    return '';
}


// Function to join or leave the course via AJAX
function updateCourseStatus(actionType, cursoId, type) {
    $.ajax({
        url: `/beneficios/curso/${cursoId}/${actionType}/`,
        type: type,
        data: {
            csrfmiddlewaretoken: getCSRFToken(),
            // You can add additional data if needed
        },

        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCSRFToken()); // Set CSRF token in request header
        },
        success: function (data) {
            if (type == 'DELETE') {
                Swal.fire({
                    icon: "error",
                    text: `${data.message}`,
                    allowOutsideClick: false,
                    showConfirmButton: false,
                    timer: 3000,
                });
            }

            Swal.fire({
                icon: "success",
                text: `${data.message}`,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 3000,
            });

        },
        error: function (error) {
            Swal.fire({
                icon: "error",
                text: `${JSON.stringify(error)}`,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 3000,
            });

        },
    });
}

// Event listeners for joining and leaving the course
$(document).ready(function () {
    $('#join-course').click(function () {
        const cursoId = $(this).data('curso-id');
        updateCourseStatus('join', cursoId, 'POST');
    });

    $('#leave-course').click(function () {
        const cursoId = $(this).data('curso-id');
        updateCourseStatus('leave', cursoId, 'DELETE');
    });
});
