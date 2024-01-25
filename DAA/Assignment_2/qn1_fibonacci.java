import java.util.Scanner;

public class qn1_fibonacci {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter n: ");
    int count = sc.nextInt();
    System.out.print("The nth fibonacci number is: ");
    System.out.println(fibonacci(1, 1, count)); 
  }

  public static int fibonacci(int a, int b, int count) {
    if (count <= 3) {
      return a + b;
    }
    return fibonacci(b, a + b, count - 1);
  }
}

