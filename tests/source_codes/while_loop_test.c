int main(){
    int a, b, c;
    a = 2; b = 4; c = 8;
    int cpt;
    cpt = 0;

    while(a < b){
        printl_num(cpt);
        cpt = cpt + 1;
        if(b == c){
            break;
        }
        b = b + 1;
    }

    return 0;
}
