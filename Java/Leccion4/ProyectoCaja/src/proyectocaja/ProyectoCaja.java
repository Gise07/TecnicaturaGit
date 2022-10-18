/*
Proyectocaja: 
Ejercicio 1: Crear un proyecto segun las especificaciones mostradas a continuacion.
La formula es: volumen = ancho * alto* profundidad 
*/
package proyectocaja;
public class ProyectoCaja { //Clase publica caja 
    //Atributos(caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores(acciones)
    public ProyectoCaja() { //Constructor 1 = vacio
        //Esto es por si queremos recibir parametros 
    }
    //Constructor con parametros
    public ProyectoCaja(int ancho, int alto, int profundo){ //Constructor 2 
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
               
    }
    
    public int calcularVolumen () { //Metodo para calcular
        return ancho * alto * profundo;
        
    }
}
