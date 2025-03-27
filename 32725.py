# a_list=[1,3,4]
# b_list=[5,6,7]

# c_list=[a_list, b_list]
# d_list=[[1,2,3],
#         [4,5,6]]

# print(c_list[0][0])
import random
list=[]
class person:
    def __init__(self, first_name, last_name, daily_salary,money=0):
        self.money=money
        self.first_name=first_name
        self.last_name=last_name
        self.daily_salary=daily_salary
        self.salary_list=[]

    def work(self,days):
        salry=self.daily_salary*days
        self.money=self.money+salry

    def work_a_month(self):
        month=0
        while month<12:
            salary=self.daily_salary*30*random.random()
            self.salary_list.append(salary)
            month=month+1



shawn=person("shawn",'lin',10)
ben=person("ben",'ben',20)
bob=person("bob",'bob',15)
karen=person("karen",'karen',25)

shawn.work_a_month()
ben.work_a_month()
bob.work_a_month()
karen.work_a_month()

emply=[shawn.salary_list,ben.salary_list,bob.salary_list,karen.salary_list]

rich_person=None
month_most=0
for i in range(len(list)):
    for j in range (len(emply[i].salsry_list)):
        if (person.month_most>most_daily_salry):
            rich_person=person
            most_daily_salry=rich_person.daily_salary


# list.append(shawn.first_name)
# list.append(ben.first_name)
# list.append(bob.first_name)
# list.append(karen.first_name)

# shawn.work(30)
# ben.work(15)
# bob.work(10)
# karen.work(20)

# rich_person=None
# most_daily_salry=0
# for person in list:
#     if (person.daily_salary>most_daily_salry):
#         rich_person=person
#         most_daily_salry=rich_person.daily_salary

# # print(rich_person.first_name, rich_person.last_name)