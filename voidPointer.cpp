#include <iostream>
using namespace std;

void printNumber(int* numberPtr){
    cout << *numberPtr << endl;}
void printLetter(char* charPtr){
    cout << *charPtr << endl;}
void print(void* Ptr, char type){
    switch (type){
        case 'i':cout<< *((int*)Ptr)<< endl;break;
        case 'c':cout<< *((char*)Ptr)<< endl;break;
    }

}
int main(){
    int number = 5;
    char letter = 'a';
    // printNumber(&number);
    // printLetter(&letter);
    print(&number,'i');
    print(&letter,'c');

    system("pause>0");
    return 0;
}
// pointer must be same type as the variable int pointer hold int variable but there is exception of this rule a void pointer is a speial type of pointer that hold the address of any other type of variable
// https://youtu.be/kiUGf_Z08RQ?t=1528