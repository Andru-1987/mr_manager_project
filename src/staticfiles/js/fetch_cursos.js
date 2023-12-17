let curso_header = ` 
<div class="container-md">
<table class="table table-striped">
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Status</th>
      <th>Inicio</th>
      <th>Dictado</th>
    </tr>
  </thead>
  <tbody>
`

let curso_footer = `
</tbody>
</table>
</div>
`


const formatDate = (inputDate) => {
  const months = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
  ];

  const date = new Date(inputDate);
  const monthIndex = date.getMonth();
  const day = date.getDate();
  const year = date.getFullYear();

  return `${months[monthIndex]} ${day}, ${year}`;
}

let cursoToInject = (cursos,total) =>{

  let filledData = ''
  let total_value = `
  
  <div>
    <p>
    Cantidad de cursos : 
    <b>${total}</b>
    </p>
  </div>
  `

  cursos.forEach(curso => {
    
      const {      
          dictado
        , inicio
        , nombre
        , status
      } = curso



      let template = `
      <tr>
          <td>${nombre}</td>
          <td>${status}</td>
          <td>${formatDate(inicio)}</td>
          <td>${dictado}</td>
      </tr>
      `

    filledData += template
    })
    

  return  total_value + curso_header + filledData + curso_footer
}




if (document.getElementById('cursos')){
    document.getElementById('cursos').addEventListener('click', async function(e) {
        
        e.preventDefault();

        let cursos_ = document.getElementById("data__inject")

        if (cursos_) {
          while (cursos_.firstChild) {
            cursos_.removeChild(cursos_.firstChild);
          }
        }

        $.ajax({
            url: '/beneficios/curso/persona/',
            method: 'GET',
            success: function(data_) {

              let {data:cursosFetch,total} = data_
              


              if (!cursosFetch || cursosFetch.length == 0) {
                console.log("Sin ningun dato")
                cursos_.innerHTML = "<p>No hay cursos cargadas!<p>"
                return 
              }
              
              
              cursos_.innerHTML =   cursoToInject(cursosFetch,total);
            },
            error: function(error) {
                
                console.error(error);
            }
        })
        
})}
