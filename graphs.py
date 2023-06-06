import matplotlib.pyplot as plt
import seaborn as sns


def session_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True, ylim=(0, 200)):
    columns = ["First_SessionDuration", "First_SessionPlaytime", "SessionDuration_avg", "SessionPlaytime_avg", "SessionDuration_std", "SessionPlaytime_std", "SessionDuration_growth", "SessionPlaytime_growth"]
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(20, 15))
    fig.set_dpi(300)

    axes = axes.ravel()
    for i, col in enumerate(columns):
        sns.histplot(df, x=col, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
        if i > 5:
            axes[i].set_xlim(-0.5, 0.5)
            if common_norm:
                axes[i].set_ylim(*ylim)

    return fig


def session_gaps_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True):
    columns = ["SessionGap_Growth",  "SessionGap_First2Second", "num_session_first_day", "num_session_first_week"]
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
    fig.set_dpi(300)

    axes = axes.ravel()

    sns.histplot(df, x=columns[0], hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[0])
    axes[0].set_xlim(-1, 2)

    sns.histplot(df, x=columns[1], hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[1])
    if common_norm:
        axes[1].set_ylim(0, 250)
    axes[1].set_xlim(-50, 5000)

    sns.histplot(df, x=columns[2], discrete=True, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[2])
    axes[2].set_xlim(-0.5, 20)
    sns.histplot(df, x=columns[3], hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[3])
    axes[3].set_xlim(0, 50)
    return fig

def session_nums_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True):

    columns = ["num_session",  "num_session_first_day", "num_session_first_week", "num_ads_to_session_duration"]
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
    fig.set_dpi(300)

    axes = axes.ravel()

    axes = axes.ravel()
    for i, col in enumerate(columns):
        if i == 1:
            sns.histplot(df, x=col, discrete=True, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
        else:
            sns.histplot(df, x=col, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
    axes[0].set_xlim(-1, 50)
    axes[1].set_xlim(-1, 20)
    axes[1].set_xticks(range(0, 20))
    axes[2].set_xlim(-1, 40)
    axes[3].set_xlim(-0.1, 2)
    
    return fig


def game_behaviour_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True):

    columns = ["Classic_winrate", "goal_range_avg", "goal_range_std", "goal_range_growth", "goal_avg", "goal_std", "goal_growth", "ShootCount_avg", "ShootCount_std", "ShootCount_growth", "EnemyHitCount_avg", "EnemyHitCount_std", "EnemyHitCount_growth", "GoalAcc_avg", "GoalAcc_std", "GoalAcc_growth"]
    fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(20, 15))
    fig.set_dpi(300)

    axes = axes.ravel()

    BINWIDTHS = {10:1,
                 11:1,
                 0:0.05,
                 1:0.125,
                 3:0.01,
                 6:0.0125,
                 7:5,
                 8:5,
                 9:0.025,
                 12:0.075,
                 13:0.025,
                 14:0.025,
                 15:0.025}

    for i, col in enumerate(columns):
        binwidth = BINWIDTHS.get(i)
        sns.histplot(df, x=col, binwidth=binwidth, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
    axes[0].set_xlim(-0.1, 1.1)
    axes[1].set_xlim(0.5, 4)
    axes[3].set_xlim(-0.15, 0.15)
    axes[6].set_xlim(-0.2, 0.3)
    axes[8].set_xlim(-1, 70)
    axes[9].set_xlim(-0.25, 0.75)
    axes[10].set_xlim(-1, 20)
    axes[11].set_xlim(-1, 20)
    axes[12].set_xlim(-0.5, 1.0)
    axes[13].set_xlim(-0.1, 0.6)
    axes[15].set_xlim(-0.4, 0.4)
    
    return fig


def levels_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True):
    columns = ["Levels_FirstSession",  "Levels_Session_avg", "Levels_Session_std", "Levels_Session_growth"]
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
    fig.set_dpi(300)

    axes = axes.ravel()
    BINWIDTHS = {0:1,
                 1:0.5,
                 2:0.5,
                 3:0.05}

    for i, col in enumerate(columns):
        binwidth = BINWIDTHS.get(i)
        sns.histplot(df, x=col, binwidth=binwidth, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
    axes[0].set_xlim(-1, 15)
    axes[1].set_xlim(-1, 10)
    axes[2].set_xlim(-1, 8)
    axes[3].set_xlim(-0.65, 0.8)

    return fig


def rv_interstitial_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True):

    columns = ["RvCount_Session_avg",  "RvCount", "InterstitialCount_Session_avg", "InterstitialCount"]
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
    fig.set_dpi(300)

    axes = axes.ravel()
    BINWIDTHS = {0:0.25,
                 1:2}

    for i, col in enumerate(columns):
        binwidth = BINWIDTHS.get(i)
        sns.histplot(df, x=col, binwidth=binwidth, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])

    if common_norm:
        axes[0].set_ylim(0, 250)
        axes[1].set_ylim(0, 250)

    axes[1].set_xlim(-5, 80)
    axes[2].set_xlim(-1, 15)
    if common_norm:
        axes[3].set_ylim(0, 350)
    axes[3].set_xlim(-10, 150)
    
    return fig


def interstitial_placements_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True):
    columns = ["InterstitialCount_End_Level",  "InterstitialCount_Idle_User", "InterstitialCount_Mid_Level"]
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))
    fig.set_dpi(100)

    axes = axes.ravel()
    BINWIDTHS = {}

    for i, col in enumerate(columns):
        binwidth = BINWIDTHS.get(i)
        if i == 1:
            sns.histplot(df, x=col, discrete=True, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
        else:
            sns.histplot(df, x=col, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
        axes[i].set_xlim(0, 30)
        if common_norm:
            axes[i].set_ylim(0, 1400)
    return fig


def totals_graphs(df, hue=None, palette="Set1", stat="count", common_norm=True):
    columns = ["InterstitialImpression", "RVCompleted", "TotalAdRevenue", "TotalInGameTime", "TotalPlaytime", "UniqueDays"]
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(20, 10))
    fig.set_dpi(100)

    axes = axes.ravel()
    BINWIDTHS = {}

    for i, col in enumerate(columns):
        binwidth = BINWIDTHS.get(i)
        if i in {1, 5}:
            sns.histplot(df, x=col, discrete=True, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
        else:
            sns.histplot(df, x=col, hue=hue, kde=True, palette=palette, stat=stat, common_norm=common_norm, ax=axes[i])
    axes[0].set_xlim(-1, 100)
    axes[1].set_xlim(-1, 20)
    if common_norm:
        axes[1].set_ylim(0, 500)
    axes[2].set_xlim(0, 5)
    axes[3].set_xlim(-1, 20000)
    axes[4].set_xlim(-1, 12500)
    axes[4].set_xlim(-1, 12500)
    axes[5].set_xlim(0, 15)
    return fig