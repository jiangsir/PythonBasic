from ListNode import ListNode

class Solution:

    def nodetoList(self, node):
        ll = []
        while node.next != None:
            ll.append(node.val)
        return ll

    def listtoNode(self, ll):
        
        ans = head = ListNode(-1)
        index = 0
        for i in range(len(ll)):
            head.next = ListNode(ll[i])
            head = head.next

        #print('listtoNode list=', ll , self.printNode(ans.next))
        return ans.next
            
    def printNode(self, node):
        #print("firt node = ", node)
        ans = ""
        while node != None:
            if node.next != None:
                ans += str(node.val) + "->"
            else:
                ans += str(node.val)
            node = node.next
        print('node=', ans)
        return ans
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.printNode(l1)
        self.printNode(l2)
        ans = head = ListNode(0)
        index = 0
        while l1 != None or l2!=None:
            #print('while 圈數: index=', index, l1.val, l1.next, l2.val, l2.next)
            index += 1
            if l1 !=None and l2 !=None:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                    continue
            else:
                if l1 != None:
                    head.next = l1
                    l1 = l1.next
                    continue
                    
                if l2 != None:
                    head.next = l2
                    l2 = l2.next
                    continue

        
#        ll1 = self.nodetoList(l1)
#        ll2 = self.nodetoList(l2)
#        l11.extend(ll2)

        self.printNode(ans.next)
        return ans.next

    
s = Solution()

#s.printNode(s.listtoNode([1, 2, 4]))

assert '1->1->2->3->4->4' == s.printNode(s.mergeTwoLists(s.listtoNode([1, 2, 4]), s.listtoNode([1, 3, 4])))
