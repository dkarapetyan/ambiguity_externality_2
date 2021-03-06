from otree.api import *

author = 'Your name here'

doc = """
attention check
"""


class Constants(BaseConstants):
    name_in_url = 'T_PartII_Attention'
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
        label="This question is for checking your attention. Please select Disagree.",
        choices=[[1, "Somewhat Disagree"], [2, "Agree"], [3, "Disagree"], [4, "Somewhat Agree"]],
        widget=widgets.RadioSelect,
        blank=True,
        initial = 0
    )


class AttentionCheck(Page):
    form_model = 'player'
    form_fields = ["q1"]

    def before_next_page(player: Player, timeout_happened):
        if player.q1 !=3:
            player.participant.failedattentioncheck += 1


class FailedCheck(Page):
    def is_displayed(player: Player):
        return player.participant.failedattentioncheck >= 2


page_sequence = [AttentionCheck, FailedCheck]
