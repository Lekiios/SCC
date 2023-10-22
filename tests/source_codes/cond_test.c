int main(){
    int a, b, c;
    a = 2; b = 4; c = 8;

    if(a <= b && a*b == c){
        printl_num(0);
    }

    if(a > b || a*b == c){
        printl_num(1);
    }

    if(!(a > b && a*b == c)){
        printl_num(2);
    }

    if(!(a<b || c == 7) && a*b == c){
        printl_num(3);
    } else if(2*a != b){
        printl_num(31);
    } else {
        printl_num(32);
    }

    int d;
    d = a<b;

    if(d){
        printl_num(4);
    }

    return 0;
}
