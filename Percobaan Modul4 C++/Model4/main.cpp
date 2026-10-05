#include <iostream>
using namespace std;

class Kalkulus1 {
    public:
        void penjumlahan(int a, int b) {
            int c = a + b;
            cout << "Hasil penjumlahan: " << c << endl;
        }

        void pengurangan() {
            int c = 15 - 50;
            cout << "Hasil pengurangan: " << c << endl;
        }
};

class Kalkulus2 {
    public:
        int pembagian(int a, int b) {
            int c = a / b;
            return c;
        }

        int perkalian() {
            int c = 10 * 30;
            return c;
        }
};

int main() {
    Kalkulus1 objek1;
    Kalkulus2 objek2;

    objek1.penjumlahan(10, 20);
    objek1.pengurangan();
    cout << "Hasil perkalian: " << objek2.perkalian() << endl;
    cout << "Hasil pembagian: " << objek2.pembagian(100, 20) << endl;

    return 0;
}
