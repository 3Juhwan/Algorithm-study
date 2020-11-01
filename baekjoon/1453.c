#pragma warning (disable:4996)
#include <stdio.h>

int main(){
    int N = 0, seat = 0, cnt = 0;
    int arr[101] = {0};

    scanf("%d", &N);

    for(int i = 0; i < N; i++)
    {
        scanf("%d", &seat);

        if(!arr[seat])
            arr[seat] = 1;
        else
            cnt++;
    }

    printf("%d", cnt);

    return 0;
}