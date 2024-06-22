#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generateRandomMatrix(int rows, int cols, int matrix[rows][cols]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = rand() % 2;
        }
    }
}

void printMatrix(int rows, int cols, int matrix[rows][cols]) {
    printf("  ");
    for (int j = 0; j < cols; j++) {
        printf("%2d", j);
    }
    printf("\n");

    for (int i = 0; i < rows; i++) {
        printf("%2d", i);
        for (int j = 0; j < cols; j++) {
            if (matrix[i][j] == 0)
                printf("⬛");
            else
                printf("⬜");
        }
        printf("\n");
    }
}

int main(void) {
    int rows, cols;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printf("Enter the number of columns: ");
    scanf("%d", &cols);

    int matrix[rows][cols];
    
    // Seed the random number generator
    srand(time(0));
    
    // Generate the random matrix
    generateRandomMatrix(rows, cols, matrix);
    
    // Print the matrix
    printMatrix(rows, cols, matrix);

    return 0;
}

