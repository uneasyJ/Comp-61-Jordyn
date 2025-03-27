# class person :
#     def __init__(self, first_name, last_name, daily_salary,days_worked,money=0):
#         self.money=money
#         self.days_worked=days_worked
#         self.first_name=first_name
#         self.last_name=last_name
#         self.daily_salary=daily_salary
#         print(f'{self.first_name} {self.last_name} ${self.daily_salary} per day')
#         self.salary=self.days_worked*self.daily_salary
#         self.money+=self.salary
#         print(self.money)
   

# p1=person("shawn","lin",10,30)

##ANSWER for quiz

class person:
    def __init__(self, first_name, last_name, daily_salary,money=0):
        self.money=money
        self.first_name=first_name
        self.last_name=last_name
        self.daily_salary=daily_salary

    def work(self,days):
        salry=self.daily_salary*days
        self.money=self.money+salry

shawn=person("shawn",'lin',10)
ben=person("ben",'ben',20)

shawn.work(30)
ben.work(15)

if(shawn.money>ben.money):
    print('shawn has more money')
else:
    print('ben has more money')