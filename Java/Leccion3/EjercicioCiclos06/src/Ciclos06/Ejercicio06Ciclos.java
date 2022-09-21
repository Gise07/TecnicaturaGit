
package Ciclos06;

import java.util.Scanner;


public class Ejercicio06Ciclos {
    public static void main(String[] args) {
   /* Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        int suma = 0;
        while(numero > 0){
            suma += numero;
            System.out.println("La suma de los Nº introducidos es: "+ suma);
        }
        System.out.println("El numero"+numero+"finaliza el programa");
*/
   Scanner entrada = new Scanner(System.in);
   int numero,suma = 0;
   do{
       System.out.println("Digite un numero: ");
       numero = Integer.parseInt(entrada.nextLine());
       suma += numero;
   }while(numero != 0);
        System.out.println("\nLa suma de todos los numeros ingresados es: "+suma);
        
}
}
