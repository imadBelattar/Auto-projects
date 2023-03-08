import graphyte


class User:
    user_number = 0

    def __init__(self, id_user, full_name):
        User.user_number += 1
        self.id_user = id_user
        self.full_name = full_name
        self.requests_counter = 0
        self.responses_time = 0
        self.requests_metric = self.full_name.split()[0] + "_requests_metric"
        self.responses_time_metric = self.full_name.split()[0] + "_responses_metric"
        if len(self.full_name.split()) == 2:
            self.folder = (
                f"{self.full_name.split()[0]}_{self.full_name.split()[1]}/"
            )
        else:
            self.folder = f"{self.full_name.split()[0]}/"

    def user_metrics(self):
        graphyte.send(
            self.folder + self.requests_metric,
            self.requests_counter,
        )
        self.requests_counter = 0
        graphyte.send(
            self.folder + self.responses_time_metric,
            self.responses_time,
        )
        self.responses_time = 0


# answers
yourOwner = [
    "'who is your owner'",
    "'who's your owner'",
    "'who's your developer'",
    "'who is your developer'",
    "'who's your creator'",
    "'who is your creator'",
    "'who is your owner?'",
    "'who's your owner?'",
    "'who's your developer?'",
    "'who is your developer?'",
    "'who's your creator?'",
    "'who is your creator?'",
    "'who is your owner ?'",
    "'who's your owner ?'",
    "'who's your developer ?'",
    "'who is your developer ?'",
    "'who's your creator ?'",
    "'who is your creator ?'",
]
aboutTheOwner = [
    "'who's imad belattar'",
    "'who's imad belattar?'",
    "'who's imad belattar ?'",
    "'who is imad belattar'",
    "'who is imad belattar?'",
    "'who is imad belattar ?'",
]
owner = "Imad Belattar is a Moroccan teenager who is passionate about programming and studying computer science. He was born on 02 January 2002 in Kelaa Sraghna. He is a very ambitious and patient person, and one of the best people I have ever met."
