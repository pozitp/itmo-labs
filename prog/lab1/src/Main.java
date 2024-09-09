import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.random.RandomGenerator;

public class Main {
    public static double[][] w;

    private static void generateRX(short[] arrShort, double[] arrDouble) {
        for (int i = 1; i <= 16; i++) {
            arrShort[16 - i] = (short) i;
        }
        for (int i = 0; i < 11; i++) {
            arrDouble[i] = RandomGenerator.getDefault().nextDouble(-14.0, 11.0);
        }
    }

    private static String formatArr(double[][] arr) {
        String[][] tmp = new String[16][11];

        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 11; j++) {
                tmp[i][j] = new DecimalFormat("##.####").format(arr[i][j]);
            }
        }
        return Arrays.deepToString(tmp);
    }

    public static void main(String[] args) {
        short[] r = new short[16];
        double[] x = new double[11];
        w = new double[16][11];

        generateRX(r, x);

        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 11; j++) {
                switch (r[i]) {
                    case 15:
                        w[i][j] = Math.log10(
                                Math.sqrt(
                                        Math.pow(
                                                (Math.abs(x[j]) + 1) / 2
                                                , 2)
                                )
                        );
                        break;
                    case 1, 3, 7, 8, 11, 12, 13, 16:
                        w[i][j] = Math.pow(((double) 3 / 4 * ((Math.pow((Math.cbrt(x[j])), 3) / ((double) 1 / 3 + Math.pow(x[j], x[j] + Math.PI))) + 1)), 3);
                        break;
                    default:
                        w[i][j] = Math.tan(Math.pow(Math.tan(((double) 1 / 2) / x[j]), Math.pow((double) 2 / 3 * Math.tan(x[j]), 2)));
                        break;
                }
            }
        }

        System.out.println(formatArr(w));
    }
}