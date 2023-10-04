int init(){

}

int print_num(int n){
    if(n == 0){
        return 0;
    }
    print_num(n/10);
    send (n%10)+48;
}

int printl_num(int n){
    print_num(n);
    send 10;
}

int free(){}

int malloc(int n){
    int r = *0;
    *0 = *0+n;
    return r;
}