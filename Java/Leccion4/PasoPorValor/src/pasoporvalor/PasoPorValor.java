
package pasoporvalor;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); //Solo le enviamos una copia del atributo
        System.out.println("valorX = " + valorX);
    }
    //Creamos un metodo despues del main 
    
    public static void cambioValor(int arg1){ //Parametro por valor 
        System.out.println("arg1 = " + arg1); 
        arg1 = 15; //No cambia porque usamos la variable local 
    }
}
