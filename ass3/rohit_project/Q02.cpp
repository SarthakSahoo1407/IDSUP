#include <iostream>
#include <string>

using namespace std;

class Account {
protected:
    string customerName;
    string accountNumber;
    string accountType;
    float balance;

public:
    Account(string customerName, string accountNumber, string accountType, float balance)
        : customerName(customerName), accountNumber(accountNumber), accountType(accountType), balance(balance) {}

    virtual void deposit(float amount) {
        balance += amount;
    }

    virtual void displayBalance() const {
        cout << "Account Balance: " << balance << endl;
    }

    virtual void computeInterest(float rate) {}

    virtual void withdraw(float amount) {}

    virtual void checkMinimumBalance(float minBalance, float serviceCharge) {}
};

class CurrentAccount : public Account {
private:
    float minBalance;
    float serviceCharge;

public:
    CurrentAccount(string customerName, string accountNumber, float balance, float minBalance, float serviceCharge)
        : Account(customerName, accountNumber, "Current Account", balance), minBalance(minBalance), serviceCharge(serviceCharge) {}

    void withdraw(float amount) override {
        if (balance - amount < minBalance) {
            cout << "Insufficient balance to withdraw." << endl;
            return;
        }
        balance -= amount;
    }

    void checkMinimumBalance(float minBalance, float serviceCharge) override {
        if (balance < minBalance) {
            cout << "Balance below minimum. Service charge applied." << endl;
            balance -= serviceCharge;
        }
    }
};

class SavingsAccount : public Account {
private:
    float interestRate;

public:
    SavingsAccount(string customerName, string accountNumber, float balance, float interestRate)
        : Account(customerName, accountNumber, "Savings Account", balance), interestRate(interestRate) {}

    void computeInterest(float rate) override {
        balance += (balance * rate / 100);
    }

    void withdraw(float amount) override {
        if (balance - amount < 0) {
            cout << "Insufficient balance to withdraw." << endl;
            return;
        }
        balance -= amount;
    }
};

int main() {
    CurrentAccount current("John Doe", "CA123", 1000.0, 500.0, 10.0);
    SavingsAccount savings("Jane Smith", "SA456", 2000.0, 5.0);

    current.displayBalance();
    current.deposit(500);
    current.displayBalance();
    current.withdraw(300);
    current.displayBalance();
    current.checkMinimumBalance(500.0, 10.0);
    current.displayBalance();

    savings.displayBalance();
    savings.deposit(1000);
    savings.displayBalance();
    savings.computeInterest(5.0);
    savings.displayBalance();
    savings.withdraw(500);
    savings.displayBalance();

    return 0;
}
