from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'B_Consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(
        choices=[
            [1, "I consent"],
            [2, "I do not consent"]
        ]
    )


# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']


class BlockDropouts(Page):
    def is_displayed(player: Player):
        return player.consent == 2


page_sequence = [Consent, BlockDropouts]
