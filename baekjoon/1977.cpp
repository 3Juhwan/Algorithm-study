#include <iostream> 

void getSolution(int m, int n);

void makeSquredNum();

int dp[10001] = {0, };

int main()
{
    int m = 0, n = 0;
    
    std::cin >> m >> n;    
   
    makeSquredNum();
    
    getSolution(m, n);
    
    return 0;
}

void makeSquredNum()
{
    for(int i = 1; i <= 100; i++)
    {
        dp[i*i] = 1;
    }
}

void getSolution(int m, int n)
{
    int sum = 0, mini = 10001;
    
    for(int i = m; i <= n; i++)
    {
        if(dp[i])
        {
            sum += i;
            mini = std::min(mini, i);
        }
    }
    
    if(sum == 0)
    {
        std::cout << -1 << '\n';
    }
    else
    {
        std::cout << sum << '\n';
        std::cout << mini;
    }
}