import time
def task_1(a):
    print("Let's start first task")
    yield "exercising"
    yield "reading a book"

def task_2(b):
    print("Let's start second task")
    yield "solving problems in leetcode"
    yield "playing computer games"

def task_3(a, b):
    print("Let's start the task 4")
    yield "Do homework"
    yield "revise past topics"

def test():
    yield task_1(2)
    yield task_2(2)
    yield task_3(2, 3)

for i in test():
    print("next")
    time.sleep(1)
    for j in i:
        time.sleep(1)
        print(j)
