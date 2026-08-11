# imports
import logging


# variables

tasks = {}

# functions

def gen_task_key():
    task_key = len(tasks.keys())
    return task_key + 1

def create_task(task_val: str):
    task_key = gen_task_key()
    tasks.update({task_key: task_val})

def add_task():
    pass

def update_task():
    pass 

def delete_task():
    pass

def view_tasks():
    for k, v in tasks.items():
        print("Task No: ",k, " : ", v)

if __name__ == "__main__":
    print("----- ToDo App ------")
    print("""
    Options -> \n
    01: View todos
    02: Add todos
    03: Update todos
    04: Delete todos
    """)

    while True:
        try: 
            user_choice = int(input("Enter choice: "))
        except Exception as e:
            print(f"Wrong input. Error - {e}")
        if user_choice == 1:
            print(view_tasks())
        elif user_choice == 2:
            user_task = str(input("Enter task: "))
            create_task(user_task)
            print("Task added.")
        elif user_choice == 0:
            exit()


    # test
    # print(gen_task_key())