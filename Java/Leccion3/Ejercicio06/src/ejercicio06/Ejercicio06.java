
package ejercicio06;

import java.util.Scanner;


public class Ejercicio06 {

  
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int numero, suma = 0;
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            suma += numero;
            System.out.println("La suma de los Nº introducidos es: "+ suma);
        }
        System.out.println("El numero"+numero+"finaliza el programa");
        
    }
}
