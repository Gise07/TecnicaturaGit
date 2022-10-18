
package leccionclasesobjeto;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); //Llamamos al constructor 
        //con new accedemos a los atributos 
        persona1.nombre = "Gisela";
        System.out.println("persona1 nombre: " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: "+persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo valor de objeto es: "+persona2.nombre);
    }
    //Debajo del metodo main 
    public static void cambiarValor(Persona persona){ //Parametro por referencia
        persona.nombre = "Facundo";
    }
    //Creamos otro metodo 
    public static Persona cambiarElValor(Persona persona){ //Tipo object
        if(persona == null){
            System.out.println("Valor de persona es invalido: NULL");
            return null;
        }
        else{
            persona.nombre = "Lucas";
            return persona;
        }
        
    }
}
