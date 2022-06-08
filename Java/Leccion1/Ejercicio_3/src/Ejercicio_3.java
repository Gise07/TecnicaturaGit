
import java.util.Scanner;

//Ejercicio 3, area y perimetro de un rectangulo 
public class Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el alto del rectangulo : ");
        int alto = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el ancho del rectangulo");
        int ancho = Integer.parseInt(entrada.nextLine());
        var area = alto * ancho;
        var perimetro = (alto + ancho) * 2;
        System.out.println("El area del rectangulo es = " + area);
        System.out.println("El perimetro del rectangulo es = " + perimetro);
        
    }
}
