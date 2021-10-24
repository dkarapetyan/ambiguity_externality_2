from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'M_Dictator'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    transfer = models.IntegerField()
    endowment = models.IntegerField()


# PAGES
class Instructions(Page):
    def is_displayed(player: Player):
        return "victim" in player.participant.name


class Examples(Page):
    def is_displayed(player: Player):
        return "victim" in player.participant.name


class Offer(Page):
    def is_displayed(player: Player):
        return "victim" in player.participant.name

    form_model = 'player'
    form_fields = ['transfer']

    def before_next_page(player: Player, timeout_happened):
        if "victim" in player.participant.name:
            player.participant.dictator = 20 - player.transfer
        else:
            player.participant.dictator = 10


class Results(Page):
    pass


page_sequence = [Instructions, Examples, Offer, Results]
