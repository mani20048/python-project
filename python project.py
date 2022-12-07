date1=list(input('Enter the date1: ').split("/"))
date2=list(input('Enter the date2: ').split("/"))
s = []                                             # creating empty list
b = []
if int(date1[0])<=31 and int(date2[0])<=31:
    if int(date1[1])<=12 and int(date2[1])<=12:
        if int(date1[2])<int(date2[2]):
            if len(date1)<=3 and len(date2)<=3:
                for i in range(int(date1[2]),int(date2[2])+1):                    # loop for starting year to ending year
                    if i % 4 == 0:                                 # conditions for checking leap year or not
                        if i % 100 != 0:
                            s.append(i)                            # using append function to store value
                                                   # in the list
                        elif i % 100 == 0:
                            if i % 400 == 0:
                                s.append(i)

                            else:
                                b.append(i)
                    else:
                        b.append(i)
                print("leap years are:", s)                                            # printing leap years
                print("Non leap years are:", b)                    # printing non- leap years
    else:
        print('Enter the valid Date')
