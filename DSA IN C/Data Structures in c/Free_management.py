from datetime import datetime as d

date = d.now().strftime("%y-%m-%d")
year = d.now().strftime("%y")
month = d.now().strftime("%m")
day = d.now().strftime("%d")


fee_data = {
    "student_id_1": {"name": "John", "fees": 200, "total_due": 0, "deposition_date": '01-12-24', "admission_date": '01-11-24'},
    "student_id_2": {"name": "Alice", "fees": 300, "total_due": 0, "deposition_date": '01-11-24', "admission_date": '01-10-24'},
}

def show():
    for key, val in fee_data.items():
        print(key,end=" : ")
        print(val)

def add():
    num = 1 + len(fee_data)
    ids = "student_id_" + str(num)
    name = input('Enter student name: ')
    fees = int(input('Enter student monthly fees: '))
    admission_date = d.now().strftime("%d-%m-%y")
    deposition_date = admission_date
    # total_due = 0
    fee_data[ids]={
        "name": name, 
        "fees": fees,
        "total_due": 0,
        "deposition_date": deposition_date,
        "admission_date": admission_date
        }
    show()
    print(f"student {name} is successfully added")

def delete():
    student_id = input("Enter student id number or name to remove: ")
    try:
        student_id = int(student_id)
        student_id = str(student_id)
        
        student_id = "student_id_" + student_id
        if student_id in fee_data:
            del fee_data[student_id]
        else:
            print(f"{student_id} doesn't exist")
    except ValueError:
        for key, val in fee_data.items():
            if val["name"]==student_id:
                del fee_data[key]
                return
        print(f"{student_id} doesn't exist")

def due_fees():
    current_year = int(year)
    current_month = int(month)
    current_day = int(day)
    for key, val in fee_data.items():
        name = val["name"]
        fees = val["fees"]
        deposition_date = val["deposition_date"]
        last_deposit_year = int(deposition_date.split("-")[2])
        last_deposit_month = int(deposition_date.split("-")[1])
        last_deposit_day = int(deposition_date.split("-")[0])
        
        months_due = (current_year - last_deposit_year) * 12 + (current_month - last_deposit_month)
        
        val["total_due"] = (months_due*fees)  + val["total_due"]
        # show()
        
        if current_day < last_deposit_day:
            months_due -= 1
        if months_due > 0:
            print("--------------------------------------------------")
            print(f"{name} owes fees for {months_due} month\nand due fee is ==> {val["total_due"]} \nfrom {deposition_date}.")
            
            print("--------------------------------------------------")
        else:
            print(f"{name} is up-to-date with fees.")

def deposit():
    name = input("Enter name to deposit fees for : ")
    amount = int(input("Enter amount of fees deposited : "))
    for key, val in fee_data.items():
        if val['name'] == name:
            if val["total_due"] > 0:
                val["total_due"] = val["total_due"] - amount
                # val['deposition_date']=
                print(f"Deposit of {amount} successfull to {val['name']}")
                break
            else:   
                print("No due found")
    
def main():
    while True:
        print("\n1. Add Student")
        print("2. Delete Student")
        print("3. Show Student")
        print("4. Due Fees")
        print("5. Deposit Fees")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add()
        elif choice == "2":
            delete()
        elif choice == "3":
            show()
        elif choice == "4":
            due_fees()
        elif choice == "5":
            deposit()
        elif choice == "6":
            break

main()