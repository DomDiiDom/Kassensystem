class Logger():
    name = ""

    def __init__(self, name):
        self.name = name


    def info(self, message):
        print(f"[{self.name}][INFO] > {message}")