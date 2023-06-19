print("welcome to college campus drive")
age=int(input("enter age"))
if(age>=18):
    experience=int(input("enter experience"))
    if(experience>1):
        education=input("enter education")
        if(education=="btech" or "mca" or "bca"):
            college=input("enter college")
            if(college=="rit","rce"):
                print("eligible for college campus drive")
            else:
                print("college not defined")
        else:
            print("education not up to marks")
    else:
        print("experience not matched")
else:
    print("age not defined")                        

