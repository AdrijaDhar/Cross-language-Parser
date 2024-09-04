// C++ code
#include <iostream>

using namespace std;

int main() {
    // Factorial of a number
    int n = 5;
    int factorial = 1;
    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }
    cout << "Factorial: " << factorial << endl;
    return 0;
}
