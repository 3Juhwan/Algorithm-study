#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

string s1, s2;
int a, b, c;
int n1, n2;
int dp[3000][3000];


int score(int x, int y) {
    if (x == n1)
        return b * (n2-y);
    if (y == n2)
        return b * (n1-x);

    int &ret = dp[x][y];
    if (ret != -1)
        return ret;

    ret = max(b+score(x+1, y), b+score(x, y+1));
    int add = (s1[x] == s2[y]) ? a : c;
    ret = max(ret, add+score(x+1, y+1));

    return ret;
}


int main() {
	cin >> a >> b >> c;
	cin >> s1;
	cin >> s2;

	n1 = s1.length();
	n2 = s2.length();
	
	for (int i = 0; i < n1; i++)
        memset(dp[i], -1, sizeof(int)*n2);

	cout << score(0, 0);
}