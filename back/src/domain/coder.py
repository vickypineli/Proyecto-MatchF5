class Coder:
    def __init__(self, name, locations=[], skills=[], languages=[], prom=""):
        self.name = name
        self.locations = locations
        self.skills = skills
        self.languages = languages
        self.prom = prom

    def prom_and_name(self):
        if self.name == "joker":
            return "-"
        return self.prom + " " + self.name
