/*

  Node is defined as
  struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/
class Solution {
    public:
      // Function to sort a linked list of 0s, 1s and 2s.
      Node* segregate(Node* head) {
          if(head==NULL || head->next==NULL){
              return head;
          }
          int zero=0,one=0,two=0;
       Node *temp=head;
       while(temp){
           if(temp->data==0){
               zero++;
           }
           else if(temp->data==1){
              one++;
           }
           else{
              two++;
           }
            temp=temp->next;
       }
       temp=head;
       while(temp){
           while(zero--){
               temp->data=0;
               temp=temp->next;
           }
           while(one--){
               temp->data=1;
               temp=temp->next;
           }
           while(two--){
               temp->data=2;
               temp=temp->next;
           }
           
       }
       return head;
      }
  };