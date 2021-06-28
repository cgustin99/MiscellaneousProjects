#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

class Bank{

  public:
    std::string name;
    int balance;
    int amount;
    std::string password;

    Bank(){} //Default constructor
    Bank(std::string name, int balance, std::string password){
      this->name = name;
      this->balance = balance;
      this->password = password;
    }//Parameterized constructor
    void newAccount();
    void deposit(int amount);
    void withdraw(int amount);
    void inquireBalance();
    void printInfo();

};

void Bank::printInfo(){
  std::cout << "Name: " << name << "\n" << "Balance: " << balance << "\n"
    << "Password: " << password << std::endl;
}
void Bank::deposit(int amount){
  balance += amount;
}

void Bank::withdraw(int amount){
  balance -= amount;
}

void printChoices();
int getChoice();
std::string getName();
int getBalance();
std::string getPassword();

int main(){
  int numAccounts = 0;
  Bank* accounts = new Bank[100];

  while(true){
    printChoices();
    int currentChoice = getChoice();
    switch(currentChoice){
      case 1: {
        //Create New Account
        std::string thisName = getName();
        int thisBalance = getBalance();
        std::string thisPassword = getPassword();
        accounts[numAccounts++] = Bank(thisName, thisBalance, thisPassword);
        break;
      }
      case 2: {
        //Deposit Money
        std::string depositName = getName();
        int depositAmount;
        std::cout << "Amount to deposit: \n";
        std::cin >> depositAmount;
        std::string depositPassword = getPassword();

        for (int i = 0; i <= numAccounts; i++){
          if (accounts[i].name == depositName && accounts[i].password == depositPassword){
            std::cout << "Granted access" << std::endl;
            accounts[i].deposit(depositAmount);
          }
        }
        break;
      }
      case 3: {
        //withdraw
        std::string withdrawName = getName();
        int withdrawAmount;
        std::cout << "Amount to deposit: \n";
        std::cin >> withdrawAmount;
        std::string withdrawPassword = getPassword();

        for (int i = 0; i <= numAccounts; i++){
          if (accounts[i].name == withdrawName && accounts[i].password == withdrawPassword){
            std::cout << "Granted access" << std::endl;
            accounts[i].withdraw(withdrawAmount);
          }
        }
        break;
      }
      case 4: {
        //inquiry
        std::string inquireName = getName();
        std::string inquirePassword;
        std::cout << "Enter password:" << std::endl;
        std::getline(std::cin, inquirePassword);
        std::cout << "\n";

        for (int i = 0; i <= numAccounts; i++){
          if (accounts[i].name == inquireName && accounts[i].password == inquirePassword){
            std::cout << "Granted access" << std::endl;
            accounts[i].printInfo();
          }
        }
        break;
      }
      case 5: {
        std::exit(0);
        break;
      }
    }
  }


  return 0;
}

void printChoices(){

  std::cout << "========================" << std::endl;
  std::cout << " Bank Management System " << std:: endl;
  std::cout << "========================" << std::endl;
  std::cout << "1. New Account" << std::endl;
  std::cout << "2. Deposit Amount" << std::endl;
  std::cout << "3. Withdraw Amount" << std::endl;
  std::cout << "4. Balance Inquiry" << std::endl;
  std::cout << "5. Exit" << std::endl;

}

int getChoice(){
  int choice;
  std::cout << "Select a command (1-5): ";
  std::cin >> choice;

  return choice;
}

std::string getName(){
  std::string name;
  std::cout << "Enter name:" << std::endl;
  std::cin.ignore(256, '\n');
  std::getline(std::cin, name);
  return name;
}

std::string getPassword(){
  std::string password;
  std::cout << "Enter password:" << std::endl;
  std::cin.ignore(256, '\n');
  std::getline(std::cin, password);
  return password;
}

int getBalance(){
  int balance;
  std::cout << "Enter balance: \n";
  std::cin >> balance;
  return balance;
}
