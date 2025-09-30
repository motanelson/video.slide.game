import time
print("\033c\033[43;30m\nboard\n")
def build(lena,incx,incy):
    x=0
    y=0
    t=0
    list1=[]
    for n in range(lena):
        
        l1=[x,y]
        list1=list1+[l1]
        x=x+incx
        y=y+incy
        
    return list1 
def mark(list1,array1,value,t):
    c=0
    for n in list1:
        
        xx=n[0]
        yy=n[1]
        
        array1[c][yy][xx]=value
        c=c+1    
    return array1
def draw(arrays,t):
    print("\033c\033[43;30m\n")
    a="0123456789ABCDEF"
    counts=0
    counts2=0
    print(" "+a)
    arrayss=arrays[t]
    for nn in range(len(arrayss)):
        print(a[counts2],end="")
        counts=0
        
        for n in range(len(arrays[t][nn])):
            i=arrays[t][nn][n]
            
            print(i,end="")
            counts=counts+1
        print((len(a)-counts)*" "+a[counts2])
        counts2=counts2+1
    print(" "+a)

def board():
    print("\033c\033[43;30m\n")
    a="0123456789ABCDEF"
    print(" "+a)
    for n in a:
        print(n+(" "*16)+n)
    print(" "+a)
def videoslides(x,y,t):
    # corrigido para evitar que todas as linhas sejam a mesma referência
    return [[[" " for _ in range(x)] for _ in range(y)] for _ in range(t)]


a=videoslides(15,15,8)
aaa=build(8,2,2)
#print(a)
a=mark(aaa,a,"X",8)
for n in range(8):
    draw(a,n)
    time.sleep(2)
