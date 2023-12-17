// ================================  LOADER  ====================================== //

setTimeout(() => {
    const loader = document.querySelector(".loader");
    loader.style.opacity = "0";
    loader.style.backgroundColor = "transparent";
    setTimeout(() => {
        loader.style.display = "none";
        document.body.style.overflow = "visible";
    }, 500);
}, 1000);




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


function generateStringFromObject(obj) {
    let result = '';
    if (object){

        for (const [key, value] of Object.entries(obj)) {
            result += `${key}: ${Array.isArray(value) ? value.join(' ') : value}\n`;
        }
    }
    
    return result;
  }
  





function modifyFormData(formData) {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  
    checkboxes.forEach(function(checkbox) {
        formData.append(checkbox.name, Boolean(checkbox.value))
    });
}


if (document.getElementById('registro-form')){
    document.getElementById('registro-form').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        let formData = new FormData(this);
        
        modifyFormData(formData);

        
        
        try {
            let post_data = await fetch('/register/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken':  getCSRFToken(),
                    'X-Requested-With': 'XMLHttpRequest'
                    
                }
            })
            
            let data = await post_data.json()
            

            if (!post_data.ok) {
        
                throw new Error(generateStringFromObject(data.error));
            }
        

            Swal.fire({
                icon: "success",
                text: `Usuario : ${data.dni} creado exitosamente`,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 4000,
            });

            setTimeout(function() {
                window.location.href = '../login/';
            }, 3000); 


            
        }


        catch(error ) {

            Swal.fire({
                icon: "error",
                text: error,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 4000,
            });
            
        }
    })
}





if (document.getElementById('login-form')){
    document.getElementById('login-form').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        let formData = new FormData(this);
        
        modifyFormData(formData);


        try {

            let post_data = await fetch("/login/", {
                                method: 'POST',
                                body: formData,
                                headers: {
                                    'X-CSRFToken':  getCSRFToken(),
                                    'X-Requested-With': 'XMLHttpRequest'
                                    
                                }
                            })
            let data = await post_data.json()
            
            if (data.status !="success"){
                throw new Error( `${data.message}`);

            } 

            Swal.fire({
                icon: "success",
                text: `Bienvenido ${data.usuario}`,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 2000,
            });

            setTimeout(function() {
            
                window.location.href = '/beneficios/curso/';
            }, 3000); 

            

        }


        catch(error ) {

            Swal.fire({
                icon: "error",
                text: error,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 1000,
            });
            
        }
    })
}





if (document.getElementById('update-form')){
    document.getElementById('update-form').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        let formData = new FormData(this);
        
        modifyFormData(formData);

        try {

            let post_data = await fetch(window.location.href, {
                                method: 'POST',
                                body: formData,
                                headers: {
                                    'X-CSRFToken':  getCSRFToken(),
                                    'X-Requested-With': 'XMLHttpRequest'
                                    
                                }
                            })
            let data = await post_data.json()
                            
            console.log(data)

            if (!post_data.ok) {
                throw new Error( `${data.message}`);
            }
        
            

            Swal.fire({
                icon: "success",
                text: `Bienvenido ${data.usuario}`,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 2000,
            });

            setTimeout(function() {
            
                window.location.href = '/';
            }, 3000); 

            

        }


        catch(error ) {

            Swal.fire({
                icon: "error",
                text: error,
                allowOutsideClick: false,
                showConfirmButton: false,
                timer: 1000,
            });
            
        }
    })
}

/* Delete files with AJAX*/

$(document).ready(function() {
    $('.delete-file').on('click', function() {
        var fileId = $(this).data('file-id');
        if (confirm('¿Estás seguro/a de borrar este archivo?')) {
            $.ajax({
                type: 'POST',
                url: `/file/delete/${fileId}/`,  
                data: {
                    csrfmiddlewaretoken: getCSRFToken()
                },
                success: function(response) {

                    location.reload(); 
                },
                error: function(error) {
                    console.error('Failed to delete file:', error);
                }
            });
        }
    });
});

