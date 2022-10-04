
package ejerciciociclos08;

import javax.swing.JOptionPane;

public class EjercicioCiclos008 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i ++;
        }
    }
}
