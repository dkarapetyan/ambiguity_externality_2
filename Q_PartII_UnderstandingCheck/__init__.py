from otree.api import *

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'G_PartII_UnderstandingCheck'
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
        label="Your bonus payment is expected to be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    q2 = models.IntegerField(
        label="I will be paired with the same player I was paired with in Part 1.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    q3 = models.IntegerField(
        label="How many tokens will I earn for each word I encode correctly?",
        choices=[[1, "One"], [2, "Two"],[3, "Four"]],
        widget=widgets.RadioSelect
    )
    q4 = models.IntegerField(
        label="It is possible a yellow player's bonus payment may not be impacted by a blue player’s efforts in "
              "Part 2.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )


class UnderstandingCheck(Page):
    form_model = "player"
    form_fields = ["q1", "q2", "q3", "q4"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            q1=1,
            q2=2,
            q3=2,
            q4=1
        )

        error_messages = dict()

        for field_name in solutions:
            if len(player.initial_ans) < 6:
                player.initial_ans += str(values[field_name])
            if values[field_name] != solutions[field_name]:
                player.num_wrong += 1
                error_messages[field_name] = 'Wrong answer. Click "Back" to review the instructions and try again'

        return error_messages


page_sequence = [UnderstandingCheck]
