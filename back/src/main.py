from src.domain.match import Match


def create_list_of_matches(coders, recruiters, number_of_meetings):
    matchs_list = []
    for coder in coders:
        for recruiter in recruiters:
            for meeting in range(number_of_meetings):
                match = Match(coder, recruiter, meeting)
                matchs_list.append(match)
    return matchs_list
