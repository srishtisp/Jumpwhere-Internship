#Problem 206

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      
        prev = None 
        curr = head 


        while curr is not None:
            next_node = curr.next 
            
            curr.next = prev  
            
         
            prev = curr  
            curr = next_node  

       
        return prev