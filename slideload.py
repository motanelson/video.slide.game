import time
import zlib
def loads(texts):
    ll=True
    ti=0
    xi=0
    yi=0
    a=[]
    ttt=texts.split(";")
    ti=len(ttt)
    for t in range(ti):
        yyy=ttt[t].split("\n")
        yi=len(yyy)
        for y in range(yi):
            xxx=yyy[y].split(",")
            xi=len(xxx)
            if ll:
                a=videoslides(xi,yi,ti)
            ll=False
            for x in range(xi):
                 b=xxx[x].strip()
                 if b=="":
                     a[t][y][x]=" "
                 else:
                     a[t][y][x]=b
    return ti,yi,xi,a  
def save_compressed(filename, text):
    """Compacta a string e guarda no ficheiro com extensão .xytb"""
    compressed = zlib.compress(text.encode("utf-8"))
    with open(filename, "wb") as f:
        f.write(compressed)

def load_compressed(filename):
    """Carrega o ficheiro .xytb, descompacta e devolve a string"""
    with open(filename, "rb") as f:
        compressed = f.read()
    return zlib.decompress(compressed).decode("utf-8")
print("\033c\033[43;30m\nboard\n")
def memorys(arrays):
    ll=False
    aaa=""
    for n in arrays:
        if ll!=False:
             aaa=aaa+";"
        
        ll=True
        for nn in n:
             l=False
             for nnn in nn:
                 if l:
                     aaa=aaa+", "+str(nnn)
                 else:
                     aaa=aaa+str(nnn)
                 l=True
             aaa=aaa+"\n"
    return aaa
    

def saves(files,arrays):
    ll=False
    f1=open(files,"w")
    for n in arrays:
        if ll!=False:
             f1.write(";")
        
        ll=True
        for nn in n:
             l=False
             for nnn in nn:
                 if l:
                     f1.write(", "+str(nnn))
                 else:
                     f1.write(str(nnn))
                 l=True
             f1.write("\n")
    f1.close()
    
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
tt,yy,xx,a=loads(load_compressed("saida.xytb"))
for n in range(tt):
    draw(a,n)
    time.sleep(2)
