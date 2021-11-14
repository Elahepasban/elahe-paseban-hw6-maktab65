class Tesk:
    def __init__(self, title, data, category, description, importance, clock_reminer, is_done=False):
        self.title = title
        self.data = data
        self.category = category
        self.description = description
        self.importance = importance
        self.clock_reminer = clock_reminer
        self.is_done = is_done

    def chek(self):
        if not self.is_done:
            self.is_done = True
            print(f"{self.title} {self.is_done}")
        else:
            print(":)")

    def __str__(self):
        return f'{self.title} is {self.is_done}'


task_list = []


def print_task():
    for i, task in enumerate(task_list):
        print(f"{i + 1} {task}")


def get_data():
    title, data, category, description, importance, clock_reminer = \
        input(" title, data, category, description, importance, clock_reminer:").split(",")
    task = Tesk(title, data, category, description, importance, clock_reminer)
    return task


while True:
    x = input("what would you like to do?")
    if x == "1":
        task_list.append(get_data())
    elif x == "2":
        print_task()
    elif x == "3":
        # print_task()
        index = int(input("enter yor number:"))
        Tesk.chek(task_list[index - 1])

# T1= Tesk("")
# print(T1.__str__())
# print(T1.chek())
