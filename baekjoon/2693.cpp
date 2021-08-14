#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int n = 0;
    cin >> n;
    
    for (int i = 0; i < n; i++)
    {
        vector<int> number(10);
        for (int j = 0; j < 10; j++)
            cin >> number[j];
        sort(number.begin(), number.end());
        cout << number[7] << endl;
    }
    
    return 0;
}