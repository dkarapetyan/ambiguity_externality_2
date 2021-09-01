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

    transfer = models.IntegerField(
        doc="""Amount dictator transferred""",
    )
    endowment = models.IntegerField()


# PAGES
class Introduction(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim2"


class Instructions(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim2"


class Offer(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim2"

    form_model = 'player'
    form_fields = ['transfer']

    def before_next_page(player: Player, timeout_happened):
        if player.session.config['name'] == "victim2":
            player.participant.dictator_II = 30 - player.transfer
        else:
            player.participant.dictator_II = 15


class Results(Page):
    pass


page_sequence = [Introduction, Instructions, Offer, Results]
