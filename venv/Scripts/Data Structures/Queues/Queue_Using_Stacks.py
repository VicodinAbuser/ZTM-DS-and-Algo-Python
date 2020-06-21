#This ia popular interview question. Implementation of a queue using stacks.
#We have access to stacks push and pop operations. Using those we need to execute a qeueue's enqueue and dequeue operation
#It can be done in two ways, by either making the enqueue operation costly(O(n)) or the dequeue operation costly(O(n))
#In the first method, we need two stacks say s1 and s2 and we have maintain them such that the element entered first
#Is always at the top of the stack s1. This way, for dequeue, we just need to pop from s1.
#But for enqueueing, we have to make the enqueued item reach the bottom of the stack.
#For that, we will have to pop the elements of s1 one by one and push them onto stack 2, then add the new item to stack1 ,
#And then again pop everything from stack2 and push it back to stack 1., so the new item is now at the last.

#Lets implement a queue using stacks(array implementation) using this method first

class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []


    def peek(self):
        if len(self.s1) == 0:
            print("Queue empty")
        else:
            return self.s1[len(self.s1)-1]


    def enqueue(self, data):
        for i in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)
        self.s1.append(data)
        for i in range(len(self.s2)):
            item = self.s2.pop()
            self.s1.append(item)
        return

    def dequeue(self):
        if len(self.s1)==0:
            print("Queue Empty")
            return
        else:
            return self.s1.pop()

    def print_queue(self):
        if len(self.s1) == 0:
            print("Queue Empty")
            return
        for i in range(len(self.s1) - 1,0,-1):
            print(f'{self.s1[i]} <<-- ',end='')
        print(self.s1[0])
        return


my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(5)
my_queue.enqueue(0)
my_queue.print_queue()
#2 <<-- 5 <<-- 0

my_queue.dequeue()
my_queue.print_queue()
#5 <<-- 0

print(my_queue.peek())
#5
my_queue.enqueue(9)
my_queue.print_queue()
#5 <<-- 0 <<-- 9

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
#Queue Empty


'''
For the second method, we can make the dequeue operation costly just like we did with the enqueue operation above.
For enqueueing, we will simply push in s1.
For dequeueing, we will pop all but last element of s1 and push it onto s2. Then we will pop the last element of s1,
Which is the element we want to dequeue. After that we pop out all items of s2 and push it back onto s1.
This makes the dequeue uperation O(n) while enqueue and peek remain O(1)
'''