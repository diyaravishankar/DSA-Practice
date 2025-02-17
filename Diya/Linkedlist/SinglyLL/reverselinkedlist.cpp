#include <stdio.h>
using namespace std;
class Node{
    public: 
    int data;
    int* Node;
    Node (int data1,Node* next){
        data1=data;
        next=next;

    }
    Node(int data1){
        data1=data;
        next=NULL;
    }

};
Node* reverse(Node* head){
    Node* prev=Null;
    Node* curr=head;
    Node* temp=NULL;
    while(curr!=NULL){
        temp=curr->next;
        curr->next=prev;
        prev=curr;
        curr=prev;
    }
    return prev;
}

int main(){
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);
    head->next->next->next->next->next = head;
    Node* result = reverse(head);
    if(result!=NULL){
        cout << "Reversed list is: " << result->data << endl;
    } else {
        cout << "No starting node found." << endl;
    }
    return 0;
}