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

def update_task(task_key, task_val):
    tasks.update({task_key: task_val}) 

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
        # View Tasks
        if user_choice == 1:
            view_tasks()
        # Add Tasks
        elif user_choice == 2:
            user_task = str(input("Add task: "))
            create_task(user_task)
            print("Task added.")
        # Update Tasks
        elif user_choice == 3:
            task_key = int(input(("Enter task key to update: ")))
            task_val = str(input("Enter task value to update: "))
            update_task(task_key, task_val)
        elif user_choice == 0:
            exit()


    # test
    # print(gen_task_key())