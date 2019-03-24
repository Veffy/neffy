#include<bits/stdc++.h>
using namespace std;
int main(){
    long int a, b, temp, free_time=0, days=0;
    cin>>n>>k;
    for(int i=0; i<a; i++){
        cin >> temp;
        if(free_time < b){
            free_time += 86400-temp;
            days++;
        }
    }
    cout<<days;
    return 0;
}
