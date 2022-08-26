
import java.util.Scanner;


public class Ejercicio1 {
     public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Creamos variables
        int nota1;
        int nota2; 
        int nota3;
        
        System.out.println("Digite la primera calificacion: ");
        nota1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite la segunda calificacion: ");
        nota2 = entrada.nextInt(); 
        System.out.println("Digite la tercera calificacion: ");
        nota3 = Integer.parseInt(entrada.nextLine());
        
        if (nota1 + nota2 + nota3 / 3 >= 70)
        {
            System.out.println("El alumno esta aprobado");
        }
        else
            System.out.println("El alumno esta desaprobado");
        
     }
}
