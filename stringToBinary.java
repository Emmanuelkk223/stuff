import java.util.Scanner;

public class stringToBinary {
    public static void main(String[] args) {
        //! Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);
 
        //* */ Prompt the user to enter a string
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        //? Convert the string to binary and print the result
        String binaryRepresentation = toBinary(input);
        System.out.println("Binary representation: " + binaryRepresentation);

        //// Close the scanner
        scanner.close();
    }

    //todo Method to convert a string to its binary representation
    public static String toBinary(String input) {
        StringBuilder binary = new StringBuilder();
        for (char c : input.toCharArray()) {
            binary.append(String.format("%8s", Integer.toBinaryString(c)).replace(' ', '0')).append(" ");
        }
        return binary.toString().trim();
    }
}
