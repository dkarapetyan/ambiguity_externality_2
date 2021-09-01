from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.05,
    'participation_fee': 3.75,
    'doc': "",
}
PARTICIPANT_FIELDS = ['nettokens',
                      'externality1',
                      'externality2',
                      'externality3',
                      'ext_choice',
                      'payoff_final',
                      'payoff_ext',
                      'payoff_noext',
                      'payoff_choice',
                      'performance1',
                      'performance2',
                      'performance3',
                      'performance_final',
                      'dictator',
                      'random_part',
                      'failedattentioncheck',
                      'bluematch',
                      'v2_treatment'
                      ]

SESSION_CONFIGS = [
    dict(
        name='victim1',
        display_name="Session Y1",
        num_demo_participants=1,
        completionlink="http://www.prolific.co",
        app_sequence=[#'A_ExperimentIntro',
                      #'B_Attention_1',
                      #'C_GenInstructions_1',
                      #'D_EncryptPractice',
                      #'E_Attention_2',
                      #'F_PlayerRoles',
                      #'G_UnderstandingCheck_1',
                      'G_EncryptTask_1',
                      'H_BeliefElicitation',
                      #'I_PartI_RevealEarnings',
                      #'H_BeliefElicitation',
                      #'K_Attention_3',
                      #'L_Treatment',
                      #'L_PartI_Dictator',
                      #'M_PartI_Fairness',
                      #'O_ExperimentEnd',
                      #'X_Exit'
                      ],
    ),
    dict(
        name='victim2',
        display_name="Session Y2",
        num_demo_participants=1,
        completionlink="http://www.prolific.co",
        app_sequence=['A_ExperimentIntro',
                      #'B_Attention_1',
                      #'C_GenInstructions_1',
                      #'D_EncryptPractice',
                      #'E_Attention_2',
                      #'F_PlayerRoles',
                      'G_EncryptTask_1',
                      'H_BeliefElicitation',
                      #'P_PartII_EncryptPractice',
                      #'Q_PartII_UnderstandingCheck',
                      #'R_PartII_EncryptionTask',
                      #'R_PartII_RevealEarnings',
                      #'S_PartII_ExtBeliefs',
                      #'T_PartII_Attention',
                      #'T_PartII_Treatments',
                      #'M_Dictator',
                      #'N_Fairness',
                      #'O_ExperimentEnd',
                      #'X_Exit'
                      ],
    ),
    dict(
        name='perp',
        display_name="Session B",
        num_demo_participants=1,
        completionlink="https://www.prolific.co/",
        app_sequence=['A_ExperimentIntro',
                      'B_Attention_1',
                      'C_GenInstructions_1',
                      'D_EncryptPractice',
                      'E_Attention_2',
                      'F_PlayerRoles',
                      'G_EncryptTask_1',
                      'H_BeliefElicitation',
                      'I_GenInstructions_2',
                      'J_EncryptTask_2',
                      'K_Attention_3',
                      'L_Treatment',
                      'M_Dictator',
                      'N_Fairness',
                      'O_ExperimentEnd'
                      ],
    ),
]

ROOMS = [
    dict(
        name='Session_Y',
        display_name='Victims',
    ),
    dict(
        name='Session_B',
        display_name='Perpetrators',
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '09f!o3#&@=4o$@-_vas++o8hv6#9te_c&+cq$w6mp#jl&1qbd('

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
