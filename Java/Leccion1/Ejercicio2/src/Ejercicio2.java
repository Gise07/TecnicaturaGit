
import java.util.Scanner;

//Ejercicio2, cuanto gana un empleado segun lo trabajado y lo que gana
public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Creamos variables
        int horasSemanales;
        float salarioHora, salarioTotal;
        
        System.out.println("Digite las horas semanales trabajadas: ");
        horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el salario que cobra por hora");
        salarioHora = Float.parseFloat(entrada.nextLine()); //Casteo
        
        salarioTotal = horasSemanales * salarioHora;
        System.out.println("\nEl salario semanal es : US$" + salarioTotal);
        
        
    }
}
