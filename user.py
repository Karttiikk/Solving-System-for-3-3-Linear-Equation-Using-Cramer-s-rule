#solving sysytem of 3*3 linera equation by using cramers rule
print("welcome to the project of \nTRACK 2 \nGROUP 5\n(NAAK)")
x1=int(input("enter x1"))
x2=int(input("enter x2"))
x3=int(input("enter x3"))
y1=int(input("enter y1"))
y2=int(input("enter y2"))
y3=int(input("enter y3"))
z1=int(input("enter z1"))
z2=int(input("enter z2"))
z3=int(input("enter z3"))
a1=int(input("enter a1"))
a2=int(input("enter a2"))
a3=int(input("enter a3"))
d=print( "d=  ",x1,y1,z1,"\n","\t",x2,y2,z2,"\n","\t",x3,y3,z3)
delta1=((y2*z3)-(z2*y3))
delta2=((x2*z3)-(z2*x3))
delta3=((x2*y3)-(y2*z3))
delta=delta1-delta2+delta3
print(delta)
deltax=print( "deltax=  ",a1,y1,z1,"\n","\t",a2,y2,z2,"\n","\t",a3,y3,z3)
b1=((y2*z3)-(z2*y3))
b2=((a2*z3)-(z2*a3))
b3=((a2*y3)-(y2*a3))
b=b1-b2+b3
print(b)
x=b/delta
deltay=print( "deltay=  ",x1,a1,z1,"\n","\t\t",x2,a2,z2,"\n","\t\t",x3,a3,z3)
c1=((a2*z3)-(z2*a3))
c2=((x2*z3)-(z2*x3))
c3=((x2*a3)-(a2*x3))
c=c1-c2+c3
print(c)
y=c/delta
deltaz=print( "deltaz=  ",x1,y1,a1,"\n","\t\t",x2,y2,a2,"\n","\t\t",x3,y3,a3)
e1=((y2*a3)-(a2*y3))
e2=((x2*a3)-(a2*x3))
e3=((x2*y3)-(y2*x3))
e=e1-e2+e3
print(e)
z=e/delta
print(x,y,z)


