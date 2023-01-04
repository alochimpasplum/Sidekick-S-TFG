import java.util.Scanner;

public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	int VAR1 = null;
	int VAR2 = null;
	VAR1 = 2;
	VAR2 = scan.nextInt();
	VAR1 *= VAR2;
	if (VAR1 <= 10) {
		VAR1 = 15 * VAR2;
	} else {
		VAR1 -= VAR2;
		VAR1 = VAR1 + 5;
		VAR2 = 10 / 5;
	}
	VAR1 = VAR1 + VAR2;
	System.out.println(VAR1);
}
