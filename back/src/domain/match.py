class Match:
    def __init__(self, coder, recruiter, meeting_time):
        self.coder = coder
        self.recruiter = recruiter
        self.meeting_time = meeting_time
        # self.coincidence = self.calc_match()

    def is_same_location(self):
        for location in self.recruiter.location:
            if location in self.coder.location:
                return True
        return False

    def has_skill(self):
        for skill in self.recruiter.skills:
            if skill in self.coder.skills:
                return True
        return False

    def has_same_languages(self):
        for languages in self.recruiter.languages:
            if languages in self.coder.languages:
                return True
        return False

    # def calc_match(self):
    #     location_value = 0
    #     for location in self.coder.location:
    #         if location in self.recruiter.location:
    #             location_value = 0.5

    #     skills_coincidences = []
    #     for skill in self.coder.skills:
    #         if skill in self.recruiter.skills:
    #             skills_coincidences.append(skill)

    #     skills_value = len(skills_coincidences) / len(self.recruiter.skills) * 0.3

    #     languages_coincidences = []
    #     if self.recruiter. languages == []:
    #         languages_value = 0.2
    #     else:

    #     for language in self.coder.languages:

    #         if language in self.recruiter.languages:
    #             languages_coincidences.append(language)

    #     languages_value = (
    #         len(languages_coincidences) / len(self.recruiter.languages) * 0.2
    #     )

    #     return skills_value + languages_value + location_value
