import java.util.random.RandomGenerator;

public class Main {
    /*
    Create a public variable w for (possibly) future external use.
    Although for security reasons we should only use a function that only returns the value of the variable, otherwise it may cause bugs, but in this case we will ignore it.
    */
    public static double[][] w;

    /*
    We will use the private type only for those functions that are used for internal calculations and must be inaccessible outside the class.
    This is a necessity to ensure class security and proper debugging and testing, otherwise it will be hard to catch places where data changes occur.
    */

    private static void generateSX(short[] s, double[] x) {
        for (int i = 1; i <= 16; i++) {
            // Generate reversed array (0=16..15=1)
            s[16 - i] = (short) i;
        }
        for (int i = 0; i < 11; i++) {
            // Generate random number (type Int) in range -14..11, then add it to double array
            // (It's automatically converts to double (-14 => -14.0))
            x[i] = RandomGenerator.getDefault().nextInt(-14, 11);
        }
    }

    private static void calculateW(double[][] w, short[] s, double[] x, int i, int j) {
        switch (s[i]) {
            case 15:
                w[i][j] = Math.log10(Math.sqrt(Math.pow((Math.abs(x[j]) + 1) / 2, 2)));
                break;
            case 1, 3, 7, 8, 11, 12, 13, 16:
                w[i][j] = Math.pow(((double) 3 / 4 * ((Math.pow((Math.cbrt(x[j])), 3) / ((double) 1 / 3 + Math.pow(x[j], x[j] + Math.PI))) + 1)), 3);
                break;
            default:
                w[i][j] = Math.tan(Math.pow(Math.tan(((double) 1 / 2) / x[j]), Math.pow((double) 2 / 3 * Math.tan(x[j]), 2)));
        }
    }

    // Make the output readable and suitable for the requirements
    private static void printFormatted(double[][] w) {
        // Go through rows
        for (double[] row : w) {
            // Go through elements of row
            for (double e : row) {
                System.out.format("%8.4f ", e); // Set format width (8 symbols), and 4 symbols after dot
            }
            System.out.println(); // newline
        }
    }

    public static void main(String[] args) {
        // Initialize variables
        short[] s = new short[16];
        double[] x = new double[11];
        w = new double[16][11];

        // Generate array elements
        generateSX(s, x);

        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 11; j++) {
                calculateW(w, s, x, i, j);
            }
        }

        printFormatted(w); // Output final elements
    }
}