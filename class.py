class programmer:
    company="google"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def info(self):
        print(f"the name of the {self.company} programmer is {self.name} and {self.product}")

ak=programmer("ak","you")
sam=programmer("sam","tube")
sam.info()
