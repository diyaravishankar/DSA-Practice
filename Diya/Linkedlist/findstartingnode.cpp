#include <iostream>
using namespace std;
int main(){
    class Node{
        public:
            int data;
            Node* next;
        Node (int data; Node* next){
            this->data = data;
            this->next = next;
        }
        Node (int data1){
            this->data = data1;
            this->next = NULL;
        }
    };
    Node* firstnode(Node* head){
        Node* slow=head;
        Node* fast=head;
        while(fast!=Null && fast->next=Null){
            slow=slow->next;
            fast=fast->next->next;
            if(slow==fast){
                slow=head;
                while(slow!=fast){
                    slow=slow->next;
                    fast=fast->next->next;
                }
                return slow;
            }
        }
        return NULL;
       
    }
    int main(){
        Node* head = new Node(1);
        head->next = new Node(2);
        head->next->next = new Node(3);
        head->next->next->next = new Node(4);
        head->next->next->next->next = new Node(5);
        head->next->next->next->next->next = head;
        Node* result = firstnode(head);
        if(result!=NULL){
            cout << "Starting node is: " << result->data << endl;
        } else {
            cout << "No starting node found." << endl;
        }
        return 0;
    }

    

}