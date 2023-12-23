#include <iostream>
#include <fstream>
#include <string>
using namespace std;


string get_input() {
    string input;
    string input_line;
    ifstream inputFile("./input.txt");
    if (inputFile.is_open()) {
        while (getline(inputFile, input_line)) {
            input += input_line;
        }
        inputFile.close();
    }
    return input;
}


int part_1(string &input) {
    int current_level = 0;
    for (int i = 0; i < input.length(); ++i) {
        if (input[i] == '(') {
            current_level++;
        } else {
            current_level--;
        }
    }
    return current_level;
}


int part_2(string &input) {
    int current_level = 0;
    int pos = 0;
    for (int i = 0; i < input.length(); ++i) {
        if (input[i] == '(') {
            current_level++;
        } else {
            current_level--;
        }
        if (current_level < 0) {
            pos = i + 1;
            break;
        }
    }
    return pos;
}


int main() {
    string input = get_input();
    int p1_answer = part_1(input);
    int p2_answer = part_2(input);
    cout << "Part 1: " << p1_answer << endl;
    cout << "Part 2: " << p2_answer << endl;
    return 0;
}
