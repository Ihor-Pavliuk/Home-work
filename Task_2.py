def outside_func():
    def inside_func():
        return "Привіт з середини функції"
    return inside_func
task_2 = outside_func()
print(task_2())
