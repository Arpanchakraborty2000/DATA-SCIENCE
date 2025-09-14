todo_list=["cleaning the house","wash the cloth","Pay bill"]

## Adding task 

todo_list.append("studdy")
todo_list.append("reading")


## Removing the element 

todo_list.remove("wash the cloth")

## check the task in this list or not 


if "Pay bill" in todo_list:
    print("PLZZZ pay the bill ...........")
    
    
    
print("print thr TO_DO list ")

for task in todo_list:
    print(f"-{task}")