
package Operaciones; //Carpeta de origen

public class PruebaAritmetica {
    public static void main(String[] args) {
        int a = 10; //variables locales 
        int b = 7;  //MEMORIA STACK
        miMetodo(); //llamamos el nuevo metodo
        Aritmetica aritmetica1 = new Aritmetica(); //LLAMA AL CONSTRUCTOR
        aritmetica1.a = 3;
        aritmetica1.b = 7; //DAMOS VALORES A VARIABLES, ATRIBUTOS
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12,12);
        System.out.println("Resultado usando arumentos = "+resultado);
        
        //Muestra los valores de los atributos a y b 
        System.out.println("aritmetica1 a:"+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 10); //Nuevo objeto, con cons 2 
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //System.gc(); metodo para limpiar residuos, es pesado, no usar 
        Persona persona = new Persona(new String ("Gisela"), ("Vizcaino")); //Pasamos argumentos 
        //Creamos un nuevo objeto de tipo string 
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
         
    }
    //CREAMOS OTRO MODULO, otro metodo 
    public static void miMetodo(){
        //a  = 10; Una variable esta limitada 
        System.out.println("Aqui hay otro metodo");
    }
}
//SEGUNDA CLASE 
class Persona{
        String nombre;
        String apellido;
        
        Persona(String nombre, String apellido){ //CONSTRUCTOR DE LA CLASE 
            super(); //TIENE QUE IR PRIMERO
            //Imprimir imprimir = new Imprimir();
            //super(); //llama al constructor clase padre object
            new Imprimir().imprimir(this);
            this.nombre = nombre;
            this.apellido = apellido;
            System.out.println("Objeto persona usando this: "+this);
        }
}

class Imprimir{
    public Imprimir(){
        super(); //El constructor de la clase padre, para reservar memoria 
    }
    //metodo dentro de clase imprimir 
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this):"+this);
    }
   
}
