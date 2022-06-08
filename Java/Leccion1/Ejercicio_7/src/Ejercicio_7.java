
import java.util.Scanner;

public class Ejercicio_7 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        var salario = 1000;
        System.out.println("Digite la cantidad de autos vendidos : ");
        int carrosVendidos = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite la suma de los valores de los autos vendidos : ");
        int valorCarro = Integer.parseInt(entrada.nextLine());
        var valorDeVenta = valorCarro * 0.05;
        var comision = (carrosVendidos * 150) + valorDeVenta;
        var salario2 = salario + comision;
        System.out.println("El salario mensual del vendedor sera : " + salario2 + "$");

    }

}
