#include <stdio.h>

int main() {
    int a = 25;

    for (int i = 0; i <= 4; i++) {
        for (int j = 0; j <= 4; j++) {
            if (i == j) {
                a += 1;
            } else if (j == 4) {
                a += 2;
            }
        }
    }

    a += 10;

    printf("%d\n", a);  // Output: 48
    return 0;
}