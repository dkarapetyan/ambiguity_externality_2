from otree.api import *

author = 'Your name here'

doc = """
attention check
"""


class Constants(BaseConstants):
    name_in_url = 'B_Attention_1'
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
        label="This question is for checking your attention. Please select Agree.",
        choices=[[1, "Disagree"], [2, "Agree"], [3, "Somewhat Agree"], [4, "Somewhat Disagree"]],
        widget=widgets.RadioSelect,
        blank=True,
        initial=0
    )


class AttentionCheck(Page):
    form_model = 'player'
    form_fields = ["q1"]

    def before_next_page(player: Player, timeout_happened):
        player.participant.failedattentioncheck = 0
        if player.q1 != 2:
            player.participant.failedattentioncheck += 1


page_sequence = [AttentionCheck]
