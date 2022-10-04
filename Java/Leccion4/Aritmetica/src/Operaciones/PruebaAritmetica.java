
package Operaciones; //Carpeta de origen

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica(); //LLAMA AL CONSTRUCTOR
        aritmetica1.a = 3;
        aritmetica1.b = 7; //DAMOS VALORES A VARIABLES, ATRIBUTOS
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12,12);
        System.out.println("Resultado usando arumentos = "+resultado);
        
    }
}
