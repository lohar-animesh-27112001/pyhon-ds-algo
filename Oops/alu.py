# from math import cos
# from scipy.optimize import root


# class Person:
#     def __init__(self, height):
#         self.height = height
#         # height += 1
#         # print(f"{height} Maity")

#     def walk(self):
#         print("Person is walking")


# class Women(Person):
#     def __init__(self):
#         self.walk()


# alu = Women()


# def eqn(n):
#     return n[0] + 3*n[0]


# myroot = root(eqn, 4)
# print(myroot.x)
# print(myroot)

# --------------------------------------- Practice


def isPrime(n):
    for i in range(2, n):
        if (n % 2 == 0):
            return False
    else:
        return True


print(isPrime(10), isPrime(5))


def twice(n):
    n = n * 2


n = 10
twice(n)
print(n)
print(id(n))


def twiceArray(arr):
    for ind in range(0, len(arr)):
        arr[ind] = arr[ind] * 2


array = [1, 2, 3]
twiceArray(array)
print(array)
print(id(array))
print(id(array[0]))
print(id(array[1]))
print(id(array[2]))


def sum_Minus(n1, n2):
    return n1+n2, n1-n2


print(type(sum_Minus(30, 20)))
print(sum_Minus(20, 30).__doc__)
# ----------------------------------------------------------------------
month = []
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
total_ticket = []
year = []
c = 0
year_now = allticket[c]["year"]

while(c < len(allticket)):
    year_now = allticket[c]["year"]
    for i in months:
        if(c < len(allticket)):
            year_now = allticket[c]["year"]
            if(i == str(calendar.month_name[allticket[c]["month"]])):
                month.append(calendar.month_name[allticket[c]["month"]])
                total_ticket.append(allticket[c]["ticketcount"])
                year.append(allticket[c]["year"])
                c = c + 1
            else:
                month.append(i)
                total_ticket.append(0)
                year.append(year_now)
        else:
            month.append(i)
            total_ticket.append(0)
            year.append(year_now)
            
ticketcountInfo = []
for i in range (0, len(month)):
    ticketcountInfo.append([month[i],year[i],total_ticket[i]])
print(ticketcountInfo)

for i in months:
    if(c < len(allticket)):
        if(i == str(calendar.month_name[allticket[c]["month"]])):
            month.append(calendar.month_name[allticket[c]["month"]])
            total_ticket.append(allticket[c]["ticketcount"]])
            c = c + 1
        else:
            month.append(i)
            total_ticket.append(0)
    else:
        month.append(i)
        total_ticket.append(0)
        
allticket = SupportRequest.objects.annotate(year=ExtractYear("creationDate"), month=ExtractMonth("creationDate")).values("year", "month").annotate(ticketcount=Count ("id")).values("month", "ticketcount")