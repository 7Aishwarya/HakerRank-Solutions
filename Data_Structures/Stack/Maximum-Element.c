/* You have an empty sequence, and you will be given N queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack. 

Input Format
The first line of input contains an integer, . The next  lines each contain an above mentioned query. (It is guaranteed that each query is valid.)
Constraints
1<= n <= 10^5
1<= x <=10^9
1 <= type <= 3
Sample Input
10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output
26
91

*/



#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

long long int arr[100000];
long long int maxa[100000];
long long int max = 0;
int top = -1;
int maxtop = -1;

void push(long long int x){
    if(top<100000){
    top = top + 1;
    arr[top] = x;
    if(max<=x){
        max = x;
        maxtop = maxtop + 1;
        maxa[maxtop] = x;
    }
    }
}

void pop(){
    if(top>=0){
    if(maxa[maxtop] == arr[top]){
        maxtop = maxtop - 1;
        max = maxa[maxtop];
    }
    top = top - 1;
    }
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long long int n, x;
    int type;
    scanf("%lli", &n);
    for(int i = 0; i<n; i++){
        scanf("%d", &type);
        switch (type) {
            case 1: scanf("%lli", &x);
                    push(x);
                    break;
            case 2: pop();
                    break;
            case 3: printf("%lli\n", maxa[maxtop]);
                    break;
        }  
    } 
    return 0;
}
