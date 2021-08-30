from otree.api import *

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'G_PartI_UnderstandingCheck'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    initial_ans = models.StringField(initial="")
    num_wrong = models.IntegerField(initial=0)
    q1 = models.IntegerField(
        label="What do you have to do in the encryption task?",
        choices=[[1, "Encode words into numbers"], [2, "Counting numbers in a line"],
                 [3, "Add a series of 2-digit numbers"]],
        widget=widgets.RadioSelect
    )
    q2 = models.IntegerField(
        label="Your earnings will be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    q3 = models.IntegerField(
        label="You are randomly and anonymously paired with a Blue player.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    q4 = models.IntegerField(
        label="How many tokens will you earn for each word you encrypt correctly? ",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    q5 = models.IntegerField(
        label="As the Blue player, how many tokens will you take away from the Yellow player for every word you "
              "encrypt correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    q6 = models.IntegerField(
        label="How many tokens will the blue player take away from you for each word they encrypt correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )


class YellowUnderstanding(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim1"

    form_model = "player"
    form_fields = ["q1", "q2", "q3", "q4", "q6"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            q1=1,
            q2=1,
            q3=1,
            q4=2,
            q6=1
        )

        error_messages = dict()

        for field_name in solutions:
            if len(player.initial_ans) < 6:
                player.initial_ans += str(values[field_name])
            if values[field_name] != solutions[field_name]:
                player.num_wrong += 1
                error_messages[field_name] = 'Wrong answer. Click "Back" to review the instructions and try again'

        return error_messages

class BlueUnderstanding(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"

    form_model = "player"
    form_fields = ["q1", "q2", "q3", "q4", "q5"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            q1=1,
            q2=1,
            q3=1,
            q4=2,
            q5=1,
            )

        error_messages = dict()

        for field_name in solutions:
            if len(player.initial_ans) < 6:
                player.initial_ans += str(values[field_name])
            if values[field_name] != solutions[field_name]:
                player.num_wrong += 1
                error_messages[field_name] = 'Wrong answer. Click "Back" to review the instructions and try again'

        return error_messages


page_sequence = [BlueUnderstanding, YellowUnderstanding]
