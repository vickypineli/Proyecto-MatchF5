from src.domain.match import Match


def create_list_of_matches(coders, recruiters, number_of_meetings):
    matchs_list = []
    for coder in coders:
        for recruiter in recruiters:
            for meeting in range(number_of_meetings):
                match = Match(coder, recruiter, meeting)
                matchs_list.append(match)
    return matchs_list


def filter_by_location(list_of_matches):
    return [match for match in list_of_matches if match.is_same_location()]


def filter_by_skill(list_of_matches):

    return [match for match in list_of_matches if match.has_skill()]


def filter_by_languages(list_of_matches):

    return [match for match in list_of_matches if match.has_same_languages()]
