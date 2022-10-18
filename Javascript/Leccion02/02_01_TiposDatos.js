// Tipos de Datos en JavaScript
/*
Tambien comentamos asi 
*/
var nombre = "Gisela"; //Tipo str
nombre = "Facundo"; //La variable se puede reutilizar
console.log(typeof nombre); //Eso es para ver el tipo de dato

var numero = 2000; //Tipo numerico
console.log(numero);

var objeto = { //Tipo object
    nombre : "Gisela",
    apellido : "Vizcaino",
    edad : "22" //Aca no hace falta coma
}

console.log(typeof objeto);

//Tipo de dato booleano 
var bandera = true;
console.log(bandera)

//Tipo de dato funcion, se reutilizan lineas de codigo 
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol 
var simbolo = Symbol("Mi simbolo")
console.log(typeof simbolo);

//Tipo de dato CLASES que tambien son funciones 
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido; //Referencia a los atributos de la clase 
    }
}

console.log(Persona);
