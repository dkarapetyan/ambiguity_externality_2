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
PARTICIPANT_FIELDS = ['externality_I',
                      'externality_II',
                      'tokens_I',
                      'tokens_II',
                      'nettokens_I',
                      'nettokens_II',
                      'ext_choice',
                      'payoff_I',
                      'payoff_II',
                      'dictator_I',
                      'dictator_II',
                      'random_part',
                      'performance_I',
                      'performance_II',
                      'failedattentioncheck',
                      'bluematch'
                      ]

SESSION_CONFIGS = [
    dict(
        name='victim1',
        display_name="Session Y1",
        num_demo_participants=1,
        completionlink="http://www.prolific.co",
        app_sequence=[#'A_LEDRIntro',
                      #'B_Consent',
                      #'D_ExperimentIntro',
                      #'E_PartI_Attention',
                      #'E_PartI_GenInstructions',
                      #'F_PartI_EncryptPractice',
                      #'G_PartI_UnderstandingCheck',
                      'H_PartI_EncryptionTask',
                      'I_PartI_RevealEarnings',
                      #'J_PartI_ExtBeliefs',
                      #'K_PartI_Attention',
                      #'K_PartI_Treatment',
                      'L_PartI_Dictator',
                      #'M_PartI_Fairness',
                      #'W_LEDROutro',
                      #'X_Exit'
                      ],
    ),
    dict(
        name='victim2',
        display_name="Session Y2",
        num_demo_participants=1,
        completionlink="http://www.prolific.co",
        app_sequence=[#'A_LEDRIntro',
                      #'B_Consent',
                      #'D_ExperimentIntro',
                      'E_PartI_Attention',
                      'O_PartII_GenInstructions',
                      'P_PartII_EncryptPractice',
                      'Q_PartII_UnderstandingCheck',
                      'R_PartII_EncryptionTask',
                      'R_PartII_RevealEarnings',
                      'S_PartII_ExtBeliefs',
                      #'T_PartII_Attention',
                      #'T_PartII_Treatments',
                      'U_PartII_Dictator',
                      #'V_PartII_Fairness',
                      #'W_LEDROutro',
                      #'X_Exit'
                      ],
    ),
    dict(
        name='perp',
        display_name="Session B",
        num_demo_participants=1,
        completionlink="https://www.prolific.co/",
        app_sequence=[#'A_LEDRIntro',
                      #'B_Consent',
                      #'D_ExperimentIntro',
                      #'E_PartI_Attention',
                      #'E_PartI_GenInstructions',
                      #'F_PartI_EncryptPractice',
                      #'G_PartI_UnderstandingCheck',
                      'H_PartI_EncryptionTask',
                      'I_PartI_RevealEarnings',
                      #'K_PartI_Attention',
                      #'M_PartI_Fairness',
                      #'N_PartI_End',
                      #'O_PartII_GenInstructions',
                      'P_PartII_EncryptInstructions',
                      'Q_PartII_UnderstandingCheck',
                      'R_PartII_EncryptionTask',
                      'T_PartII_Attention',
                      'T_PartII_Treatments',
                      'V_PartII_Fairness',
                      'W_End_PartII',
                      'W_LEDROutro',
                      'X_Exit'
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
