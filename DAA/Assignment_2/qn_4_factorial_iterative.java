import java.util.Scanner;

public class qn_4_factorial_iterative {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter the value of n: ");
    int n = sc.nextInt();

    int ans = 1;
    while (n > 1) {
      ans *= n;
      n--;
    }

    System.out.println("The factorial of the given n is: " + ans);
  }
}

