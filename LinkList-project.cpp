#include<iostream>
#include<iomanip>
#include<conio.h>


struct Polynomial {
    int coefficient;
    int exponent;
    Polynomial* next;
};

void Insert(Polynomial*& head, int coefficient, int exponent) {
    Polynomial* newTerm = new Polynomial;
    newTerm->coefficient = coefficient;
    newTerm->exponent = exponent;
    newTerm->next = head;
    head = newTerm;
}

void print(Polynomial* head) {
    while (head != NULL) {
        std :: cout << head->coefficient << "x^" << head->exponent;
        head = head->next;
        if (head != NULL)
            std::cout << " + ";
    }
    std :: cout <<"\n";
}
Polynomial* add(Polynomial* poly1, Polynomial* poly2) {
    Polynomial* result = NULL;

    while (poly1 != NULL || poly2 != NULL) {
        int coefficient1 = (poly1 != NULL) ? poly1->coefficient : 0;
        int exponent1 = (poly1 != NULL) ? poly1->exponent : 0;
        int coefficient2 = (poly2 != NULL) ? poly2->coefficient : 0;
        int exponent2 = (poly2 != NULL) ? poly2->exponent : 0;

        int sumCoefficient = coefficient1 + coefficient2;
        int sumExponent = std::max(exponent1, exponent2);

        Insert(result, sumCoefficient, sumExponent);

        if (poly1 != NULL) poly1 = poly1->next;
        if (poly2 != NULL) poly2 = poly2->next;
    }

    return result;
}

Polynomial* multiply(Polynomial* poly1, Polynomial* poly2) {
    Polynomial* result = NULL;

    while (poly1 != NULL) {
        Polynomial* current = poly2;
        Polynomial* tempResult = NULL;

        while (current != NULL) {
            int prodCoefficient = poly1->coefficient * current->coefficient;
            int prodExponent = poly1->exponent + current->exponent;

            Insert(tempResult, prodCoefficient, prodExponent);
            current = current->next;
        }

        result = add(result, tempResult);
        poly1 = poly1->next;
    }

    return result;
}

int main() {
	int a,b,c,d,e,f,g,h,i,j,k,l;
	std :: cout<<"enter your numbers:"<<"\n";
	std :: cin>>a>>b>>c>>d>>e>>f>>g>>h>>i>>j>>k>>l;
	getch();
	system("cls");
    Polynomial* poly1 = NULL;
    Polynomial* poly2 = NULL;

    Insert(poly1, a, b);
    Insert(poly1, c, d);
    Insert(poly1, e, f);

    Insert(poly2, g, h);
    Insert(poly2, i, j);
    Insert(poly2, k, l);

    std :: cout << "Polynomial 1: ";
    print(poly1);
    std :: cout << "Polynomial 2: ";
    print(poly2);


    Polynomial* sumResult = add(poly1, poly2);
    std :: cout << "Sum: ";
    print(sumResult);


    Polynomial* prodResult = multiply(poly1, poly2);
    std :: cout << "Product: ";
    print(prodResult);

    return 0;
    getch();
    system("cls");
}

