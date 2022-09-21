//Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo
//y calcular la media 
package EjercicioCiclos07;

import java.util.Scanner;


public class Ejercicio07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero,media,suma = 0,cantNum = 0;
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            cantNum += 1;
            suma += numero;
            media = (suma/cantNum);
        }while(numero >= 0);
        System.out.println("La media de los numeros ingresados es: " +media);
    }
}
