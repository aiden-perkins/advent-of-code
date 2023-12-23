#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

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
    stringstream ss(input);
    string line;
    int total = 0;
    while (getline(ss, line, '\n')) {
        stringstream ss2(line);
        char ch;
        int dm[3];
        for (int & dimension : dm) {
            ss2 >> dimension;
            ss2 >> ch;
        }
        sort(dm, dm + 3);
        total += (dm[0] * dm[1] * 3) + (dm[1] * dm[2] * 2) + (dm[2] * dm[0] * 2);
    }
    return total;
}


int part_2(string &input) {
    stringstream ss(input);
    string line;
    int total = 0;
    while (getline(ss, line, '\n')) {
        stringstream ss2(line);
        char ch;
        int dm[3];
        for (int & dimension : dm) {
            ss2 >> dimension;
            ss2 >> ch;
        }
        sort(dm, dm + 3);
        total += (dm[0] * 2) + (dm[1] * 2) + (dm[0] * dm[1] * dm[2]);
    }
    return total;
}


int main() {
    string input = get_input();
    int p1_answer = part_1(input);
    int p2_answer = part_2(input);
    cout << "Part 1: " << p1_answer << endl;
    cout << "Part 2: " << p2_answer << endl;
    return 0;
}
