console.log(location.search)     // lee los argumentos pasados a este formulario
var id=location.search.substr(4)
console.log(id)
const { createApp } = Vue
  createApp({
    data() {
      return {
        id:0,
        titulo:"",
        descripcion:"",
        category:"",
        subcategory:"",
        precio:0,
        cantidad:0,
        image:"",
        cuotas:0,
        descuento:0,
        url:'http://localhost:5000/articulos/'+id,
       }  
    },
    methods: {
        
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id=data.id
                    this.titulo = data.titulo;
                    this.descripcion=data.descripcion
                    this.category=data.category
                    this.subcategory=data.subcategory 
                    this.precio=data.precio
                    this.cantidad=data.cantidad
                    this.image=data.image
                    this.cuotas=data.cuotas
                    this.descuento=data.descuento                   
                })
                
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar() {
            
            let articulo = {
                titulo:this.titulo,
                descripcion: this.descripcion,
                category: this.category,
                subcategory:this.subcategory,
                precio:this.precio,
                cantidad:this.cantidad,
                image:this.image,
                cuotas:this.cuotas,
                descuento:this.descuento,
            }

            var options = {
                body: JSON.stringify(articulo),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }

            
            
            fetch(this.url, options)
                .then(function () {
                    alert("Articulo modificado")
                    window.location.href = "./articulos.html";             
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al modificar articulo")
                })      
        }
    },
    created() {
        this.fetchData(this.url)
    },
  }).mount('#app')