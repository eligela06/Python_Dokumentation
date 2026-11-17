class Task:
    total_executions = 0

    def __init__(self, name):
        self.name = name
        self.executions = 0

    def __str__(self):
        return f"{self.name} ({self.executions} executions)"

    def execute(self):
        self.executions += 1
        Task.total_executions += 1


class PrintTask(Task):
    def __init__(self, name, message):
        super().__init__(name)
        self.message = message

    def execute(self):
        print(self.message)
        super().execute()


class CounterTask(Task):
    def __init__(self, name, start, step):
        super().__init__(name)
        self.value = start
        self.step = step

    def execute(self):
        self.value += self.step
        print(self.value)
        super().execute()


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            task.execute()

    def run_times(self, n):
        for _ in range(n):
            self.run()

    def __len__(self):
        return len(self.tasks)


class DependentTask(Task):
    def __init__(self, name, dependency, message):
        super().__init__(name)
        self.message = message
        self.dependency = dependency

    def execute(self):
        if self.dependency.executions == 0:
            print("Waiting for dependency")
            return

        print(self.message)
        super().execute()


# task1 = PrintTask("Greeting", "Hello!")
# task2 = CounterTask("Counter A", 10, 2)

# scheduler = Scheduler()

# scheduler.add(task1)
# scheduler.add(task2)

# scheduler.run()
# # Hello!
# # 12

# scheduler.run_times(2)
# # Hello!
# # 14
# # Hello!
# # 16

# print(task1)
# # Greeting (3 executions)

# print(task2.value)           # 16
# print(Task.total_executions) # 6