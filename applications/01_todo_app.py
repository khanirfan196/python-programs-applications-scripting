# imports
import logging


# variables

task = {}

# functions

def gen_task_key():
    task_key = len(task.keys())
    return task_key + 1

def create_task(task_val: str):
    task_key = gen_task_key()
    task.update({task_key: task_val})

def add_task():
    pass

def update_task():
    pass 

def delete_task():
    pass

def view_tasks():
    pass

if __name__ == "__main__":
    print("----- ToDo App ------")
    print("""
    Options -> \n
    01: View todos
    02: Add todos
    03: Update todos
    04: Delete todos
    """)
    try: 
        user_choice = int(input("Enter option: "))
    except Exception as e:
        print(f"Wrong input. Error - {e}")


    # test
    # print(gen_task_key())