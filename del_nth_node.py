
class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next
def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head
def print_list(head):
   ptr = head
   print('[', end = "")
   while ptr:
      print(ptr.val, end = ", ")
      ptr = ptr.next
   print(']')
class Solution(object):
   def removeNthFromEnd(self, head, n):
      if not head.next:
         return None
      front=head
      back = head
      counter = 0
      flag = False
      while counter<=n:
         if(not front):
            flag = True
            break
         front = front.next
         counter+=1
      while front:
         front = front.next
         back = back.next
      if not flag:
         temp = back.next
         back.next = temp.next
         temp.next = None
      else:
         head = head.next
      return head
head = make_list([1,2,3,4,5,6])
n=int(input("enter nth node:"))
ob1 = Solution()
print_list(ob1.removeNthFromEnd(head,n))