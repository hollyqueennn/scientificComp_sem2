import numpy as np

#membuat nilai matriks menjadi absolut semua
def absolut(x):
    for i in range (4):
        for j in range (4):
            if x[i][j] < 0:
                x[i][j]*=(-1)  
    return x

#menntukan diagonal dominance
def diagDominance(x):
    diag = []
    for i in range (4):
        diag.append(x[i][i])
        
    non_diag = []
    for i in range (4):
        summ = 0
        for j in range(4):
            summ+=x[i][j]
        summ -= diag[i]
        non_diag.append(summ)
        
    #setiap diag > non_diag
    dominant = True
    for i in range (4):
        if diag[i] <= non_diag[i]:
            dominant = False    
    return dominant

def iterasi(maks, x1, x2, x3, x4, e):
    converged = False
    k = 1
    x_old = np.array([x1, x2, x3, x4])
    
    while converged == False and k <= maks:
        x1 = (3 + (2*x2) + x3 + x4)/10
        x2 = (15 + (2*x1) + x3 + x4)/10
        x3 = (-9 + x1 + x2 - (10*x4))/(-2)
        x4 = (27 + x1 + x2 - (10*x3))/(-2)
        
        x_new = np.array([x1, x2, x3, x4])
        
        print("%d  %.4f  %.4f  %.4f  %.4f"%(k, x1, x2, x3, x4))
        
        #menghitung nilai error
        x = x_new - x_old
        x = np.dot(x, x)
        dx = np.sqrt(x)
        
        if dx <= e:
            converged = True
        
        x_old = x_new
        k+=1
        
    return x1, x2, x3, x4

#main function
#matriks
a = np.array([[10, -2, -1, -1],
             [-2, 10, -1, -1],
             [-1, -1, -2, 10],
             [-1, -1, 10, -2]])

a = absolut(a)

dominant = diagDominance(a)
print("Diagonal dominant:", dominant)

epsilon = float(input("Masukan nilai epsilon: "))
print("Masukan nilai tebakan awal")
x1 = float(input("x1: "))
x2 = float(input("x2: "))
x3 = float(input("x3: "))
x4 = float(input("x4: "))

maks_iterasi = int(input("Masukan nilai maksimal iterasi: "))

x1, x2, x3, x4 = iterasi(maks_iterasi, x1, x2, x3, x4, epsilon)

print(x1, x2, x3, x4)