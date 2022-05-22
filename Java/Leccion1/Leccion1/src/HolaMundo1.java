
import java.util.Scanner;

public class HolaMundo1 {

    public static void main(String[] args) {

        /*System.out.println("Hola mundo");
        //USAMOS SIEMPRE PUNTO Y COMA 
        int miVariable = 10;
         System.out.println(miVariable);
         //Reutilizamos la variable 
         miVariable = 5; //Aca va sin el int para redefinir
         System.out.println(miVariable);
         //Tipo string 
         String miVariableCadena = "Facu 0705";
         miVariableCadena = "Teamomiamor"; //Reutilizamos la variable 
         System.out.println(miVariableCadena);
         */
        //Var - Inferencia de tipos en Java 
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        //Concatenacion de cadenas 
        System.out.println("miVariableEntera2= " + miVariableEntera2);
        System.out.println("miVariableCadena2= " + miVariableCadena2);
        //soutv + tab para que salga lo de arriba 
        //Para ejecutar Shift + F6, es la tecla para mayuscula 
        //Reglas para definir una variable en Java 
        //Se recomienda camelCase, no se pueden usar numeros como primer caract
        var miVariableEjemplo = 21;*/
        //var 2miVariable...Esta mal 
        /* var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicio: Caracteres especiales con Java 
        var nombre = "Gisela";
        System.out.println("Nueva linea: \n"+nombre); //Diagonal inversa y letra n
        System.out.println("Tabulador: \t"+nombre); //Espacio para centrar
        System.out.println("\t.:MENU:.");
        System.out.println("Retroceso: \b"+nombre); //Caracter de retroceso
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas Dobles: \""+nombre+"\""); */
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine(); //Para que lea en consola 
        System.out.println("usuario2 = " + usuario2); //String 
        System.out.println("Escriba el titulo ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " + titulo2 + " " + usuario2);
        //Ejercicio
        Scanner scanner = new Scanner(System.in);
        //Escribe tu solucion aqui
        System.out.println("Proporciona el titulo: ");
        String titulo = scanner.nextLine();
        System.out.println("Proporciona el autor: ");
        String autor = scanner.nextLine();
        System.out.println(titulo + "fue escrito por " + autor); */
 /*byte numEnteroByte = 10; //Literal de tipo entero
        System.out.println("Valor minimo del Byte:" + Byte.MIN_VALUE); //Minimo -128
        System.out.println("Valor minimo del Byte:" + Byte.MAX_VALUE); //Maximo 127

        short numEnteroShort = 32767;
        System.out.println("Valor minimo del Short:" + Short.MIN_VALUE);
        System.out.println("Valor minimo del Byte:" + Byte.MAX_VALUE);

        int numEnteroInt = 265895412;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del INT:" + Integer.MIN_VALUE);
        System.out.println("Valor minimo del Byte:" + Integer.MAX_VALUE);

        long numEnteroLong = 895623586998554235L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long:" + Long.MIN_VALUE);
        System.out.println("Valor minimo del Long:" + Long.MAX_VALUE);
        
        float numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de float:"+ Float.MIN_VALUE);
        System.out.println("El vamor maximo de float:"+Float.MAX_VALUE);*/
 /*double numDouble = 10; //Es el maximo dentro de Java 
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de double:" + Double.MIN_VALUE);
        System.out.println("El vamor maximo de double:" + Double.MAX_VALUE); */
        //Inferencia de tipos var y tipos primitivos 
        /*var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = "+numEntero);
        var numFloat = 10.0F; //Automaticamente con el punto se transforma en tipo double 
         System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
         System.out.println("numDouble = " + numDouble);*/
        //Tipos primitos char
        /*char miVariable = 'a';
        System.out.println("miVariable = " + miVariable);

        char varCharacter = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCharacter = " + varCharacter);
        char varCharacterDecimal = 36; //Valor decimal del juego de caracteres
        System.out.println("varCharacterDecimal = " + varCharacterDecimal);
        char varCharacterSimbolo = '$'; //Un caracter esoecial, podemos copiar y pegar desde unicode
        System.out.println("varCharacterSimbolo = " + varCharacterSimbolo);

        var varCharacter1 = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCharacter1 = " + varCharacter1);
        var varCharacterDecimal1 = (char) 36; //Valor entero y le asigna un tipo int
        System.out.println("varCharacterDecimal1 = " + varCharacterDecimal1);
        var varCharacterSimbolo1 = '$'; //Un caracter esoecial, podemos copiar y pegar desde unicode
        System.out.println("varCharacterSimbolo1 = " + varCharacterSimbolo1);

        int varEnteroChar = '$';
        System.out.println("varEnteroChat = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar); */
        //Tipos primitivos tipos booleanos 
        /*boolean varBool = true; // Tiene que ir con minuscula, True NO
        System.out.println("varBool = " + varBool);

        if (varBool) { //Llaves que abren el if
            System.out.println("La bandera es verde");
        }//Llaves que cierran el if
        else {
            System.out.println("La bandera es roja");
        }

        //Algoritmo: ¿Es mayor de edad?
        var edad = 15; //Literal tener presente la inferencia de tipos
        //var adulto = edad >= 18; //Esta es una expresion booleana
        if (edad >=18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }*/
        //Conversion de tipos primitivos
        /*var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI= " + valorPI);*/
        //Pedir un valor 
        /* var entrada = new Scanner(System.in);
        System.out.println("Digite su edad: ");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        //Conversion de tipos primitivos en Java parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);

        var fraseChar = "programadores".charAt(12); //12 para que muestre las 12 letras
        System.out.println("fraseChar = " + fraseChar);

        System.out.println("Digite un caracter : ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar= " + fraseChar); */
        //Operadores aritmeticos CLASE 7
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("Solucion de la suma = " + solucion);
        solucion = num1 - num2;
        System.out.println("Solucion de la resta = " + solucion);
        solucion = num1 * num2;
        System.out.println("Solucion de la multiplicacion = " + solucion);

        var solucion2 = 3.4D / num2;
        System.out.println("solucion2 resultado de la division = " + solucion2);

        solucion = num1 % num2;//Guarda el residuo entero de la division
        System.out.println("solucion= " + solucion); // 5/4

        if (num1 % 2 == 0) 
            System.out.println("Es un numero Par"); //No tiene llaves xq tiene una sola linea de bloque
        else 
            System.out.println("Es un numero Impar"); //Segunda linea de codigo 
        
        //Ejercicio
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; //Una operacion
        System.out.println("varNum3= " + varNum3);
        
        varNum1 += 1; //varNum1 = varNum1 +1;
        System.out.println("varNum1= " + varNum1);
        
        //Tarea: -= , *= , /=, %= 
        varNum1 -= 1;
        System.out.println("varNum1= " + varNum1);
        varNum1 *= 1;
        System.out.println("varNum1= " + varNum1);
        varNum1 /= 1;
        System.out.println("varNum1= " + varNum1);
        varNum1 %= 1;
        System.out.println("varNum1= " + varNum1);
        
        
    }
}
