public class method {

    static void penjumlahan(int a, int b) {
        int c = a + b;
        System.out.println("Hasil penjumlahan: " + c);
    }

    static void pengurangan() {
        int c = 15 - 20;
        System.out.println("Hasil pengurangan: " + c);
    }

    static int pembagian(int a, int b) {
        int c = a / b;
        return c;
    }

    static int perkalian() {
        int c = 10 * 29;
        return c;
    }

    public static void main(String[] args) {
        penjumlahan(10, 80);
        pengurangan();
        System.out.println("Hasil perkalian: " + perkalian());
        int d = pembagian(100, 20);
        System.out.println("Hasil pembagian: " + d);
    }
}