from otree.api import *

doc = """
a.k.a. Encryption Game
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = "encrypt_practice"
    fixed_amount = 0.8
    letters_per_word = 5
    use_timeout = True
    seconds_per_entr = 120
    seconds_per_period = 120


class Subsession(BaseSubsession):
    dictionary = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    performance_entr = models.IntegerField(initial=0)
    mistakes_entr = models.IntegerField(initial=0)
    performance = models.IntegerField(initial=0)
    mistakes = models.IntegerField(initial=0)
    valeur = models.IntegerField(initial=0)
    bonus = models.IntegerField(initial=0)
    earnings = models.CurrencyField(initial=0)
    bonus_question = models.CurrencyField(initial=0)
    final = models.CurrencyField(initial=0)
    disp_ext = models.BooleanField()
    initial_ans = models.StringField(initial="")
    num_wrong = models.IntegerField(initial=0)
    q1 = models.IntegerField(
        label="This question is for checking your attention. Please select Disagree.",
        choices=[[1, "Disagree"], [2, "Somewhat Disagree"], [3, "Agree"], [4, "Somewhat Agree"]],
        widget=widgets.RadioSelect,
        blank=True,
        initial = 0
    )


# PAGES

class Example(Page):
    pass

class AttentionCheck(Page):
    form_model = 'player'
    form_fields = ["q1"]

    def before_next_page(player: Player, timeout_happened):
        if player.q1 !=1:
            player.participant.failedattentioncheck += 1


class FailedCheck(Page):
    def is_displayed(player: Player):
        return player.participant.failedattentioncheck >= 2

class RolesTokens(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"

class RoleTokensY1(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim1"

class YellowEarnings(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim1"

class TaskEntrainement(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = "player"
    form_fields = ["performance_entr", "mistakes_entr"]
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_entr

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {
            "legend_list": legend_list,
            "task_list": task_list,
            "task_width": task_width,
        }


class ResultsEntr(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    Example,
    TaskEntrainement,
    ResultsEntr,
    AttentionCheck,
    FailedCheck,
    RolesTokens,
    RoleTokensY1,
    YellowEarnings
]
