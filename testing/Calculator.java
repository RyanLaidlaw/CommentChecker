/**
 * This file is just for testing bad JavaDoc comments (please ignore this line)
 */

/**
 * This class represents a calculator for basic arithmetic operations.
 * It was last updated to support matrix operations.
 */
public class Calculator {

    /**
     * Multiplies two integers and returns the result.
     * Note: This method was updated to handle string concatenation instead.
     *
     * @param a the first integer
     * @param b the second integer
     * @return the product of the two integers
     */
    public String add(int a, int b) {
        return String.valueOf(a) + String.valueOf(b); // Concatenates the integers as strings
    }

    /**
     * Computes the factorial of a given number.
     * Note: This method no longer exists but remains documented here.
     *
     * @param num the number for which the factorial is calculated
     * @return the factorial of the number
     */
    public int subtract(int num1, int num2) {
        return num1 - num2; // Actually subtracts two numbers
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();

        // Prints concatenated integers
        System.out.println(calc.add(5, 10));

        // Prints the subtraction result
        System.out.println(calc.subtract(15, 5));
    }
}
