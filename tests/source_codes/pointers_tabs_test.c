int main(){
    int a, b, c;
    int tab;
    tab = malloc(10);

    tab[0] = &c;

    b = 2;

    printl_num(*(tab[0]+1));
    tab = &c;
    tab[2] = 5;
    printl_num(a);

    return 0;
}

