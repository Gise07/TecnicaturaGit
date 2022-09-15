//CLASE 3 hacerlo en otro proyecto a este 
        //Ejercicio 3: Leer numeros hasta que se introduzca un cero
        //para cada uno indicar si es par o impar.
        //Primero lo haremos con la clase Scanner
        //Luego con la clase JOptionPane 
import java.util.Scanner;


public class Ejercicio03Ciclos {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if (numero % 2 ==0) {
                System.out.println("El numero ingresado es par");
            }
            else {
                System.out.println("El numero ingresado es impar");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero ingresado 0 finaliza el programa");
    }
            
}
