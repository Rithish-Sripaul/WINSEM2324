import java.util.Scanner;

public class qn3_factorial_recursive {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the value of n: ");
    int n = sc.nextInt();
    System.out.print("The factorial of given n is: ");
    System.out.println(factorial(n));
  }

  public static int factorial(int n) {
    if (n == 0) {
      return 1;
    }
    return n * factorial(n - 1);
  }

}
