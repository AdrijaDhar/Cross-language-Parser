
import java.util.*;

public class Main4 {
    public static void main(String[] args) {
        // Factorial of a number
        int n = 5;
        int factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        System.out.println("Factorial: " + factorial);
    }
}
