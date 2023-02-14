class candidate:
    def __init__(self,name,marks,address,choices):
        self.name=name
        self.marks=marks
        self.address=address
        self.choices=choices
class location:
    def __init__(self,name,no):
        self.name=name
        self.no=no
def main():
    s=[]
    n=int(input("No of students: "))
    for i in range(n):
        name=input("Enter Student "+str(i+1)+" name: ")
        marks=int(input("Enter Marks: "))
        address=input("Enter the address: ")
        choices=list(map(str,input("Enter the Location choices with space separated: ").split()))
        s.append(candidate(name,marks,address,choices))
    n=int(input("Enter no of locations: "))
    locations=[]
    for i in range(n):
        name=input("Enter the "+str(i+1)+" location name :")
        k=int(input("Enter the no of vacancies: "))
        locations.append(location(name,k))
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i].marks<s[j].marks:
                s[i],s[j]=s[j],s[i]

    d={}
    for i in s:
        for j in i.choices:
            z=0
            for k in locations:
                if j==k.name and k.no>0:
                    d[i.name]=k.name
                    k.no-=1
                    z=1
                    break
            if z==1:
                break
    leftover=[]
    print("alloted locations are:")            
    print(d)
    print("left over locations:")
    for i in locations:
        print(i.name,i.no)
    print("left over candidates:")
    for each in s:
        if(each.name not in d):
           leftover.append(each.name)
    print(leftover)
main()
