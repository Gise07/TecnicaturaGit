
import java.util.Scanner;

public class Leccion_2 {

    public static void main(String[] args) {
        var condicion = true;
        if (condicion) {
            System.out.println("Condicion Verdadera"); //Condicional simple
        } else {
            System.out.println("Condicion Falsa"); //Condicional doble 

            var numero = 2;
            var numeroTexto = "Numero desconocido";
            if (numero == 1) {
                numeroTexto = "Numero uno";
            } else if (numero == 2) {
                numeroTexto = "Numero dos";
            } else if (numero == 3) {
                numeroTexto = "Numero tres";
            } else if (numero == 4) {
                numeroTexto = "Numero cuatro";
            } else {
                numeroTexto = "Numero no encontrado";
            }
            System.out.println("numeroTexto = " + numeroTexto);
        }

        //Ejercicio 1 : estaciones del año if else 
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un mes del año");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "Estacion desconocida";
        if (mes == 1 || mes == 2 || mes == 3) {
            estacion = "Verano";
        } else if (mes == 4 || mes == 5 || mes == 6) {
            estacion = "Otonio";
        } else if (mes == 7 || mes == 8 || mes == 9) {
            estacion = "Invierno";
        } else if (mes == 10 || mes == 11 || mes == 12) {
            estacion = "Primavera";
        }
        System.out.println("estacion = " + estacion);

        //SENTENCIA DE CONTROL SWITCH
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        //var numero = 2;
        var numeroTexto = "Valor desconocido";
        switch (numero) {
            case 1:
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4:
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);

        //Ejercicio 2 : Condicional 
        System.out.println("Digite un numero del mes");
        var mes2 = Integer.parseInt(entrada.nextLine());
        var estacion2 = "Estacion desconocida";
        switch (mes) {
            case 1:
            case 2:
            case 3:
                estacion2 = "Verano";
                break;
            case 4:
            case 5:
            case 6:
                estacion2 = "Otoño";
                break;
            case 7:
            case 8:
            case 9:
                estacion2 = "Invierno";
                break;
            case 10:
            case 11:
            case 12:
                estacion2 = "Primavera";
                break;
        }
        System.out.println("estacion = " + estacion);
        
        //Ejercicio Condicional 3
        System.out.println("Digite un numero entre 0 y 10: ");
        var calificacion = Integer.parseInt(entrada.nextLine());
        if(calificacion >= 9 && calificacion <= 10) {
            System.out.println("A");
        }
        else if(calificacion >= 8 && calificacion < 9) {
            System.out.println("B");
        }
        else if(calificacion >= 7 && calificacion < 8) {
            System.out.println("C");
        }
        else if(calificacion >= 6 && calificacion < 7){
            System.out.println("D");
        }
        else if(calificacion >= 0 && calificacion < 6){
            System.out.println("F");
        }
        else {
            System.out.println("Fuera de rango");
        }

    }
}
