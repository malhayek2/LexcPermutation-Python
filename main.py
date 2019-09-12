# name Mohanad ALhayek

#procedure next permutation(a1a2 . . . an: permutation of n
# Ex 12365
# -cacluate the target; left number less than right number. which is 3
# -the smallest of the biggest number on the right of it.(5)
# -swap them numbers the two numbers => 12563
# -order the rest the number from the samellest ot the biggest! ==> 12536

# just in case you dont like how python prints the list like [n,n1,n2...nn]
# hers a method that prints like n,n1,n2,n3...nn
def printList(elements):
    for i in range(len(elements)):
        if(i != len(elements)-1):
            print(elements[i], end=',')
        else:
            print(elements[i])
    



# swaps element[x] with element[y]
def swap(x,y,elements):
    if debug:
        print("swapping" , elements[x], "with" , elements[y])
    temp1 = elements[x]
    elements[x] = elements[y]
    elements[y] = temp1
# swaps the remaining from element[start+1] with the element[end] going right << 
def swapRemaining(start, elements):
    # start with the next element
    i = start + 1
    if debug:
        print("Order remaining, start swapping at " ,elements[start+1])
    # index pointer
    j = len(elements) - 1
    while(i < j):
        swap(i,j,elements)
        #next element
        i+=1
        #go back from last index
        j-=1
# magic
def generatePermuation(bitString):
    elements = []
    # creating list of n elements
    for x in range(bitString):
        elements.append(x+1)

    j = 0
    k = 0
    while(j != -1):
        j = -1
        
        # print(elements)
        printList(elements)
        # find the index of the number that is the target; left number less than right number.
        for i in range(len(elements)-1):
            if(elements[i] < elements[i+1]):
                j = i
                if debug:
                    print("Index of target", j ,"value of target" , elements[j])
            else:
                if debug:
                    print("could not find target.")
        #  find the index of the smallest of the biggest number on the right of j
        if(j != -1):
            for i in range(len(elements)):
                if(elements[j] < elements[i]):
                    k = i
                    if debug:
                        print("Index of smallest biggest on the right of the target", k ,"value" , elements[k])
            # we swap position of j with position of k in the list
            swap(j,k,elements)
            # swap the remaining elements in order the number from the samellest to the biggest! (ascending)
            swapRemaining(j,elements)
        
        


def main():
    ans=True
    if debug:
        print("debugging is ON")
    while ans:
        print ("""
        1.Get Permutations for bit String
        2.Generate Permutations for bit of length 4
        3.Exit/Quit
        """)
        choice=input("What would you like to do? ")
        if choice=="1":
            k = input('Enter the bit String length ')
            bitString = int(k)
            generatePermuation(bitString)
        elif choice=="2":
            generatePermuation(4)
        elif choice=="3":
            print("\n Goodbye")
            ans = False
        elif choice !="":
            print("\n Not Valid Choice Try again")
# flag, debugger
debug = False
main()