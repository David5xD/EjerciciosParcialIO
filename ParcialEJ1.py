import pandas as pd
import numpy as np
import math as math
import sympy as sp

MM=9999
Colm=[]
Row=["Z"]
print("*****MÉTODO SIMPLEX********\n")

print("PARCIAL EJERCICIO #1 (Maximizar Ganancia de Productos)\n")
Mode=1
Urs=1
Sol=1
V=3
C=3

con=[]
Added=[]
ZZ=[]
Zeroline=["Z ="]
Printcc=[]
counter1=1
for i in range(0,C+1):
  if i==0:
    for k in range(1,V+1):
      if k==1:
        Z=6
      elif k==2:
        Z=5
      elif k==3:
        Z=4
      ZZ.append(Z)
      Colm=Colm+["x_"+str(counter1)]
      if Z>0:
        Zeroline.append("+"+str(Z)+" "+"x"+str(counter1))
      elif Z<0:
        Zeroline.append(str(Z)+" "+"x"+str(counter1))
      counter1=counter1+1
    ZZ.append(0)
    Added.append(ZZ)
  else:
    if Sol==2:
      if i==1:
        Type=1
      if i==2:
        Type=1
      if i==3:
        Type=1
      con.append(Type)
    else:
      Type=1
      con.append(Type)
    Addx=[]
    Printc=[]
    for j in range(0,V+1):
      if j==V:
        Xin = float(0)
        if i==1:
          Xin=180
        if i==2:
          Xin=300
        if i==3:
          Xin=240
        Addx.append(Xin)
        if Type==1:
          Printc.append("<="+str(Xin))
        elif Type==2:
          Printc.append("="+str(Xin))
        elif Type==3:
          Printc.append(">="+str(Xin))
      else:
        Xin = float(0)
        if i==1 and j==0:
          Xin=2
        if i==1 and j==1:
          Xin=1
        if i==1 and j==2:
          Xin=1
        if i==2 and j==0:
          Xin=1
        if i==2 and j==1:
          Xin=3
        if i==2 and j==2:
          Xin=2
        if i==3 and j==0:
          Xin=1
        if i==3 and j==1:
          Xin=2
        if i==3 and j==2:
          Xin=2

        Addx.append(Xin)
        if Xin<0:
          Printc.append(str(Xin)+" "+"x"+str(j+1))
        elif Xin>0:
          Printc.append("+"+str(Xin)+" "+"x"+str(j+1))
    Added.append(Addx)
    Printcc=Printcc+[Printc]
RHS=[]
for i in range(0,len(Added)):
  RHS.append(Added[i][-1])
  Added[i].pop(-1)
counter2=1
counter3=1
for i in range(1,len(con)+1):
  if con[i-1]==1:
    Row=Row+["S_"+str(counter2)]
    Colm=Colm+["s_"+str(counter2)]
    counter2=counter2+1
    for j in range(0,len(Added)):
      if j != i:
        Added[j].append(0)
      else:
        Added[j].append(1)

  elif con[i-1]==2:
    Colm=Colm+["R_"+str(counter3)]
    Row=Row+["R_"+str(counter3)]
    counter3=counter3+1
    for jj in range(0,len(Added)):
      if jj == 0:
        if Mode==1:
          Added[jj].append(-MM)
        elif Mode==2:
          Added[jj].append(MM)
      elif jj==i:
        Added[jj].append(1)
      elif (jj !=0 and jj !=i):
        Added[jj].append(0)
  elif con[i-1]==3:
    Colm=Colm+["s_"+str(counter2)]
    Colm=Colm+["R_"+str(counter3)]
    Row=Row+["R_"+str(counter3)]
    counter2=counter2+1
    counter3=counter3+1
    for jjj in range(0,len(Added)):
      if jjj==0:
        if Mode==1:
          Added[jjj].append(0)
          Added[jjj].append(-MM)
        elif Mode==2:
          Added[jjj].append(0)
          Added[jjj].append(MM)
      elif jjj==i:
        Added[jjj].append(-1)
        Added[jjj].append(1)
      elif (jjj != 0 and jjj != i):
        Added[jjj].append(0)
        Added[jjj].append(0)
for i in range(len(RHS)):
  Added[i].append(RHS[i])
Added=np.array(Added)

if Mode==1:
  Added[0]=-1*(Added[0])
Added=np.array(Added).tolist()
A=Added

#METODO DE SIMPLEX

if Sol==1:
  print("*-*-*-*-*-*-*-*(Problema)*-*-*-*-*-*-*")
  print(*Zeroline, sep=' ')
  print("Sujeto a:")
  for i in range(0,len(Printcc)):
    print(*Printcc[i], sep=' ')
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  A=np.array(A,dtype=float)

  print("------------------(Tabla: 1 )----------------")
  print(pd.DataFrame(A, index=Row,columns=Colm+["RHS"]))
  xz=2
  #___________________________________________________________________#
  MA=0
  while min(A[0,:-1])<0 or MA==1:
    if MA != 1:
      k=np.argmin(A[0,:-1])
    test=[]
    for i in range (1,A.shape[0]):
      if (A[i,k]<0) or (A[i,k]==0):
        test.append(math.inf)
        continue
      else:
        test.append(A[i,-1]/A[i,k])
    test=np.array(test)
    s=0
    for i in test:
      if i == min(test[0:]):
        s=s+1
    if s>1 and min(test)!= math.inf:
      print("***************(Tenemos degenerancia en esta tabla)*********************")
    elif min(test)==math.inf:
      print("***************(We are unbonded in This Table)************************")
      break
    n=np.argmin(test[0:])+1
    PashneRow  = np.divide(A[n], A[n][k])
    A=np.array(A).tolist()
    print("***************************")
    print(Colm[k],"Entra \t",Row[n],"Sale")
    print("***************************")
    Row[n]=Colm[k]
    for j in range(len(A)):
      Newrow=[]
      if j==n:
        A[n]  = np.divide(A[n], A[n][k])
        continue
      else:
        Newrow=PashneRow
        Newrow=Newrow*(-1)
        Newrow=Newrow*A[j][k]
        Newrow=list(Newrow)
        added=np.add(Newrow,A[j])
        A[j]=list(added)

    A=np.array(A,dtype=float)

    print("--------------- (Tabla:",xz,")------------------")
    print(pd.DataFrame(A, index=Row,columns=Colm+["RHS"]))
    xz=xz+1
    MA=0
    if Urs !=2:
      for i in range(0,V):
        if A[0][i]==0 and Colm[i] not in Row:
          k=i
          MA=1
          print("*****Tenemos multiples respuestas!!!!*****")
  Righth=round(A[0][-1],3)
  if Mode==1 and (min(test)!=math.inf):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("El valor optimo de Z es =",Righth)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  elif Mode==2 and (min(test)==math.inf):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("El valor optimo de Z es =",-1*Righth)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")