
package Operaciones;


public class Aritmetica {
    //Atributos de la clase 
    int a; //Su valor por default es cero 
    int b;
    
    //CONSTRUCTOR. Es un metodo especial. Construye un objeto 
    public Aritmetica(){ //No es necesario ponerlo 
        System.out.println("Se esta ejecutando el constructor numero uno");
    }
    
    //CONSTRUCTOR 2. Sobrecarga de constrcutores 
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor numero dos");
    }
            
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("Resultado = " + resultado);
    }
    //Para almacenar un objeto o los atributos se utiliza la memoria HEAP
    //SEGUNFO METODO
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1; //El argumento a se asigna al atributo this.a
        this.b = arg2;
        //return a + b;
        return this.sumarConRetorno(); //Es lo mismo que lo de arriba
        
        //aritmetica1 = null; nunca utilizar esto, no se debe hacer 
        //System.gc(); metodo para limpiar residuos, es pesado, no utilizar 
    }
    }

