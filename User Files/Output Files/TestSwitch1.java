import java.util.Scanner;

public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	int VAR = null;
	VAR = scan.nextLine();
	switch (VAR) {
		case 1:
			VAR -= 1;
			break;
		case 4:
			VAR += 7;
			VAR /= 2;
			break;
		default:
			VAR *= 10;
	}
	System.out.println(VAR);
}
