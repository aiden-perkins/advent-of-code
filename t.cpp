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
    int p1_answer = part_1(input);
    int p2_answer = part_2(input);
    cout << "Part 1: " << p1_answer << endl;
    cout << "Part 2: " << p2_answer << endl;
    return 0;
}
