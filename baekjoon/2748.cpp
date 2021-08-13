#include <iostream> 

long long fibonacci(int x);

long long dp[91] = {0, 1, };

int main()
{
    int n = 0;
    std::cin >> n;    
    std::cout << fibonacci(n);
    
    return 0;
}

long long fibonacci(int x)
{
    if(x <= 1)
        return x;
    
    if(dp[x] == 0)
        dp[x] = fibonacci(x - 1) + fibonacci(x - 2);
    
    return dp[x];
}