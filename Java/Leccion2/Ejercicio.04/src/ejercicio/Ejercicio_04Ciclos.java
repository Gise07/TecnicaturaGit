
import javax.swing.JOptionPane;


public class Ejercicio_04Ciclos {
    public static void main(String[] args) {
      
        int numero,cantidadNumeros = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
           cantidadNumeros ++;
           JOptionPane.showMessageDialog(null,"El numero: " +numero+ " es positivo");
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
           JOptionPane.showMessageDialog(null,"La cantidad de numeros ingresados positivos son: "+cantidadNumeros);
        
    }
}
