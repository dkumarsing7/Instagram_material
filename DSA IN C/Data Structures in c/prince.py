from datetime import datetime

date = datetime.now().strftime("%y-%m-%d")
year = datetime.now().strftime("%y")
month = datetime.now().strftime("%m")
day = datetime.now().strftime("%d")
records=[]

def add():
    stu_name=input("enter sudent name: ")
    if stu_name in records:
        print("student already exists!.")
        return
    stu_fee=input("fee of student: ")
    last_deposit=input("enter last deposit date(if not then enter): ")
    last_deposit = last_deposit.split("-")

    if not last_deposit:
        last_deposit=date
    records.append([stu_name,stu_fee,last_deposit])
    print(records)

def remove():
    stu_name=input("enter name to remove: ")
    for index,record in enumerate (records):
        if stu_name in record:
            if stu_name in record[0]:
                del(records[index])
                print(f"{stu_name} has been removed")
                return
        print(f"no student exixts in name of {stu_name}")            
        

def view_all():
    for record in records:
        print(" : ".join(record))   
    
def due():
    for record in records:
        if record[2][2] == day:
            due_yr = 
            print(f"student {record[0]} is due for payment")
            
            
    
    
    
def main():
    while True:
        choice =input("1.add\n2.remove\n3.view all\n4.check due\ntype exit to quit\n: ")

        if choice == "1":
            add()
        elif choice == "2":
            remove()
        elif choice == "3":
            view_all()
        elif choice == "4":
            due()
        elif choice == "exit":
            print("exiting")
            break 
    return    
        
main()