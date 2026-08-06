# imports
import logging


# variables



# functions

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