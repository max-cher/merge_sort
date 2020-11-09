from random import randint


def Merge(A, p, q, r):
    
    #B = [0]*len(A)
    #b_index = 0
    B = []
    p -= 1
    left = p
    right = r
    middle = q
    middle_point = middle
        
    while(left < middle_point and middle < right):
        if(A[left] <= A[middle]):
            B.append(A[left])
            #B[b_index] = A[left]
            #b_index += 1
            left += 1
            
        else:
            B.append(A[middle])
            #B[b_index] = A[middle]
            #b_index += 1
            middle += 1

    L = []
    while(left < middle_point):
        L.append(A[left])
        B.append(A[left])
        #B[b_index] = A[left]
        #b_index += 1
        left += 1
    
    R = []
    while(middle < right):
        R.append(A[middle])
        B.append(A[middle])
        #B[b_index] = A[middle]
        #b_index += 1
        middle += 1
        
    L1 = []
    L2 = []
    for i in range(p, q):
        L1.append(A[i])
    for i in range(q, r):
        L2.append(A[i])
    
    C = []
    for i in range(p, r):
        A[i] = B[i - p]


def Sort(A, p, r):
    if(p < r):
        q = (p + r)//2
        Sort(A, p, q)
        Sort(A, q+1, r)
        Merge(A, p, q, r)


def main():
    #print('\n')
    #print('\n')
    #A = [5,2,4,6,1,3,2,6]
    #A = [5,2,4,6,1,3]
    A = []
    for i in range(10000):
        A.append(randint(0, 99))
    #A = [1, 3, 5, 7, 2, 4, 6, 8]
    B = []
    for i in A:
        B.append(i)
#    print((len(A) - 1)//2)
    #p = 1
    #r = len(A)
    #q = (p + r)//2
    #Merge(A, p, q, r)

    #print('\nИсходный:')
    #print('A: ' + str(A))

    Sort(A,1,len(A))
    #print('\nМой:')
    #print('A: ' + str(A))

    #A.sort()
    #print('\nМой сортированный:')
    #print('A: ' + str(A))

    B.sort()
    #print('\nСортированный:')
    #print('A: ' + str(B))
    for i in B:
        if B[i] != A[i]:
            print('sort fail! exit')
            return
    print('sotr pass!')

if __name__ == "__main__":
        main()

