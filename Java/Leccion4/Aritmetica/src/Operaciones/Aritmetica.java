
package Operaciones;


public class Aritmetica {
    //Atributos de la clase 
    int a; //Su valor por default es cero 
    int b;
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("Resultado = " + resultado);
    }
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
        
        
    }
    }

