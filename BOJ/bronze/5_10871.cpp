// https://www.acmicpc.net/problem/10871

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x;
    vector<int> arr(10000);
    vector<int> ans;
    cin >> n >> x;

    for(int i=0; i<n; i++){
        int temp;
        cin >> arr[i];
    }

    for(int i=0; i<n; i++){
        if(arr[i] < x){
            ans.push_back(arr[i]);
        }
    }

    for(int i=0; i<ans.size(); i++){
        cout << ans[i] << " ";
    }

     return 0;
}

int anothor_ans1(void){

    int n, x, a[100005];
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> x;
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i<n; i++)
        if(a[i] < x) cout << a[i] << " ";
}


int another_ans2(void){

    int n, x, t;
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> x;
    while(n--) {
        cin >> x;
        if(t < x) cout << t << ' ';
    }
    
    return 0;
}