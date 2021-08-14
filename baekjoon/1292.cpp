#include <iostream>
using namespace std;

int main()
{
    int a = 0, b = 0;
    cin >> a >> b;
    
    int dp[1001] = {0, };
    int now = 1, i = 0;
    while (i <= 1000)
    {
        for (int j = 0; j < now && i <= 1000; j++)
        {
            dp[i] = now;
            i++;
        }
        now += 1;
    }
    
    int total = 0;    
    for (int i = a - 1; i < b; i++)
        total += dp[i];
    
    cout << total << endl;
    
    return 0;
}