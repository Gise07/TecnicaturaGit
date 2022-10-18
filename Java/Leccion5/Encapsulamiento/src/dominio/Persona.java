
package dominio;

public class Persona {
    //ATRIBUTOS 
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    //CONSTRUCTOR 
    public Persona(String nombre, double sueldo, boolean eliminado){
    //Debe llevar el mismo nombre de la clase 
    //accede a los atributos para que puedan ser ingresados o modificados 
    this.nombre = nombre; //atributo
    this.sueldo = sueldo;
    this.eliminado = eliminado;
    }
    //CREAMOS METODOS 

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
}
