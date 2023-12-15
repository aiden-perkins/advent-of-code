#include <iostream>
#include <fstream>
using namespace std;


string get_input() {
    string input;
    string input_line;
    ifstream inputFile("./input.txt");
    if (inputFile.is_open()) {
        while (getline(inputFile, input_line)) {
            input += input_line + "\n";
        }
        inputFile.close();
    }
    return input;
}


int part_1(string &input) {
    return 0;
}


int part_2(string &input) {
    return 0;
}


int main() {
    string input = get_input();
    cout << part_1(input) << endl;
    cout << part_2(input) << endl;
    return 0;
}
