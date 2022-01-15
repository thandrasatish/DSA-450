def reversearray(A,start,end):
    while(start <end):
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
    
A=list(map(int,input().split()))
reversearray(A,0,len(A)-1)
print(*A)


#INPUT:-
  #5 4 8 1 4
#OUTPUT:-
  #4 1 8 4 5
