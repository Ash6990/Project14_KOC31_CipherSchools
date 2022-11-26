
dict1={"Kai":6307892445,"Ray":4563782913,"Max":3747585919,"Tyson":4573829503,"Kenny": 8789667232,"Glenn":6782919356,"Carl":4563728395,"Rick":4676859383}
print("-----------------------------------------------------------------------")
print("                     WELCOME TO THE CLASS REPOSITORY                   ")
print("-----------------------------------------------------------------------")
print("What do you want to do?","\n 1.Search a Contact number","\n 2.Display all contacts with names","\n 3.Fetch the contact number of multiple students","\n 4.Update record")
c=int(input("Enter your choice: "))
m=list(dict1.items())
if c ==1:
    n=input("Enter the name of the student: ")
    
    if n=="Kai":
        print(m[0])
    elif n=="Ray":
        print(m[1])
    elif n=="Max":
        print(m[2])
    elif n=="Tyson":
        print(m[3])
    elif n=="Kenny":
        print(m[4])
    else:
        print("Record not found")
elif c==2:
    print(dict1,sep="\n")
elif c==3:
    a=int(input("Enter no.of contacts to be fetched: "))
    if a>len(m):
        print("value exceded")
    else:    
        b=[input("Enter the name to fetch contacts: ")for _ in range (a)]
        tu=[]
        for k in b:
            tu.append(dict1.get(k))
        print(tu)    
else:
    
    e=input("Enter name of the student: ")
    f=int(input("Enter the contact number: "))
    dict1.update({e:f})
    print("Repoitory updated",dict1)
    








































