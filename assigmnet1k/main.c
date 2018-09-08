
#include<stdio.h>
struct listnode
{
    char name;
    struct listnode *next
};
void enter();
void insert();
void deletion();
struct listnode **head;
void main()
{  int a;
   printf("want to enter names press 1");
   printf("want to insert name press 2");
   printf("want to delete name press 3");
   scanf("%d",&a);
   switch(a)
   {


        case 1:
          enter();
        case 2:
            insert();
        case 3:
             deletion();
        default :
            printf("wrong entry");
            return;
   }
}
void enter()
{
    int k;
    struct listnode *p,*q;
    do{
        printf("enter name");
        scanf("%s",p->name);
        q->next=p;
        *head=p;
        printf("if end, enter 0 or else enter 1");
        scanf("%d",&k);
    }while(k!=0);
    return;


}
void insert()
{
    int i,k=1;
    struct listnode *newnode,*p,*q;
    printf("enter position");
    scanf("%d",&i);
    if(i==1)
    {
        printf("enter name");
        scanf("%s",p->name);
        q=*head;
        p->next=q;
        *head=p;
            return;
    }
    else{
        while(p!=0&&k<i)
        {    k++;
            q=p;
            p=p->next;
        }
        printf("enter name");
        scanf("%s",newnode->name);
        q->next=newnode;
        newnode->next=p;
        return;
    }
}

    void deletion()
    {
        int i,k;
        struct listnode *p,*q;
        printf("enter position");
        scanf("%d",&k);
        p=*head;
        if((*head)==0)
        {
            printf("list empty");
            return;
        }
        if(k==1)
        {
            *head=(*head)->next;
            free(p);
            return;
        }
  else{
    while((p!=0)&&k<i)
    {   k++;
        q=p;
        p=p->next;
    }
    if(p==0)
    {
        printf("position does not exist ");
        return;
    }
    else
    {
        q->next=p->next;
        free(p);
        return;
    }
  }
}
