from xmlrpc.client import boolean

def fuction1(a,b,c,d,e,f):
    print(a);
    print(b);
    print(c);
    print(d);
    print("My hobbies are");
    print(e);
    print(f);

def fuction2(a):
    print(f"Love to do{a}")

def function3(a,b):
    list1=[a,b]
    return list1;

name=input("Enter your name")
age=int(input("Enter age"))
city=input("Enter city")
choice=bool(input("True if like coding else false"))
InfoDict={"Name": "Anshul","Age": "20","City": "Dehradun"};
InfoList=["football","beatboxing"]
tuple1=("Banana","Apple","Mango")
fuction1(name,age,choice,InfoDict,InfoList,tuple1)
fuction2(InfoList)
p=int(input("Enter a numbers for function3"))
q=int(input("Enter another number for function3"))
list2=function3(p,q)
print(f"List of function 3:{list2}") 
