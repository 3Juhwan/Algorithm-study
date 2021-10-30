#include <iostream>

using namespace std;

int box[21];
bool f = 1;


int fillBox(int x, int y, int z) {
	if (!x || !y || !z) return 0;
	
    for (int i = 20; i >= 0; i--) {
        int n = 1 << i;
        if (box[i]) {
            if (n <= x && n <= y && n <= z) {
                box[i] -= 1;
                return 1 + fillBox(x, y-n, z) + fillBox(x, n, z-n) + fillBox(x-n, n, n);
            }
        }
    }
    
	f = 0;
	return -1;
}


int main() {
	int l, w, h, n;
    cin >> l >> w >> h;
	cin >> n;
	for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        box[a] = b;
	}
	
	int answer = fillBox(l, w, h);
    
	if (f) cout << answer;
	else cout << -1;
}