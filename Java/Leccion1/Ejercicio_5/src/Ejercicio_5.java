
import java.util.Scanner;


public class Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la primera calificacion : ");
        int nota1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite la segunda calificacion");
        int nota2 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite la tercera calificacion");
        int nota3 = Integer.parseInt(entrada.nextLine());
        var suma = nota1 + nota2 + nota3;
        System.out.println("La suma de las calificaciones es = " + suma);
        
    }
}
