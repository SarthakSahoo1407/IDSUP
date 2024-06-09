#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Staff {
protected:
    string code;
    string name;

public:
    Staff(string code, string name) : code(code), name(name) {}

    virtual void displayInfo() const {
        cout << "Code: " << code << ", Name: " << name;
    }
};

class Officer : public Staff {
private:
    string grade;

public:
    Officer(string code, string name, string grade) : Staff(code, name), grade(grade) {}

    void displayInfo() const override {
        Staff::displayInfo();
        cout << ", Grade: " << grade;
    }
};

class Teacher : public Staff {
private:
    string subject;
    string publication;

public:
    Teacher(string code, string name, string subject, string publication) : Staff(code, name), subject(subject), publication(publication) {}

    void displayInfo() const override {
        Staff::displayInfo();
        cout << ", Subject: " << subject << ", Publication: " << publication;
    }
};

class Typist : public Staff {
private:
    int speed;

public:
    Typist(string code, string name, int speed) : Staff(code, name), speed(speed) {}

    void displayInfo() const override {
        Staff::displayInfo();
        cout << ", Speed: " << speed;
    }
};

class CasualTypist : public Typist {
private:
    float dailyWages;

public:
    CasualTypist(string code, string name, int speed, float dailyWages) : Typist(code, name, speed), dailyWages(dailyWages) {}

    void displayInfo() const override {
        Typist::displayInfo();
        cout << ", Daily Wages: " << dailyWages;
    }
};


class RegularTypist : public Typist {
public:
    RegularTypist(string code, string name, int speed) : Typist(code, name, speed) {}
};

int main() {
    Officer officer("OF123", "John Doe", "Grade A");
    Teacher teacher("TCH456", "Jane Smith", "Mathematics", "Research Paper XYZ");
    CasualTypist casualTypist("CT789", "Alice Johnson", 80, 50.0);
    RegularTypist regularTypist("RT101", "Bob Williams", 100);

    cout << "Officer-> ";
    officer.displayInfo();
    cout << endl;

    cout << "Teacher-> ";
    teacher.displayInfo();
    cout << endl;

    cout << "Casual Typist-> ";
    casualTypist.displayInfo();
    cout << endl;

    cout << "Regular Typist-> ";
    regularTypist.displayInfo();
    cout << endl;

    return 0;
}
