
import java.util.Scanner;


public class Ejercicio__6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la cantidad de dolares que tiene Guillermo : ");
        int dolares = Integer.parseInt(entrada.nextLine());
        var dolaresLuis = dolares/ 2;
        var dolaresJuan = (dolares + dolaresLuis) / 2;
        var dolaresSuma = dolares + dolaresLuis + dolaresJuan;
        System.out.println("Guillermo, Luis y Juan tienen = " + dolaresSuma + " " + "USD$");
    }
}
