n = int(input("Degree of the polynomial: "))
n_cof = []

for i in range(n + 1):
    n_cof.append(float(input(f"coefficient of the {abs(i-n)} power: ")))

new_n = n

def derivative(f, n):
    der = []
    new_n = n
    for i in range(len(f)):
        if f[i] != 0:
            der.append(f[i]* new_n)
        else:
            der.append(f[i])
        new_n-=1
    
    if der[-1] == 0:
        der.pop()
    return der, n-1 

def sign(x):
    if abs(x) == x:
        return 1
    else:
        return -1

def F(x, n, coff):
    y = 0
    for i in coff:
        y+= i * x ** n
        n-=1

    return y

def find_intervals(f, roots,n):

    intervals = []
    if n % 2 ==0:
        x1 = sign(f[0]) 
        x2 = x1 
        #edge case
        if sign(F(roots[0],n,f)) != x1:
            intervals.append([x1* float('inf'), roots[0]])


        for i in range(len(roots)-1):
            if sign(F(roots[i],n,f)) != sign(F(roots[i+1],n,f)) and F(roots[i],n,f) != 0 and F(roots[i+1],n,f) != 0:
                intervals.append([roots[i], roots[i+1]])

        if sign(F(roots[-1],n,f)) != x1:
            intervals.append([x1* float('inf'), roots[-1]])

    elif n % 2 !=0:
        x2 = sign(f[0])
        x1 = -1 * x2
        if sign(F(roots[0],n,f)) != x1:
            intervals.append([x1 * float('inf'), roots[0]])


        for i in range(len(roots)-1):
            if sign(F(roots[i],n,f)) != sign(F(roots[i+1],n,f)) and F(roots[i],n,f) != 0 and F(roots[i+1],n,f) != 0:
                intervals.append([roots[i], roots[i+1]])


        if sign(F(roots[-1],n,f)) != x2:
            intervals.append([x2 * float('inf'), roots[-1]])

    return intervals
    
def Newtons_method(f, interval, der,n,allinter):

    if float('-inf')in interval:
        if allinter.index(interval) == 0:
            point = interval[1] - 1
        else:
            point = interval[1] + 1
    elif float('inf')in interval:
        if allinter.index(interval) == 0:
            point = interval[1] - 1
        else:
            point = interval[1] + 1
    else:
        point = (interval[0] + interval[1])/2

    while abs(F(point,n,f)) > 0.00000005: #desired accuracy
        point -= F(point,n,f)/F(point,n-1,der)

    return point

f_list = []
f_list.append(n_cof)
while new_n>2:
    n_cof, new_n = derivative(n_cof, new_n)
    f_list.append(n_cof)

roots = []
delta = (n_cof[1]**2 - 4 * n_cof[0] * n_cof[2])
if delta >=0:
    roots.append((-1*n_cof[1] - delta**(1/2))/(2*n_cof[0]))
    roots.append((-1*n_cof[1] + delta**(1/2))/(2*n_cof[0]))
    roots.sort()
    
    for i in range(len(f_list)-1):
        new_n+=1
        intervals = find_intervals(f_list[-2-i],roots,new_n)
        points = []



        if F(0,new_n,f_list[-2-i])==0: #temporary fix, probably will cause incorrect results
            points.append(0)
            domainintervals = intervals
            if len(intervals) != 1:
                if domainintervals[0][0] == float('inf'):
                    domainintervals[0][0] = float('-inf')
                if domainintervals[-1][0] == float('-inf'):
                    domainintervals[-1][0] = float('inf')
                for j in domainintervals:
                    if j[0]<= 0 <= j[1] or j[0]>= 0 >= j[1]:

                        intervals.remove(j)
                        break



        for j in intervals:
            points.append(Newtons_method(f_list[-2-i],j,f_list[-1-i],new_n,intervals))
        roots = points
        roots.sort()

    print(roots)


else:
    print("NO QUADRATIC ROOTS, THE METHOD CANNOT BE IMPLEMENTED")  


