#quadratic formula: ax^2 + bx + c = 0
import cmath

a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

#calculate the discriminant
D =  (b**2) -  (4*a*c)
if D > 0:
    sol1 = (-b + cmath.sqrt(D))/(2*a)
    sol2 = (-b - cmath.sqrt(D))/(2*a)  
    print(f"the naswer is{sol1} , {sol2} ")
elif D == 0:
    sol = (-b)/(2*a)
    print(f"The answer is{sol} ")
else:
    print("There are no real solutions(imaginary)")
    