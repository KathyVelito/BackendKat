console.log("hola")

const BASE_URL = "http://127.0.0.1:5000"
const btnProductos = document.getElementById("btn-traer-productos")

fetch(BASE_URL+"/", {method:"GET"}).then((respuesta) =>{
    console.log(respuesta.status)
});

btnProductos.onclick = (e) => {
    fetch(BASE_URL+"/productos", {method:"GET"})
    .then((respuesta) =>{
       return respuesta.json()
    })
    .then((productos) => {
        console.log(productos)
    })
}

btnProductos.addEventListener("click", async () => {
    console.log("Me hizo click 2")
    const respuesta = await fetch(BASE_URL + "/productos", {method: "GET"})
    const productos = await respuesta.json()

    console.log(productos)
})