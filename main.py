#PYTHON 

def print_pyramid(rows):
    print(f"\nGenerating a Pyramid with {rows} rows...")
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    print("\nLogic: Inner loop handles spaces (rows-i-1) and stars (2*i+1).")

rows = int(input("Enter number of rows: "))
print_pyramid(rows)


#C++ 
#include <iostream>
using namespace std;

void printPyramid(int rows) {
    cout << "\n--- Generating Pyramid in C++ ---\n";
    
    for (int i = 1; i <= rows; i++) {
        // 1. Logic for Spaces
        for (int j = 1; j <= rows - i; j++) {
            cout << " ";
        }
        // 2. Logic for Stars
        for (int k = 1; k <= (2 * i - 1); k++) {
            cout << "*";
        }
        cout << endl;
    }
    
    cout << "\n[Logic Breakdown]:" << endl;
    cout << "- Outer loop runs for 'rows' times." << endl;
    cout << "- First inner loop handles leading spaces: (rows - i)." << endl;
    cout << "- Second inner loop handles odd-numbered stars: (2*i - 1)." << endl;
}

int main() {
    int rows;
    cout << "Enter the number of rows: ";
    cin >> rows;
    
    printPyramid(rows);
    
    return 0;
}
