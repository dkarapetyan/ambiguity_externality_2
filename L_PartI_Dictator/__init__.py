from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'L_PartI_Dictator'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    transfer = models.CurrencyField(
        #choices=[0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4, -.5, -1, -1.5, -2],
        doc="""Amount dictator transferred""",
    )
    endowment = models.CurrencyField()


# PAGES
class Introduction(Page):
    pass


class Instructions(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim"


class Offer(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim"

    form_model = 'player'
    form_fields = ['transfer']

    def before_next_page(player: Player, timeout_happened):
        if player.session.config['name'] == "victim":
            player.participant.dictator_I = cu(4) - player.transfer
        else:
            player.participant.dictator_I = cu(2)


class Results(Page):
    pass


page_sequence = [Introduction, Instructions, Offer, Results]
