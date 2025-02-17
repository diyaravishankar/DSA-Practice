/*
struct Node
{
    int data;
    Node * next;
    Node * prev;
    Node (int x)
    {
        data=x;
        next=NULL;
        prev=NULL;
    }
        
};
*/

class Solution
{
public:

    Node * removeDuplicates(struct Node *head)
    {
        //if(!head or !head->next) return head;
        Node *nd = head;
        while(nd and nd->next) {
            Node *newnd = nd->next;
            while(newnd and nd->data == newnd->data) {
                Node *dup = newnd;
                newnd = newnd->next;
                free(dup);
            }
            nd->next = newnd;
            if(newnd)
            newnd->prev = nd;
            nd = nd->next;
        }
        return head;
        // Your code here
    }
};