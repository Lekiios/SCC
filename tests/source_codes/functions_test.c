int add(int a, int b){
    return (a + b);
}

int sub(int a, int b){
    return (a - b);
}

int plusplus(int a){
    if(a == 0){
        return 1;
    }
    return plusplus(a-1)+1;
}

int main(){
    int a, b, c;
    a = 2; b = 4; c = 8;

    printl_num(plusplus(a));
    printl_num(add(a, plusplus(b)));
    printl_num(sub(c, b));

    return 0;
}

