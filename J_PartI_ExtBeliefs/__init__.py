from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'J_PartI_ExtBeliefs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    externality_guess = models.IntegerField(min=0, max=32, label="Between 0 and 32 tokens, how much do you think the " 
                                                  "blue player "
                                                  "decreased your earnings by?")


# PAGES
class ExtBeliefs(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim"

    form_model = "player"
    form_fields = ['externality_guess']


page_sequence = [ExtBeliefs]
