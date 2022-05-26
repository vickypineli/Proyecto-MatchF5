class Coder:
    def __init__(self, name, locations=[], skills=[], languages=[], prom=""):
        self.name = name
        self.locations = locations
        self.skills = skills
        self.languages = languages
        self.prom = prom

    def prom_and_name(self):
        return self.prom + " " + self.name
