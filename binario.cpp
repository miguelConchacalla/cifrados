#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char const *argv[]) {
    vector<int> arr;
    int n;
    cout << "Ingrese numero decimal a convertir en binario: " << endl;
    cin >> n;

    vector<int>::iterator itr;

    while (n != 0) {
        int c = n % 2;
        arr.insert(arr.begin(), c);
        n /= 2;
    }

    while (arr.size() % 4 != 0) {
        arr.insert(arr.begin(), 0);
    }

    // 100 1011 0000
    int i = 1;
    for (itr = arr.begin(); itr != arr.end(); ++itr, ++i) {
        cout << *itr;
        if (i % 4 == 0) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}
