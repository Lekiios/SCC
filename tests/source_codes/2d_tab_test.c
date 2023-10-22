int main(){
    int vector;
    vector = malloc(2);
    int tab1;
    tab1 = malloc(2);
    tab1[0] = 1;
    tab1[1] = 0;
    int tab2;
    tab2 = malloc(2);
    tab2[0] = 0;
    tab2[1] = 1;

    vector[0] = tab1;
    vector[1] = tab2;

    print_num((vector[0])[0]);
    printl_num((vector[1])[0]);
    print_num((vector[0])[1]);
    printl_num((vector[1])[1]);
    return 0;
}

