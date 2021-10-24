from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'H_BeliefElicitation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    earnings_guess = models.IntegerField(
        min=0,
        label="1. We would like to know how much you think you would have earned if the Blue player’s performance had "
    "no impact on your earnings. Please express the amount in tokens, and type in numbers only:"
    )
    externality_guess = models.IntegerField(
        min=0,
        label="2. Now, we would like to know how much you think your matched Blue player reduced your earnings by. "
              "Please express the amount in tokens, and type in numbers only:"
    )
    externality_bool = models.IntegerField(
        label="",
        choices=[[1, "Yes"], [2, "No"]],
        widget=widgets.RadioSelect
    )


# PAGES
class ExtBeliefs_v1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.name == "victim1"

    form_model = "player"
    form_fields = ['earnings_guess', 'externality_guess']

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return "K_Attention_3"


class ExtBeliefs_v2_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.name == "victim2"
    form_model = "player"
    form_fields = ['externality_bool']

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.externality_bool == 2:
            return "K_Attention_3"


class ExtBeliefs_v2_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.name == "victim2" and player.externality_bool == 1
    form_model = "player"
    form_fields = ['earnings_guess', 'externality_guess']

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return "K_Attention_3"


page_sequence = [ExtBeliefs_v1, ExtBeliefs_v2_1, ExtBeliefs_v2_2]
