import java.util.Scanner; 
public class AddUpto10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int i = sc.nextInt();


        // while (i==i) {
            i = (i*(i+1))/2;
        // }

        System.out.println("Sum from 1 to 10 is: " + i);
    }
}
