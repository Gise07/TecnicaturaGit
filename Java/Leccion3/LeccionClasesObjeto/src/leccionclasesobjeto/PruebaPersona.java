
package leccionclasesobjeto;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //Llama al constructor, es un objeto 
        //Permite asignar valores a la variable 
        persona1.nombre = "Gisela"; //Asignamos valor al atributo 
        persona1.apellido = "Vizcaino";
        persona1.obtenerInformacion(); //Llama al metodo, muestra la inf de los atrivutos 
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " +persona2);
        System.out.println("persona1 = " +persona1);
        persona2.obtenerInformacion();
        //Cada objeto tiene su propia informacion, comparten inf entre objetos 
        persona2.nombre = "Facundo";
        persona2.apellido = "Pereyra<3 Alias cochita";
        persona2.obtenerInformacion();
        //Cada objeto se lo conoce como una instancia 
        
        
        
    }
    
}
