int main(){
    int var;
    var = 10;
    {
        printl_num(var);
        int var;
        var = 5;
        {
            printl_num(var);
            int var;
            var = 2;
            printl_num(var);
        }
        printl_num(var);
    }
    printl_num(var);
    return 0;
}