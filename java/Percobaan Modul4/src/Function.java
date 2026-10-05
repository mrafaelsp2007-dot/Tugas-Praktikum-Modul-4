public class Function {

    public void sapa() {
        System.out.println("Haloo Worldd!!");
    }

    public String perkenalan(String nama, String kota, String hobi) {
        return "Namaku " + nama + ", Aku dari " + kota
                + " dan hobiku adalah " + hobi;
    }

    public void umur(int umur) {
        System.out.println("Aku berumur " + umur + " tahun");
    }

    public static void main(String[] args) {
        System.out.println();
        System.out.println("-----------------");
        Function objek = new Function();
        objek.sapa();
        System.out.println(objek.perkenalan("Rafael", "Bekasi", "Main ff"));
        objek.umur(21);
    }
}