#include <iostream>
#include <string>
#include <algorithm>
#include <functional>

// Utility namespace to make the code look modular
namespace Utility {
    // Function to calculate factorial using recursion
    std::function<int(int)> factorial = [](int n) -> int {
        return (n <= 1) ? 1 : n * factorial(n - 1);
    };

    // Function to reverse a string
    std::string reverseString(const std::string& input) {
        std::string reversed = input;
        std::reverse(reversed.begin(), reversed.end());
        return reversed;
    }

    // Function to check if a string is a palindrome
    bool isPalindrome(const std::string& input) {
        std::string reversed = reverseString(input);
        return input == reversed;
    }
}

int main() {
    // Variables and input
    int number;
    std::string text;

    std::cout << "Enter a number to calculate its factorial: ";
    std::cin >> number;
    std::cout << "The factorial of " << number << " is: " << Utility::factorial(number) << "\n";

    std::cout << "\nEnter a string to check for palindrome: ";
    std::cin >> text;

    if (Utility::isPalindrome(text)) {
        std::cout << "\"" << text << "\" is a palindrome!\n";
    } else {
        std::cout << "\"" << text << "\" is not a palindrome.\n";
    }

    std::cout << "\nReversed string: " << Utility::reverseString(text) << "\n";

    return 0;
}