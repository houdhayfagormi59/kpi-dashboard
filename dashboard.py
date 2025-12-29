import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="REPORT GAME AJMAN CLUB ACADEMY KPI'S PERFORMANCE TEAM",
    layout="wide"
)

st.title("REPORT GAME AJMAN CLUB ACADEMY KPI'S PERFORMANCE TEAM")
st.markdown("---")

# ================= GAME INFO =================
st.subheader("GAME INFO")
col1, col2, col3 = st.columns(3)
with col1:
    team_home = st.text_input("TEAM HOME")
with col2:
    team_away = st.text_input("TEAM AWAY")
with col3:
    date = st.date_input("DATE")

score = st.text_input("SCORE")
st.divider()

# ================= PHASE ATTACK =================
st.subheader("PHASE ATTACK")
a1, a2, a3, a4 = st.columns(4)
with a1:
    key_passes = st.number_input("KEY PASSES", 0)
with a2:
    dribble_success = st.number_input("DRIBBLE SUCCESS", 0)
with a3:
    shoot_on_target = st.number_input("SHOOT ON TARGET", 0)
with a4:
    ball_in_box_receive = st.number_input("BALL IN BOX (RECEIVE)", 0)

# ================= PHASE DEFENSE =================
st.subheader("PHASE DEFENSE")
d1, d2, d3, d4 = st.columns(4)
with d1:
    tackles_success = st.number_input("TACKLES SUCCESS", 0)
with d2:
    interceptions = st.number_input("INTERCEPTIONS", 0)
with d3:
    one_vs_one_def = st.number_input("1VS1 DEF", 0)
with d4:
    duels_aerial = st.number_input("DUELS AERIAL", 0)

st.divider()

# ================= PLAYER KPI BY POSITION =================
st.subheader("PLAYER KPI BY POSITION")
cb, fb, cm, wing, stt = st.columns(5)

with cb:
    st.markdown("**CENTER BACK**")
    cb_ball_progress = st.number_input("BALL PROGRESS", 0)
    cb_interceptions = st.number_input("INTERCEPTIONS", 0, key="cb_int")
    cb_duels = st.number_input("DUELS AERIAL", 0, key="cb_duel")

with fb:
    st.markdown("**BACK L/R**")
    fb_tackles = st.number_input("TACKLES", 0)
    fb_key_passes = st.number_input("KEY PASSES", 0, key="fb_kp")
    fb_first_touch = st.number_input("FIRST TOUCH", 0)

with cm:
    st.markdown("**CENTER MIDFIELD**")
    cm_ball_between = st.number_input("BALL BETWEEN LINES", 0)
    cm_forward_run = st.number_input("FORWARD RUN", 0)
    cm_pass_break = st.number_input("PASS BREAK LINE", 0)
    cm_def_cover = st.number_input("DEFENSE COVER", 0)

with wing:
    st.markdown("**WING L/R**")
    wing_1v1 = st.number_input("1VS1 ATTACK", 0)
    wing_run_behind = st.number_input("RUN BEHIND", 0)
    wing_shoot_create = st.number_input("SHOOT CREATE", 0)
    wing_crossing = st.number_input("CROSSING", 0)

with stt:
    st.markdown("**STRIKER**")
    mov_in_box = st.number_input("MOV IN BOX", 0)
    pressing_triggers = st.number_input("PRESSING TRIGGERS", 0)
    shoot = st.number_input("SHOOT", 0, key="shoot2")
    ball_in_box = st.number_input("BALL IN BOX", 0)

# ================= TOTAL KPI =================
total = (
    key_passes + dribble_success + shoot_on_target + ball_in_box_receive +
    tackles_success + interceptions + one_vs_one_def + duels_aerial +
    cb_ball_progress + cb_interceptions + cb_duels +
    fb_tackles + fb_key_passes + fb_first_touch +
    cm_ball_between + cm_forward_run + cm_pass_break + cm_def_cover +
    wing_1v1 + wing_run_behind + wing_shoot_create + wing_crossing +
    mov_in_box + pressing_triggers + shoot + ball_in_box
)

st.divider()
st.subheader("KPI PERFORMANCE TEAM")
st.metric("TOTAL KPI SCORE", total)

# ================= KPI CATEGORY =================
if total <= 30:
    st.error("WEAK")
elif total <= 60:
    st.warning("MEDIUM")
elif total <= 90:
    st.info("NORMAL")
elif total <= 120:
    st.success("GOOD")
else:

    st.success("VERY GOOD")
