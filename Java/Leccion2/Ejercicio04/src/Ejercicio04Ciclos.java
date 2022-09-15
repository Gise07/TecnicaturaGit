
import java.util.Scanner;

//Ejercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar 
//cuantos numeros se han introducido
//Lo hacemos primero con la clase Scanner 
//Luego con la clase JOptionPane

public class Ejercicio04Ciclos {
    public static void main(String[] args) {
        
        var cantidadNumeros = 0;
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
           cantidadNumeros += 1;
           System.out.println("El numero: " +numero+ "es positivo");
           System.out.println("Digite otro numero: ");
           numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresado" +cantidadNumeros+ "que no son negativos");
    }
}
            