import streamlit as st
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Khazabi Rock Paper Scissors",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ============================================================
# BLUE THEME CSS
# ============================================================

st.markdown("""
<style>

    /* Main Background */
    .stApp {
        background: linear-gradient(
            135deg,
            #eff6ff 0%,
            #dbeafe 45%,
            #bfdbfe 100%
        );
    }

    /* Main Title */
    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #1e3a8a;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .sub-title {
        text-align: center;
        color: #2563eb;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 25px;
    }

    /* Game Card */
    .game-card {
        background: rgba(255, 255, 255, 0.92);
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #93c5fd;
        box-shadow: 0 8px 25px rgba(30, 64, 175, 0.15);
        margin-bottom: 20px;
    }

    /* Choice */
    .choice-box {
        background: linear-gradient(
            145deg,
            #dbeafe,
            #eff6ff
        );
        border: 2px solid #60a5fa;
        border-radius: 18px;
        padding: 20px;
        font-size: 4rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(37, 99, 235, 0.15);
    }

    /* Choice Name */
    .choice-name {
        color: #1e40af;
        font-size: 1.1rem;
        font-weight: 700;
        text-align: center;
        margin-top: 8px;
    }

    /* Result Banner */
    .result-win {
        background: linear-gradient(
            135deg,
            #1d4ed8,
            #2563eb
        );
        color: white;
        padding: 18px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 800;
        margin-top: 20px;
    }

    .result-lose {
        background: linear-gradient(
            135deg,
            #1e40af,
            #1d4ed8
        );
        color: white;
        padding: 18px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 800;
        margin-top: 20px;
    }

    .result-tie {
        background: linear-gradient(
            135deg,
            #2563eb,
            #60a5fa
        );
        color: white;
        padding: 18px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 800;
        margin-top: 20px;
    }

    /* Statistics */
    .stat-box {
        background: white;
        border-radius: 15px;
        border: 2px solid #bfdbfe;
        padding: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(30, 64, 175, 0.10);
    }

    .footer {
        text-align: center;
        color: #1e40af;
        padding: 25px;
        font-size: 0.9rem;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        border: 2px solid #60a5fa;
        background: linear-gradient(
            135deg,
            #2563eb,
            #1d4ed8
        );
        color: white;
        font-weight: 700;
        padding: 10px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: linear-gradient(
            135deg,
            #1e40af,
            #2563eb
        );
        border-color: #1e3a8a;
        transform: scale(1.02);
    }

</style>
""", unsafe_allow_html=True)

# ============================================================
# GAME CONSTANTS
# ============================================================

CHOICES = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# ============================================================
# SESSION STATE
# ============================================================

if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "ties" not in st.session_state:
    st.session_state.ties = 0

if "rounds" not in st.session_state:
    st.session_state.rounds = 0

if "last_user_move" not in st.session_state:
    st.session_state.last_user_move = None

if "last_computer_move" not in st.session_state:
    st.session_state.last_computer_move = None

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# ============================================================
# DETERMINE WINNER
# ============================================================

def determine_winner(user, computer):

    if user == computer:
        return "Tie"

    winning_combinations = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    if winning_combinations[user] == computer:
        return "User"

    return "Computer"

# ============================================================
# PLAY ROUND
# ============================================================

def play_round(user_choice):

    computer_choice = random.choice(
        list(CHOICES.keys())
    )

    result = determine_winner(
        user_choice,
        computer_choice
    )

    st.session_state.last_user_move = user_choice

    st.session_state.last_computer_move = computer_choice

    st.session_state.last_result = result

    st.session_state.rounds += 1

    if result == "User":

        st.session_state.user_score += 1

    elif result == "Computer":

        st.session_state.computer_score += 1

    else:

        st.session_state.ties += 1

# ============================================================
# RESET GAME
# ============================================================

def reset_game():

    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.rounds = 0

    st.session_state.last_user_move = None
    st.session_state.last_computer_move = None
    st.session_state.last_result = None

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# 🎮 Khazabi Game"
    )

    st.markdown("---")

    st.markdown(
        "### 📜 Game Rules"
    )

    st.markdown("""
    🪨 **Rock** beats ✂️ Scissors

    📄 **Paper** beats 🪨 Rock

    ✂️ **Scissors** beats 📄 Paper

    🤝 Same choice = Tie
    """)

    st.markdown("---")

    st.markdown(
        "### 🎯 Objective"
    )

    st.info(
        "Choose Rock, Paper, or Scissors "
        "and try to beat the AI!"
    )

    st.markdown("---")

    if st.button(
        "🔄 Reset Game",
        use_container_width=True
    ):

        reset_game()
        st.rerun()

    st.markdown("---")

    st.markdown(
        "**💙 Created by Khazabi**"
    )

# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🎮 Khazabi Rock Paper Scissors'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    '💙 Challenge the AI in a Classic Blue Showdown!'
    '</div>',
    unsafe_allow_html=True
)

# ============================================================
# SCOREBOARD
# ============================================================

score1, score2, score3 = st.columns(3)

with score1:

    st.metric(
        "👤 Player",
        st.session_state.user_score
    )

with score2:

    st.metric(
        "🤝 Ties",
        st.session_state.ties
    )

with score3:

    st.metric(
        "🤖 AI",
        st.session_state.computer_score
    )

st.markdown("---")

# ============================================================
# GAME STATISTICS
# ============================================================

if st.session_state.rounds > 0:

    player_wins = st.session_state.user_score

    win_percentage = (
        player_wins /
        st.session_state.rounds
    ) * 100

else:

    win_percentage = 0

stat1, stat2, stat3 = st.columns(3)

with stat1:

    st.markdown(
        f"""
        <div class="stat-box">
            <b>🎯 Rounds</b><br>
            <h2>{st.session_state.rounds}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat2:

    st.markdown(
        f"""
        <div class="stat-box">
            <b>🏆 Win Rate</b><br>
            <h2>{win_percentage:.1f}%</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat3:

    total_wins = (
        st.session_state.user_score +
        st.session_state.computer_score +
        st.session_state.ties
    )

    st.markdown(
        f"""
        <div class="stat-box">
            <b>🎮 Games Played</b><br>
            <h2>{total_wins}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ============================================================
# CHOOSE MOVE
# ============================================================

st.markdown(
    "### 🎯 Choose Your Move"
)

st.write(
    "Select one of the options below:"
)

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "🪨 Rock",
        use_container_width=True
    ):

        play_round("Rock")
        st.rerun()

with col2:

    if st.button(
        "📄 Paper",
        use_container_width=True
    ):

        play_round("Paper")
        st.rerun()

with col3:

    if st.button(
        "✂️ Scissors",
        use_container_width=True
    ):

        play_round("Scissors")
        st.rerun()

# ============================================================
# ROUND RESULT
# ============================================================

if st.session_state.last_result:

    st.markdown("---")

    st.markdown(
        "### ⚔️ Last Round"
    )

    result_col1, result_col2 = st.columns(2)

    # Player Move
    with result_col1:

        st.markdown(
            "<h4 style='text-align:center; color:#1e40af;'>"
            "👤 Your Move"
            "</h4>",
            unsafe_allow_html=True
        )

        user_move = st.session_state.last_user_move

        st.markdown(
            f"""
            <div class="choice-box">
                {CHOICES[user_move]}
                <div class="choice-name">
                    {user_move}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # AI Move
    with result_col2:

        st.markdown(
            "<h4 style='text-align:center; color:#1e40af;'>"
            "🤖 AI Move"
            "</h4>",
            unsafe_allow_html=True
        )

        computer_move = (
            st.session_state.last_computer_move
        )

        st.markdown(
            f"""
            <div class="choice-box">
                {CHOICES[computer_move]}
                <div class="choice-name">
                    {computer_move}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ========================================================
    # RESULT
    # ========================================================

    result = st.session_state.last_result

    if result == "User":

        st.markdown(
            """
            <div class="result-win">
                🎉 YOU WIN! 🏆
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    elif result == "Computer":

        st.markdown(
            """
            <div class="result-lose">
                🤖 AI WINS THIS ROUND!
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="result-tie">
                🤝 IT'S A TIE!
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🎮 <b>Khazabi Rock Paper Scissors</b><br>
        💙 Built with Python + Streamlit<br>
        🪨 Rock &nbsp; | &nbsp; 📄 Paper &nbsp; | &nbsp; ✂️ Scissors
    </div>
    """,
    unsafe_allow_html=True
)