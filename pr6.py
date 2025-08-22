name= input("Name :")
roll= input("Roll No :")

s1=float(input("mark of subject 1 :"))
s2=float(input("mark of subject 2 :"))
s3=float(input("mark of subject 3 :"))
s4=float(input("mark of subject 4 :"))
s5=float(input("mark of subject 5 :"))

total = s1+s2+s3+s4+s5
pr=(total/500)*100

print("\n---Marksheet---")
print("name",name)
print("roll no :", roll)
print("total:",total)
print("precentage:",pr)

if pr >= 90:
    print("grade: A+")

elif pr >=80:
    print("grade : A")

elif pr >=70:
    print("grade : B")
 
elif pr >=60:
    print("grade : C")

elif pr >=50:
    print("grade : D")

else:
    print("grade: F")

  
