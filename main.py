
# 4-m
class Xodim:
    def __init__(self, ism , maosh):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Maosh: {self.maosh}")


class Dasturchi(Xodim):
    def __init__(self, ism, maosh, til):
        super().__init__(ism, maosh)
        self.til = til


    def malumot(self):
        super().malumot()
        print(f"Til: {self.til}")

x = Dasturchi("Bunyod", 0, 'uzbek')
x.malumot()


