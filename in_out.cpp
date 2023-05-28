#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main()
{
    queue<int> queue;
    string name;
    cout << "hi" << endl;
    cin >> name;
    cout << "hello" << name << endl;

    return 0;
}

int main()
{
    std::string name, phone;
    int age;

    std::cout << "당신의 이름을 입력하세요: ";
    std::cin >> name;

    std::cout << "당신의 나이를 입력하세요: ";
    std::cin >> age;

    std::cout << "당신의 전화번호를 입력하세요: ";
    std::cin >> phone;

    std::cout << std::endl << "안녕하세요, " << name << "님." << std::endl;
    std::cout << "당신의 나이는 " << age << "살이고 "
        << "전화번호는 " << phone << "이군요!" << std::endl;
        return 0;
}