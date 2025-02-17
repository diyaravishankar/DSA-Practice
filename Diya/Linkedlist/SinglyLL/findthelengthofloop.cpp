class Solution {
    public:
      // Function to find the length of a loop in the linked list.
      int countNodesinLoop(Node *head) {
          unordered_map<Node*,int> visitednodes;
          // Code here
          Node* temp=head;
          int count=0;
          while(temp!=NULL){
              if(visitednodes.find(temp)!=visitednodes.end()){
                  int looplen=count-visitednodes[temp];
                  return looplen;
              }
              visitednodes[temp]=count;
              temp=temp->next;
              count++;
          }
          return 0;
          
      }
};  