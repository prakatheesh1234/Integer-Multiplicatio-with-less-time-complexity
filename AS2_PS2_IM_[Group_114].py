import math

def multiply(x,y,file):
    
    sx= str(x)
    sy= str(y)
    nx= len(sx)
    ny= len(sy)
    if ny<=2 or nx<=2:
        r = int(x)*int(y)
        return r
    n = nx
    if nx>ny:
        sy = sy.rjust(nx,"0")
        n=nx
    elif ny>nx:
        sx = sx.rjust(ny,"0")
        n=ny
    m = n%2
    offset = 0
    if m != 0:
        n+=1
        offset = 1
    floor = int(math.floor(n/2)) - offset
    a = sx[0:floor]
    b = sx[floor:n]
    c = sy[0:floor]
    d = sy[floor:n]
    file.write("\n")

    file.write("Intermediate Values of A1, B1 after partition:")
    file.write("\n")

    file.write(" A : "+str(x))
    file.write(" A1 : "+str(a))
    file.write(" A2 : "+str(b))
    file.write("\n")
    file.write(" B : "+str(y))
    file.write(" B1 : "+str(c))
    file.write(" B2 : "+str(d))
    file.write("\n")
    
    
    
    
    print(a,b,c,d)

    ac = multiply(a,c,file)
    file.write("\n")

    file.write("Intermediate Values of A1, B1 after partition:")
    file.write("\n")

    file.write(" A : "+str(x))
    file.write(" A1 : "+str(a))
    file.write(" A2 : "+str(b))
    file.write("\n")
    file.write(" B : "+str(y))
    file.write(" B1 : "+str(c))
    file.write(" B2 : "+str(d))
    file.write("\n")
    bd = multiply(b,d,file)
   
    

    ad_bc = multiply((int(a)+int(b)),(int(c)+int(d)),file)-ac-bd
    
    r = ((10**n)*ac)+((10**(n/2))*ad_bc)+bd

    return r


f = open("./inputPS2.txt","r")
input_num=f.readlines()

file = open("outputPS2.txt", "w")
file.write("1st number : "+str(input_num[0].replace("\n","").strip()))
file.write("\n")
file.write("2nd number : "+str(input_num[1].replace("\n","").strip()))
file.write("\n")
file.write("--------------------------------------------- ")
file.write("\n")

#print(int(multiply(223245,123456 )))
file.write("Result ->"+str(input_num[0].replace("\n","").strip())+" * "+str(input_num[0].replace("\n","").strip())+" = ")
#+" = "+str(multiply(input_num[0].replace("\n","").strip(),input_num[1].replace("\n","").strip(),file)))
print(int(multiply(input_num[0].replace("\n","").strip(),input_num[1].replace("\n","").strip(),file)))

#print(int(multiply(4872349085723098457,597340985723098475)))
#
#print(int(multiply(4908347590823749,97098709870985)))
