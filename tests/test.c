int add(int a){
    if(a >= 10){
        return a+1;
    }
    return add(a+2);
}

int main(){
    int a;
    a = 0;
    a = add(a);
    debug a;
    return 0;
}
