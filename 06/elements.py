class Identify():
    element = ""

    def melt(self):
        self.element = "water" if self.element == "snow" else\
            "solder" if self.element == "tin" else \
            "tungsten"
