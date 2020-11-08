def Merge(A, p, q, r):
    #print('p = ', str(p))
    #print('q = ', str(q))
    #print('r = ', str(r))
    
    #B = [0]*len(A)
    #b_index = 0
    B = []
    p -= 1
    #q -= 1
    #r -= 1
    left = p
    right = r
    middle = q
    middle_point = middle
    
    print(A)
    print(A[left:middle], A[middle:right])
        
    print('--sort-->> p=' + str(left) + ' q=' + str(middle) + ' r=' + str(right) + ' B:' + str(B))
        
    while(left < middle_point and middle < right):
        if(A[left] <= A[middle]):
            print('LEFT: ' + str(A[left]) + ' <= ' + str(A[middle]))
            B.append(A[left])
            #B[b_index] = A[left]
            #b_index += 1
            left += 1
            
        else:
            B.append(A[middle])
            print('RIGHT ' + str(A[left]) + ' > ' + str(A[middle]))
            #B[b_index] = A[middle]
            #b_index += 1
            middle += 1

    
    print('--sort-->> p=' + str(left) + ' q=' + str(middle) + ' r=' + str(right) + ' B:' + str(B))
    
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
    
    print('L:' + str(L) + ' R:' + str(R) + ' = ' + str(B) + ' L1 = ' + str(L1) + ' L2 = ' + str(L2) +  '\n')
    
    C = []
    for i in range(p, r):
        A[i] = B[i - p]
        print(i - p + 1)
#        A[i] = B[i - p - 1]
#        A[i] = B[i]
#        C.append(B[i - p - 1])
    print('A: ' + str(A))
    print('C: ' + str(C))
    print('B: ' + str(B))
    #print('\n')
        






def Sort(A, p, r):
    if(p < r):
        q = (p + r)//2
        print('p=' + str(p) + ' q=' + str(q) + ' r=' + str(r))
        Sort(A, p, q)
        Sort(A, q+1, r)
        #print("-------------")
        Merge(A, p, q, r)
        

def main():
    #print('\n')
    #print('\n')
    #A = [5,2,4,6,1,3,2,6]
    A = [5,2,4,6,1,3]
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
    print('\nМой:')
    print('A: ' + str(A))

    A.sort()
    print('\nМой сортированный:')
    print('A: ' + str(A))

    B.sort()
    print('\nСортированный:')
    print('A: ' + str(B))


if __name__ == "__main__":
        main()

