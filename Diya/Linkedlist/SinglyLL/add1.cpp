// User function template for C++

/*

struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};

*/

class Solution {
    public:
    Node* reverseLinkedList(Node* head) {
        Node* prev = NULL;
        Node* temp = head;
        while(temp != NULL) {
            Node* nextNode = temp->next;
            temp->next = prev;
            prev = temp;
            temp = nextNode;
        }
        return prev;
    }
  
    Node* addOne(Node* head) {
        head = reverseLinkedList(head);  // Reverse the list first
        Node* temp = head;
        int carry = 1; // Start with 1 (since we need to add 1)
        
        while(temp != NULL) {
          int sum = temp->data + carry;
          temp->data = sum%10;
          carry = sum/10;
          
          if(temp->next== NULL && carry > 0){
              temp->next = new Node(carry);
              carry = 0 ;
          }
          temp = temp->next;
        }
  
        return reverseLinkedList(head); // Reverse back before returning
    }
  };