from otree.api import *


doc = """
a.k.a. Encryption Game
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = "encrypt_II"
    letters_per_word = 5
    use_timeout = True
    seconds_per_period = 480


class Subsession(BaseSubsession):
    dictionary = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    performance = models.IntegerField(initial=0)
    mistakes = models.IntegerField(initial=0)
    bonus = models.IntegerField(initial=0)
    earnings = models.CurrencyField(initial=0)
    bonus_question = models.CurrencyField(initial=0)
    final = models.CurrencyField(initial=0)
    tokens = models.IntegerField(initial=0)
    externality = models.IntegerField(
        label="Externality Choice",
        widget=widgets.RadioSelect,
        choices=[[1,
                  "I would like to earn <b>2 tokens for every word I encrypt, with 1 token taken away from the "
                  "earnings "
                  "of the yellow player I am paired with."],
                 [2,
                  "I would like to earn 1.5 tokens for every word I encrypt, with no tokens taken away from the "
                  "earnings of the yellow player I am paired with."]],
    )


# PAGES

class ExternalityChoice(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"

    form_model = "player"
    form_fields = ["externality"]

    def before_next_page(player: Player, timeout_happened):
        player.participant.externality_II = player.externality


class BeginEncryptionTask(Page):
    pass


class Task(Page):
    form_model = "player"
    form_fields = ["performance", "mistakes"]
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {
            "legend_list": legend_list,
            "task_list": task_list,
            "task_width": task_width,
        }


class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.tokens_II = 2*player.performance
        player.participant.performance_II = player.performance


class Results(Page):
    pass


page_sequence = [
    ExternalityChoice,
    BeginEncryptionTask,
    Task,
    Hidden,
    Results,
]
