# Given a linked list with string data, check whether the combined string 
# formed is palindrome. If the combined string is palindrome then 
# return true otherwise return false.


#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
    str = ''
    while(head is not None):
        str = str + head.data
        head = head.next
    
    if str == str[::-1]:
        return True
    
    else:
        return False




#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n1 = int(input())
        arr1 = input().split()
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        if compute(ll1.head):
            print('true')
        else:
            print('false')

# } Driver Code Ends