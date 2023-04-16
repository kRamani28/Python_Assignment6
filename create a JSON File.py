import json
{
    'name': 'Ravali',
    'dob': '22-9-1999',
    'height': '4.9',
    'city': 'Warangal',
    'state': 'Telangana'
}
{
    'name': 'Swetha',
    'dob': '12-7-1998',
    'height': '5.1',
    'city': 'Jangon',
    'state':'Telangana'
}
{
    'name': 'Priyanka',
    'dob': '21-8-2000',
    'height': '5.2',
    'city': 'Mahabubabad',
    'state': 'Telangana'
}
{
    'name': 'Rahul',
    'dob': '12-4-1998',
    'height': '5.0',
    'city': 'Karimnagar',
    'state': 'Telangana'
}
{
    'name': 'Ganesh',
    'dob': '2-9-1997',
    'height': '5.5',
    'city': 'Hydrabad',
    'state': 'Telangana'
}




# For creating a json file of 5 employees and print objects of Employee class in list-->
import json
class Employee:
    def __init__(self):
        self.emp_dic={}
    def creat_JSON(self):
        for i in range(5):
            name = input("Enter your name: ")
            dob = input("Enter your  DOB: ")
            height = input("Enter your height: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            emp={'name':name,'dob':dob,'height':height,'city':city,'state':state}
            emp_id = len(self.emp_dic)+1
            self.emp_dic[emp_id]=emp
        with open("emps.json","w") as f:
            json.dump(self.emp_dic,f)

    def data_print(self):
        with open("emps.json","r") as f:
            data = json.load(f)
        for i in data.values():
            l1 = []
            l1.append(i)
            print(l1)
x = Employee()
x.creat_JSON()
print("-----------------------------------------------")
x.data_print()

# output
# Enter your name: Ravali
# Enter your DOB: 22-9-1999
# Enter your height: 4.9
# Enter your city: Warangal 
# Enter your state: Telangana
# Enter your name: Swetha
# Enter your DOB: 12-7-1998
# Enter your height: 5.1
# Enter your city: Jangon
# Enter your state: Telangana
# Enter your name: Priyanka
# Enter your DOB: 21-8-2000
# Enter your height: 5.2
# Enter your city: Mahabubabad
# Enter your state: telangana
# Enter your name: Rahul
# Enter your DOB: 12-4-1998
# Enter your height: 5.0
# Enter your city: Karimnagar
# Enter your state: Telangana
# Enter your name: Ganesh
# Enter your height: 5.5
# Enter your city: Hydrabad
# Enter your state: Telangana
#-----------------------------------------------------------------------
# [{'name': 'Ravali', 'dob': '22-9-1999', 'height': '4.9', 'city': 'Warangal', 'state': 'Telangana'}]
# [{'name': 'Swetha', 'dob': '12-7-1998', 'height': '5.1', 'city': 'Jangon', 'state': 'Telangana'}] 
# [{'name': 'Priyanka', 'dob': '21-8-2000', 'height': '5.2','city': 'Mahabubabad', 'state': 'Telangana'}]
# [{'name': 'Rahul', 'dob': '12-4-1998', 'height': '5.0', 'city': 'Karimnagar', 'state': 'Telangana'}]
# [{'name': 'Ganesh', 'dob': '2-9-1997', 'height': '5.5', 'city': 'Hydrabad', 'state': 'Telangana'}]
