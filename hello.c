extern "C" void putss(char *c);
int main(){
    char c[]="\ec\e[43;37mhello world c++\n";
    putss(c);
    return 0;
}
