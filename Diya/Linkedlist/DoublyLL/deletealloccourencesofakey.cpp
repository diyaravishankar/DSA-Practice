// User function Template for C++


/* a Node of the doubly linked list 
struct Node
{
  int data;
  struct Node *next;
  struct Node *prev;
  Node(int x) { data = x; next = prev = NULL; }
}; */

class Solution {
    public:
      void deleteAllOccurOfX(struct Node** head_ref, int x) {
          // Write your code here
          struct Node* curr = *head_ref;
          struct Node* prev = NULL;
          while(curr and curr->data == x) {
              *head_ref = curr->next;
              (*head_ref)->prev = prev;
              free(curr);
              curr = *head_ref;
          }
          while(curr){
              //if(curr->data == x)
              if(curr->data == x) {
                  struct Node* nd = curr->next;
                  prev->next = nd;
                  if(nd)
                  nd->prev = prev;
                  struct Node* temp = curr;
                  curr = curr->next;
                  free(temp);
                  
              }
              else{
                  prev = curr;
                  curr = curr->next;
              }
          }
          //return *head_ref;
      }
  };