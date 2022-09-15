
import javax.swing.JOptionPane;

//CLASE 3 hacerlo en otro proyecto a este 
        //Ejercicio 3: Leer numeros hasta que se introduzca un cero
        //para cada uno indicar si es par o impar.
        //Primero lo haremos con la clase Scanner
        //Luego con la clase JOptionPane 
 //Clase optionpane
public class Ejercicio_03Ciclos {
    public static void main(String[] args){
         int num;
        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(num != 0){
            if (num % 2 ==0) {
                JOptionPane.showMessageDialog(null,"El numero ingresado es par ");
            }
            else {
                JOptionPane.showMessageDialog(null,"El numero ingresado es impar ");
            }
             num = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null,"El numero ingresado" +num+ "finaliza el programa ");
    }
}
