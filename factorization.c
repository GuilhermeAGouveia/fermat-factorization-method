#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
struct leaf {
    int value;
    struct leaf* lft;
    struct leaf* rgt;
};
struct leaf* factors = NULL;
 
void insert(struct leaf** tree, int value);
void print_tree(struct leaf* tree);
 
void fermat(int number);
 
int main(int argc, char* argv[])
{
    int num = atoi(argv[1]);
 
    fermat(num);
 
    print_tree(factors);
 
    return(0);
}
 
void insert(struct leaf** tree, int value)
{
    struct leaf* current = *tree;
 
    if(current == NULL)
    {
        struct leaf* new = malloc(sizeof(struct leaf));
        new->value = value;
        new->lft = NULL;
        new->rgt = NULL;
 
        *tree = new;
    }
 
    else
    {
        if(value < current->value)
            insert(&(current->lft), value);
        else
            insert(&(current->rgt), value);
    }
}
 
void print_tree(struct leaf* tree)
{
    struct leaf* current = tree;
 
    if(current!=NULL)
    {
        print_tree(current->lft);
        printf("%d ", current->value);
        print_tree(current->rgt);
    }
}
 
void fermat(int number)
{
    int r;
    short int is_prime = 1;
 
    while(number % 2 == 0)
    {
        number = number/2;
        insert(&factors,2);
    }
 
    if(number == 1)
        return;
 
    r = sqrt(number);
 
    while(r < (number+1)/2)
    {
        int m = (r*r) - number;
 
        if(m >= 0 && sqrt(m) == floor(sqrt(m)))
        {
            int s = sqrt(m);
 
            fermat(r - s);
            fermat(r + s);
 
            is_prime = 0;
            return;
        }
        r=r+1;
 
    } 
 
    if(is_prime == 1)
        insert(&factors,number);
}