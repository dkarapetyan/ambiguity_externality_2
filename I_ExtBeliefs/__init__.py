from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'I_ExtBeliefs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    earnings_guess = models.IntegerField(min=0, max=64,label="We would like to know how much you think you would have earned if the Blue player’s performance had no impact on your earnings. "
                                                            "Please express the amount in tokens:")
    externality_guess = models.IntegerField(min=0, max=32, label="Now, we would like to know how much you think your matched Blue player reduced your earnings by. "
                                                                 "Please express the amount in tokens:")


# PAGES
class ExtBeliefs(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim1"

    form_model = "player"
    form_fields = ['earnings_guess', 'externality_guess']


page_sequence = [ExtBeliefs]
