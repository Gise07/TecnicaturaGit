
import java.util.Scanner;

public class Ejercicio__2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float compra;
        double precio_final;
       
        System.out.println("Digite el precio de la compra");
            compra = Float.parseFloat(entrada.nextLine());
        
        if (compra >= 100 )
                precio_final = (compra - compra * 0.2);
        else
            precio_final = compra ;
        
        System.out.println("El precio final de la compra es: " + precio_final + "$");

    }
}
