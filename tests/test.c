int main(){
    int tab;
    tab = malloc(8);
    tab[2] = 6;
    int a;
    a = 10;
    printl_num(&tab+2);
    printl_num(*a+3);
    return 0;
}
