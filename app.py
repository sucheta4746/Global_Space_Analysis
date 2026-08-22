"""Premium visual layer for the existing Space Insights Streamlit dashboard."""
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Space Dashboard", page_icon="*", layout="wide",initial_sidebar_state="expanded")
@st.cache_data
def load_data():
    return (
        pd.read_csv("01_space_launches_main.csv"), pd.read_csv("02_rockets_database.csv"),
        pd.read_csv("03_ai_in_space.csv"), pd.read_csv("04_space_economy.csv"),
        pd.read_csv("cleaned_spacemissions1.csv"), pd.read_csv("cleaned_rocketdatabase2.csv"),
        pd.read_csv("cleaned_ai3.csv"), pd.read_csv("cleaned_space_economy4.csv"),
    )

df1, df2, df3, df4, df, rockets, ai1, economy = load_data()
css = Path("premium_space.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
st.markdown('''<div class="space-decor" aria-hidden="true"><svg class="satellite" viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="45" y="26" width="30" height="28" rx="4" stroke="currentColor" stroke-width="3"/><path d="M45 32H8v16h37M75 32h37v16H75M55 26V14h10v12M60 54v12" stroke="currentColor" stroke-width="3"/><circle cx="60" cy="40" r="5" fill="currentColor"/></svg><svg class="astronaut" viewBox="0 0 80 100" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="40" cy="22" r="16" stroke="currentColor" stroke-width="3"/><path d="M25 39c-3 20-2 39 4 54m26-54c3 20 2 39-4 54M25 48 8 65m47-17 17 17M33 93l-9 5m23-5 9 5" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg><svg class="edge-rocket" viewBox="0 0 50 100" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M25 5C7 27 9 55 9 64h32c0-9 2-37-16-59Z" stroke="currentColor" stroke-width="3"/><path d="M9 63 3 80l14-8m24-9 6 17-14-8M20 64l5 28 5-28" stroke="currentColor" stroke-width="3"/></svg><span class="moon"></span><span class="radar"></span><span class="meteor"></span></div><span class="hologram" aria-hidden]="true"></span>''', unsafe_allow_html=True)


def card(label, value, note):
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">{label}</div><div class="kpi-value">{value}</div><div class="kpi-text">{note}</div></div>', unsafe_allow_html=True)

def square_card(title, value):
    st.markdown(f'<div class="square-card"><div class="square-value">{value}</div><div class="square-title">{title}</div></div>', unsafe_allow_html=True)

def show_chart(fig, height=330):
    fig.update_layout(
        height=height, margin=dict(l=58, r=30, t=88, b=62),
        paper_bgcolor="#080e28", plot_bgcolor="#080e28",
        font=dict(color="#d9e6fb", family="Manrope", size=12),
        title=dict(x=.025, y=.975, font=dict(size=16, color="#f2f7ff")),
        legend=dict(orientation="h", y=1.14, x=0, font=dict(color="#d7e5fb", size=11)),
        hoverlabel=dict(bgcolor="#121d47", font_color="#f5f9ff"),
    )
    fig.update_xaxes(gridcolor="rgba(154,180,230,.18)", zeroline=False, tickfont=dict(color="#c2d0e9"), title_font=dict(color="#d9e6fb"), automargin=True)
    fig.update_yaxes(gridcolor="rgba(154,180,230,.18)", zeroline=False, tickfont=dict(color="#c2d0e9"), title_font=dict(color="#d9e6fb"), automargin=True)
    st.plotly_chart(fig, use_container_width=True)


def story_signal(label, headline, detail, tone="mission"):
    """Present a data-derived takeaway in a consistent, scan-friendly format."""
    st.markdown(
        f'<div class="story-signal {tone}-signal"><span>{label}</span><strong>{headline}</strong><p>{detail}</p></div>',
        unsafe_allow_html=True,
    )


def chapter_story(kicker, title, copy, icon, tone="cyan"):
    """Open a dashboard chapter with a visual cue and a human-readable thesis."""
    st.markdown(
        f'<section class="chapter-story {tone}-story"><div class="chapter-orbit"><span class="chapter-icon">{icon}</span><i></i><b></b></div><div><span class="chapter-kicker">{kicker}</span><h2>{title}</h2><p>{copy}</p></div></section>',
        unsafe_allow_html=True,
    )


def dataset_view_button(view_id, symbol, name):
    """Render one compact glass navigation button for the dataset explorer."""
    selected = st.session_state.dataset_view == view_id
    if st.button(f"{symbol}\n{name}", key=f"dataset_nav_{view_id}", use_container_width=True, type="primary" if selected else "secondary"):
        st.session_state.dataset_view = view_id
        st.rerun()


def square_card(icon, title, value):
    st.markdown(f"""
    <style>
    .square-card {{
        width:220px;
        height:200px;
        border:2px solid #00E5FF;
        border-radius:25px;
        background:#25244D;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        margin:20px;
        box-shadow:0 0 12px rgba(0,229,255,.35);
    }}

    .square-card:hover{{
        transform: scale(1.05);
        box-shadow:0 0 30px rgba(34,211,238,.4);
    
    }}

    .square-icon {{
        font-size:55px;
        margin-bottom:0px;
    }}

    .square-value {{
        font-size:35px;
        font-weight:700;
        color:white;
    }}

    .square-title {{
        margin-top:3px;
        color:white;
        font-size:20px;
        text-align:center;
    }}
    
    </style>

    <div class="square-card">
        <div class="square-icon">{icon}</div>
        <div class="square-value">{value}</div>
        <div class="square-title">{title}</div>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown('''<div class="brand"><svg viewBox="0 0 24 24" fill="none"><path d="M12 2c3 3 4 6 4 10l3 3-3 1-1 4-3-3c-4 0-7-1-10-4 3-6 6-9 10-11Z" stroke="currentColor" stroke-width="1.6"/><path d="m7 17-3 3M16 8h.01" stroke="currentColor" stroke-width="1.6"/></svg>SPACE INSIGHTS</div>''', unsafe_allow_html=True)
    st.markdown('<div class="side-caption">Mission control</div>', unsafe_allow_html=True)
    opt = st.radio(
        "Navigation",
        ["Start Here", "Home", "Missions", "Rockets", "AI in Space", "Space Economy", "Dataset", "Mission Lab", "About"],
        label_visibility="collapsed",
        key="navigation",
    )
    st.markdown('<div class="side-caption">Mission filters</div>', unsafe_allow_html=True)
    year = st.slider("Year range", int(df.year.min()), int(df.year.max()), (int(df.year.min()), int(df.year.max())))
    filtered = df[df.year.between(*year)].copy()
    countries = st.multiselect("Select Country", sorted(filtered.Country.dropna().unique()))
    if countries: filtered = filtered[filtered.Country.isin(countries)]
    agencies = st.multiselect("Agency", sorted(filtered.Agency.dropna().unique()))
    if agencies: filtered = filtered[filtered.Agency.isin(agencies)]
    ai_filter = st.radio("AI Assisted", ["All", "Yes", "No"])
    if ai_filter == "Yes": filtered = filtered[filtered.AI_Assisted == 1]
    if ai_filter == "No": filtered = filtered[filtered.AI_Assisted == 0]
    st.info("Together we explore the universe of possibilities.")
    st.caption("Made by Sucheta")

if opt == "Start Here":
    st.markdown("""
        <section class="intro-hero">
            <div class="intro-hero-copy">
                <p class="intro-eyebrow">GLOBAL SPACE MISSIONS ANALYSIS</p>
                <h1>From the First Launch<br>to the New Space Age.</h1>
                <p>Humanity's journey into space began with one launch. Today it connects weather forecasts, navigation, communication, science, and a growing global economy.</p>
                <p class="intro-support">This is an interactive story of the people, missions, machines, and ideas that carried us from looking up at the sky to working beyond it.</p>
            </div>
            <div class="intro-orbit" aria-hidden="true">
                <span class="intro-orbit-ring ring-a"></span><span class="intro-orbit-ring ring-b"></span><span class="intro-orbit-ring ring-c"></span>
                <span class="intro-earth"></span><span class="intro-rocket-track"><span class="intro-rocket-rotor"><span class="intro-rocket"></span></span></span><span class="intro-satellite"></span>
                <span class="intro-signal signal-one"></span><span class="intro-signal signal-two"></span>
                <span class="intro-orbit-label">MISSION SIGNAL ACTIVE</span>
            </div>
        </section>
    """, unsafe_allow_html=True)

    st.markdown("""
        <section class="intro-journey">
            <p class="intro-eyebrow">A JOURNEY THROUGH TIME</p>
            <h2>One human ambition. Five chapters.</h2>
            <div class="intro-timeline">
                <div><span>01</span><strong>Beginning of<br>Space Age</strong></div>
                <i></i><div><span>02</span><strong>Global<br>Exploration</strong></div>
                <i></i><div><span>03</span><strong>Rocket<br>Evolution</strong></div>
                <i></i><div><span>04</span><strong>AI<br>Transformation</strong></div>
                <i></i><div><span>05</span><strong>Space<br>Economy</strong></div>
            </div>
        </section>
    """, unsafe_allow_html=True)

    highlights = [
        (f"{len(df):,}", "recorded missions"),
        (f"{df['Country'].nunique():,}", "countries in the story"),
        (f"{df['Agency'].nunique():,}", "space agencies"),
        (f"{len(rockets):,}", "rocket profiles"),
        (f"{len(ai1):,}", "AI space records"),
    ]
    for col, (value, label) in zip(st.columns(5), highlights):
        with col:
            st.markdown(f'<div class="intro-stat"><strong>{value}</strong><span>{label}</span></div>', unsafe_allow_html=True)

    st.markdown('<section class="intro-discover"><p class="intro-eyebrow">WHAT WILL YOU DISCOVER?</p><h2>Space is not distant. Its impact is everywhere.</h2><p class="intro-discover-copy">Follow the evidence behind humanity’s exploration, the technology that made it possible, and the new opportunities it is creating on Earth.</p></section>', unsafe_allow_html=True)
    discoveries = [
        ("01", "Global Mission Landscape", "See where missions began, who led them, and how exploration spread across the world."),
        ("02", "Rocket & Launch Evolution", "Meet the vehicles that turned a bold idea into a repeatable journey beyond Earth."),
        ("03", "AI in Space", "Explore how intelligent systems help spacecraft see, learn, and respond far from home."),
        ("04", "Space Economy", "Understand how missions create new industries, investment, and services for everyday life."),
        ("05", "Global Trends & Insights", "Find the patterns that reveal where space has been and what could come next."),
    ]
    for col, discovery in zip(st.columns(5), discoveries):
        with col:
            number, title, copy = discovery
            st.markdown(f'<article class="intro-discovery"><span>{number}</span><h3>{title}</h3><p>{copy}</p></article>', unsafe_allow_html=True)

    st.markdown('<div class="start-uvp-line"><span>WHY THIS EXISTS</span><strong>One guided place to see where space has been, understand what drives it, and imagine what comes next.</strong></div>', unsafe_allow_html=True)
    st.markdown('<section class="intro-cta"><p class="intro-eyebrow">THE STORY CONTINUES</p><h2>Ready to explore the data?</h2><p>This is more than a collection of charts. It is an intelligence platform for understanding how humanity has explored, commercialized, and transformed space.</p></section>', unsafe_allow_html=True)
    left, centre, right = st.columns([1, 1.3, 1])
    with centre:
        st.button("ENTER THE SPACE INTELLIGENCE HUB ->", key="enter_dashboard", on_click=lambda: setattr(st.session_state, "navigation", "Home"), use_container_width=True)
    st.markdown('<p class="intro-footer">Explore the missions. Understand the technology. See the future of space.</p>', unsafe_allow_html=True)

elif opt == "Mission Lab":
    st.markdown('<div class="dashboard-title">MISSION LAB</div><section class="mission-lab-intro"><span class="mission-lab-marker" aria-hidden="true"></span><span>YOUR SPACE EXPERIMENT</span><h1>What will you send beyond Earth?</h1><p>Choose a mission, pick an agency, and shape the journey. The dashboard compares your idea with real historical mission patterns and gives you a simple score.</p><div class="lab-how-it-works"><b>CHOOSE</b><i>→</i><b>ADJUST</b><i>→</i><b>SEE YOUR SCORE</b></div></section>', unsafe_allow_html=True)

    lab_left, lab_right = st.columns([1.7, 1.5], gap="large")
    with lab_left:
        st.markdown('<div class="lab-step-heading"><span>STEP 1</span><strong>What kind of journey?</strong><small>Choose the mission you want to send.</small></div>', unsafe_allow_html=True)
        mission_type = st.selectbox("Mission type", sorted(df["Mission_Type"].dropna().unique()), key="lab_mission_type")
        mission_agencies = sorted(df.loc[df["Mission_Type"] == mission_type, "Agency"].dropna().unique())
        agency_options = ["All agencies"] + mission_agencies
        st.markdown('<div class="lab-step-heading compact"><span>STEP 2</span><strong>Who will help launch it?</strong><small>Choose a space agency or compare all agencies.</small></div>', unsafe_allow_html=True)
        selected_agency = st.selectbox("Agency", agency_options, key="lab_agency")
        st.markdown('<div class="lab-step-heading compact"><span>STEP 3</span><strong>Shape your mission</strong><small>Change the plan and watch the score react.</small></div>', unsafe_allow_html=True)
        payload = st.slider("Payload size (kg)", 0, int(df["Payload_Mass_kg"].max()), 1000, step=100, key="lab_payload")
        crew = st.slider("People on board", 0, int(df["Crew_Count"].max()), 0, key="lab_crew")
        risk = st.slider("How adventurous?", 1, 10, 5, help="1 means cautious; 10 means bold.", key="lab_risk")
        ai_support = st.toggle("Add AI support", value=True, key="lab_ai")

    mission_profile = df[df["Mission_Type"] == mission_type].copy()
    profile = mission_profile if selected_agency == "All agencies" else mission_profile[mission_profile["Agency"] == selected_agency].copy()
    if profile.empty:
        profile = mission_profile
    typical_payload = profile["Payload_Mass_kg"].median()
    typical_crew = profile["Crew_Count"].median()
    base_success = profile["Mission_Success"].mean() * 100
    payload_fit = max(0, 100 - abs(payload - typical_payload) / max(typical_payload, 1) * 35)
    crew_fit = max(0, 100 - abs(crew - typical_crew) * 12)
    ai_bonus = 5 if ai_support else 0
    mission_score = min(100, max(0, base_success * 0.55 + payload_fit * 0.25 + crew_fit * 0.1 + risk * 1.0 + ai_bonus))

    with lab_right:
        st.markdown('<div class="section-divider">Your mission result</div>', unsafe_allow_html=True)
        st.markdown(f'''<div class="mission-lab-result"><span class="lab-kicker">PROJECTED MISSION SCORE</span><strong>{mission_score:.0f}<small>/100</small></strong><p>Your {mission_type.lower()} mission with {selected_agency} is compared with {len(profile):,} similar historical missions.</p><div class="lab-signal"><span>Typical success rate</span><b>{base_success:.1f}%</b></div><div class="lab-signal"><span>Typical payload</span><b>{typical_payload:,.0f} kg</b></div><div class="lab-signal"><span>AI support</span><b>{"On" if ai_support else "Off"}</b></div></div>''', unsafe_allow_html=True)

    mission_meters = [
        ("PAYLOAD FIT", payload_fit, "How close your payload is to the typical profile"),
        ("CREW FIT", crew_fit, "How closely your crew plan matches the mission type"),
        ("HISTORICAL CONFIDENCE", base_success, "Average success across similar missions"),
    ]
    meter_markup = "".join(
        f'<div class="mission-meter"><div><span>{label}</span><b>{value:.0f}%</b></div><div class="meter-track"><i style="width:{min(100, max(0, value)):.1f}%"></i></div><small>{detail}</small></div>'
        for label, value, detail in mission_meters
    )
    launch_state = "READY FOR LAUNCH" if mission_score >= 70 else "NEEDS MORE TESTING"
    score_hint = "Reduce payload" if payload_fit < 55 else "Increase payload" if payload_fit > 92 else "Payload is close"
    crew_hint = "Reduce crew" if crew_fit < 55 and crew > typical_crew else "Increase crew" if crew_fit < 55 else "Crew plan is close"
    st.markdown(f'<div class="mission-meter-board"><div class="meter-board-heading"><span>MISSION PLAYBACK</span><strong>How your choices perform</strong></div><div class="reactor-stage"><div class="reactor-orbit orbit-a"></div><div class="reactor-orbit orbit-b"></div><div class="reactor-core"><span>✦</span><small>LIVE</small></div><i class="reactor-signal signal-a">◉</i><i class="reactor-signal signal-b">✦</i><i class="reactor-signal signal-c">◆</i></div><div class="mission-personality"><span>MISSION PERSONALITY</span><b>{"CAREFUL EXPLORER" if risk <= 3 else "BALANCED COMMANDER" if risk <= 7 else "BOLD PATHFINDER"}</b><small>{score_hint} • {crew_hint} to move closer to the historical success signal.</small></div>{meter_markup}<div class="launch-status"><span class="launch-rocket">🚀</span><div><small>ORBIT AI READOUT</small><strong>{launch_state}</strong><p>{mission_type} with {selected_agency} • {len(profile):,} comparable missions</p></div><b>{mission_score:.0f}</b></div></div>', unsafe_allow_html=True)

elif opt == "Home":
    st.markdown('<div class="dashboard-title">GLOBAL SPACE MISSION ANALYTICS DASHBOARD</div><div class="dashboard-subtitle">Explore global space missions, rockets, agencies, AI impact &amp; the space economy.</div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-strip"><i></i><b>POWERED BY PANDAS, PLOTLY &amp; STREAMLIT</b> &nbsp; | &nbsp; GLOBAL SPACE MISSION ANALYTICS</div>', unsafe_allow_html=True)
    chapter_story("CHAPTER 01 / THE BIG PICTURE", "Every launch is a thread in one living story.", "Start with the rhythm of exploration: who launched, where the activity gathered, and how the mission record changes across time.", "◉")
    values = [("TOTAL MISSIONS", f"{len(df):,}", "All time missions"), ("COUNTRIES", filtered.Country.nunique(), "Participating countries"), ("TOTAL AGENCIES", filtered.Agency.nunique(), "Space agencies"), ("SUCCESS RATE", f"{filtered.Mission_Success.mean()*100:.2f}%" if len(filtered) else "--", "Selected missions"), ("COST / KG", f"${filtered.Cost_Per_kg.median():.1f}" if len(filtered) else "--", "Median cost per kg"), ("AI ASSISTED", f"{filtered.AI_Assisted.sum():,.0f}", "Missions using AI")]
    for col, item in zip(st.columns(6), values):
        with col: card(*item)
    st.markdown('<div class="section-divider">Mission intelligence</div>', unsafe_allow_html=True)
    home_left, home_right = st.columns(2)
    with home_left:
        launches = filtered.groupby("year").size().reset_index(name="Launches")
        show_chart(px.line(launches, x="year", y="Launches", markers=True, title="Launch activity over time", color_discrete_sequence=["#62ddff"]))
    with home_right:
        country = filtered.groupby("Country").size().nlargest(10).sort_values().reset_index(name="Launches")
        fig = px.bar(country, x="Launches", y="Country", orientation="h", title="Leading launch nations", color="Launches", color_continuous_scale=["#403180", "#62ddff"]); fig.update_coloraxes(showscale=False); show_chart(fig)
    st.markdown("""
            <div class="quote-card">
            <div class="quote-icon">🌌</div>

            <div class="quote-text">
                "Turning six decades of space exploration
                into insights that everyone can understand."
            </div>

            <div class="quote-author">
                — Space Insights
            </div>
            </div>
        """, unsafe_allow_html=True)

    home_lower_left, home_lower_right = st.columns(2)
    with home_lower_left:
        sites = filtered.groupby("Launch_Site").size().nlargest(10).sort_values().reset_index(name="Launches")
        fig = px.bar(sites, x="Launches", y="Launch_Site", orientation="h", title="Top launch sites", color="Launches", color_continuous_scale=["#332965", "#a994ff", "#62ddff"]); fig.update_coloraxes(showscale=False); show_chart(fig)
    with home_lower_right:
        country_year = filtered.groupby(["year", "Country"]).size().reset_index(name="Launches")
        race = px.bar(country_year, x="Country", y="Launches", color="Launches", animation_frame="year", title="Global space race through time", color_continuous_scale=["#403180", "#62ddff"])
        race.update_layout(transition=dict(duration=450)); show_chart(race)
    story_signal("THE FIRST READING", f"{filtered.Country.nunique()} countries are active in the selected story.", "Use the filters to move from the global picture to the exact places and eras where exploration accelerated.")
  
elif opt == "Missions":
    st.title("All time Missions Explorer")
    st.markdown("Dive into Mission analytics over decades.")
    chapter_story("CHAPTER 02 / HUMAN AMBITION", "From bold attempts to repeatable progress.", "This chapter follows the tension between launch volume and mission success, revealing how exploration becomes an operating discipline.", "🚀", "cyan")
    values = [("TOTAL MISSIONS", f"{len(df):,}", "All time missions"), ("MISSION TYPES", filtered.Mission_Type.nunique(), "Different mission kinds"), ("SPACE ERAS", filtered.Space_Era.nunique(), "Across decades"), ("COMMERCIAL", f"{filtered.Commercial_Mission.sum():,}", "Commercial missions"), ("CREWED", f"{filtered.crewed.sum():,}", "Crew based missions"), ("SUCCESSFUL", f"{filtered.Mission_Success.sum():,}", "Successful missions")]
    for col, item in zip(st.columns(6), values):
        with col: card(*item)
    st.markdown('<div class="section-divider">Mission patterns</div>', unsafe_allow_html=True)
    mission_left, mission_right = st.columns(2)
    with mission_left:
        yearly = filtered.groupby("year").agg(Launches=("Mission_ID","count"), Successful=("Mission_Success","sum")).reset_index()
        show_chart(px.line(yearly, x="year", y=["Launches","Successful"], markers=True, title="Launches and successful missions", color_discrete_map={"Launches":"#62ddff","Successful":"#7cf0a5"}))
    with mission_right:
        era = filtered.groupby("Space_Era").size().reset_index(name="Missions")
        show_chart(px.pie(era, names="Space_Era", values="Missions", hole=.58, title="Mission activity by space era", color_discrete_sequence=["#62ddff","#a994ff","#7cf0a5","#ffc46b","#ee88b7"]))
    mission_row_two_left, mission_row_two_right = st.columns(2)
    with mission_row_two_left:
        era_hist = px.histogram(filtered, x="Space_Era", color="Space_Era", title="Distribution of missions across space eras", color_discrete_sequence=["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4"])
        era_hist.update_layout(showlegend=False); show_chart(era_hist)
    with mission_row_two_right:
        agency_type = px.histogram(filtered, x="year", color="Agency_Type", title="Government vs private space missions", color_discrete_map={"Government":"#7cf0a5", "Private":"#62ddff", "Business":"#a994ff"})
        show_chart(agency_type)
    mission_row_three_left, mission_row_three_right = st.columns(2)
    with mission_row_three_left:
        corr_cols = ["Payload_Mass_kg", "Mission_Cost_USD_M", "Cost_Per_kg", "Crew_Count", "Mission_Success"]
        corr = filtered[corr_cols].corr()
        heatmap = px.imshow(corr, color_continuous_scale=["#0d1539", "#6251b4", "#62ddff"], title="Mission metric correlation")
        show_chart(heatmap)
    with mission_row_three_right:
        hierarchy = filtered.groupby(["Country", "Agency", "Rocket"]).size().reset_index(name="Missions")
        show_chart(px.sunburst(hierarchy, path=["Country", "Agency", "Rocket"], values="Missions", title="Country, agency and rocket distribution", color_discrete_sequence=px.colors.qualitative.Prism))
    mission_row_four_left, mission_row_four_right = st.columns(2)
    with mission_row_four_left:
        payload_tree = filtered.groupby(["Country", "Agency", "Rocket"], dropna=False).agg(Payload_Mass_kg=("Payload_Mass_kg", "sum"), Mission_Success=("Mission_Success", "mean")).reset_index()
        show_chart(px.treemap(payload_tree, path=["Country", "Agency", "Rocket"], values="Payload_Mass_kg", color="Mission_Success", color_continuous_scale=["#ff7c9e", "#ffc46b", "#7cf0a5"], title="Payload contribution by mission hierarchy"), height=410)
    with mission_row_four_right:
        era_type = filtered.groupby(["Space_Era", "Mission_Type"]).size().reset_index(name="Missions")
        show_chart(px.sunburst(era_type, path=["Space_Era", "Mission_Type"], values="Missions", title="Mission types across space eras", color_discrete_sequence=px.colors.qualitative.Plotly_r), height=410)
    comparison = yearly.melt(id_vars="year", value_vars=["Launches", "Successful"], var_name="Metric", value_name="Count")
    comparison_chart = px.bar(comparison, x="year", y="Count", color="Metric", facet_col="Metric", title="Year-wise mission analysis", color_discrete_map={"Launches":"#62ddff", "Successful":"#7cf0a5"})
    comparison_chart.update_layout(showlegend=False)
    show_chart(comparison_chart, height=360)
    story_signal("MISSION SIGNAL", f"{int(filtered.Mission_Success.sum()):,} selected missions reached success.", "The charts above connect the human scale of launches with the practical signals of reliability, crew, cost, and mission type.")

elif opt == "Rockets":
    st.title("Rocket Database")
    chapter_story("CHAPTER 03 / MACHINES OF MOMENTUM", "A rocket is not just hardware. It is accumulated confidence.", "Compare the vehicles that carried exploration from one-off achievements toward repeatable access, reuse, and operational scale.", "◒", "violet")
    for col, item in zip(st.columns(3), [("ROCKETS",rockets.shape[0],"Catalogue entries"),("OPERATORS",rockets.Operator.nunique(),"Active organisations"),("REUSABLE",int(rockets.reusable.sum()),"Reusable vehicles")]):
        with col: card(*item)
    st.markdown('<div class="section-divider">Vehicle performance</div>', unsafe_allow_html=True)
    rocket_left, rocket_right = st.columns(2)
    with rocket_left:
        fleet = rockets.nlargest(10,"Total_Launches").sort_values("Total_Launches")
        show_chart(px.bar(fleet, x="Total_Launches", y="Rocket_Name", orientation="h", title="Most flown vehicles", color="Success_Rate", color_continuous_scale=["#a994ff","#62ddff"]))
    with rocket_right:
        reuse = rockets.assign(Type=rockets.reusable.map({1:"Reusable",0:"Not reusable"}).fillna("Unknown")).groupby("Type").size().reset_index(name="Vehicles")
        show_chart(px.pie(reuse, names="Type", values="Vehicles", hole=.58, title="Vehicle reusability", color_discrete_sequence=["#62ddff","#ffc46b","#a994ff"]))
    rocket_detail_left, rocket_detail_right = st.columns(2)
    with rocket_detail_left:
        mission_rockets = filtered.groupby("Rocket").size().nlargest(15).sort_values().reset_index(name="Missions")
        rocket_use = px.bar(mission_rockets, x="Missions", y="Rocket", orientation="h", text="Missions", title="Most frequently used rockets", color="Missions", color_continuous_scale=["#104b54", "#62ddff"])
        rocket_use.update_coloraxes(showscale=False); show_chart(rocket_use, height=420)
    with rocket_detail_right:
        rocket_summary = filtered.groupby("Rocket").agg(Launches=("Rocket", "count"), Country=("Country", "first"), Reusable=("reusable", "first"), Avg_Payload=("Payload_Mass_kg", "mean"), Success_Rate=("Mission_Success", "mean")).reset_index().nlargest(10, "Launches")
        summary_chart = px.bar(rocket_summary, x="Rocket", y="Launches", color="Success_Rate", hover_data=["Country", "Reusable", "Avg_Payload"], title="Rocket reliability and launch volume", color_continuous_scale=["#a994ff", "#62ddff"])
        show_chart(summary_chart, height=420)
    leading_rocket = filtered["Rocket"].value_counts().index[0]
    story_signal("VEHICLE SIGNAL", f"{leading_rocket} appears most often in the selected mission history.", "Read that frequency beside reusability and success rate: the strongest vehicle story is where repetition meets reliability.", "rocket")
    

elif opt == "Space Economy":
    st.title("Space Economy")
    chapter_story("CHAPTER 05 / VALUE BEYOND ORBIT", "Exploration becomes infrastructure, then becomes opportunity.", "Follow the money, services, launches, and investment that turn space activity into systems people use on Earth.", "◇", "green")
    for col, item in zip(st.columns(3), [("RECORDS",economy.shape[0],"Economic observations"),("METRICS",economy.shape[1],"Available indicators"),("LATEST YEAR",int(economy.Year.max()),"Most recent record")]):
        with col: card(*item)
    st.markdown('<div class="section-divider">Market trajectory</div>', unsafe_allow_html=True)
    economy_view = economy[economy["Year"].between(year[0], year[1])].copy()
    if economy_view.empty:
        st.info("No space economy observations fall within the selected mission year range.")
        economy_view = economy.copy()
    economy_left, economy_right = st.columns(2)
    with economy_left:
        st.caption("The overall value of the global space economy across the selected years.")
        show_chart(px.line(economy_view, x="Year", y="Global_Space_Economy_USD", markers=True, title="Global space economy growth", color_discrete_sequence=["#62ddff"]))
    with economy_right:
        st.caption("Launch activity is one visible measure of the industry's operational scale.")
        show_chart(px.bar(economy_view, x="Year", y="Orbital_Launches", color="Economy_Growth_Rate", title="Orbital launches by year", color_continuous_scale=["#403180","#62ddff"]))

    st.markdown('<div class="section-divider">Where the value is</div>', unsafe_allow_html=True)
    segment_columns = ["Satellite_Services_USD", "Launch_Services_USD", "Satellite_Manufacturing_USD", "Ground_Equipment_USD"]
    segment_labels = {"Satellite_Services_USD":"Satellite services", "Launch_Services_USD":"Launch services", "Satellite_Manufacturing_USD":"Satellite manufacturing", "Ground_Equipment_USD":"Ground equipment"}
    segment_view = economy_view.melt(id_vars="Year", value_vars=segment_columns, var_name="Segment", value_name="Value (USD)")
    segment_view["Segment"] = segment_view["Segment"].map(segment_labels)
    value_left, value_right = st.columns(2)
    with value_left:
        st.caption("Four measured segments show how activity is distributed across the space economy.")
        segment_chart = px.bar(segment_view, x="Year", y="Value (USD)", color="Segment", barmode="stack", title="Space economy composition by segment", color_discrete_sequence=["#62ddff", "#a994ff", "#6ee7b7", "#ffc46b"])
        show_chart(segment_chart, height=380)
    with value_right:
        st.caption("The commercial and government shares show the changing structure of the market.")
        share_view = economy_view.melt(id_vars="Year", value_vars=["Commercial Share %", "Government Share %"], var_name="Share", value_name="Percent")
        share_chart = px.line(share_view, x="Year", y="Percent", color="Share", markers=True, title="Commercial and government market share", color_discrete_map={"Commercial Share %":"#62ddff", "Government Share %":"#a994ff"})
        share_chart.update_yaxes(range=[0, 100], ticksuffix="%")
        show_chart(share_chart, height=380)

    st.markdown('<div class="section-divider">Capital and operating scale</div>', unsafe_allow_html=True)
    scale_left, scale_right = st.columns(2)
    with scale_left:
        st.caption("Private investment and venture deal volume trace the flow of commercial capital.")
        capital_chart = px.line(economy_view, x="Year", y="Private_Investment_USD", markers=True, title="Private investment and venture activity", color_discrete_sequence=["#6ee7b7"])
        capital_chart.add_scatter(x=economy_view["Year"], y=economy_view["VC_Deals"], mode="lines+markers", name="VC deals", yaxis="y2", line=dict(color="#62ddff", width=3), hovertemplate="Year %{x}<br>VC deals %{y}<extra></extra>")
        capital_chart.update_layout(yaxis_title="Private investment (USD)", yaxis2=dict(title="VC deals", overlaying="y", side="right", showgrid=False))
        show_chart(capital_chart, height=380)
    with scale_right:
        st.caption("Each point compares launch cadence, satellite deployment, investment, and commercial participation.")
        scale_chart = px.scatter(economy_view, x="Orbital_Launches", y="Satellites_Deployed", size="Private_Investment_USD", color="Commercial Share %", hover_name="Year", hover_data=["VC_Deals", "Major_Operators", "Global_Space_Economy_USD"], title="Launches, deployed satellites, and investment", color_continuous_scale=["#403180", "#62ddff"])
        show_chart(scale_chart, height=380)

    st.markdown('<div class="section-divider">Growth signals</div>', unsafe_allow_html=True)
    growth_left, growth_right = st.columns(2)
    with growth_left:
        st.caption("Year-over-year growth shows when the market accelerated or settled.")
        growth_chart = px.bar(economy_view.dropna(subset=["Economy_Growth_Rate"]), x="Year", y="Economy_Growth_Rate", color="Economy_Growth_Rate", title="Economic growth rate by observation", color_continuous_scale=["#174b66", "#6ee7b7"])
        growth_chart.update_coloraxes(showscale=False)
        show_chart(growth_chart, height=350)
    with growth_right:
        st.caption("Investment per launch puts capital intensity alongside the industry's operating tempo.")
        intensity_chart = px.line(economy_view, x="Year", y="Investment_per_Launch", markers=True, title="Private investment per orbital launch", color_discrete_sequence=["#6ee7b7"])
        show_chart(intensity_chart, height=350)

    latest_economy = economy_view.sort_values("Year").iloc[-1]
    top_segment = max(segment_columns, key=lambda column: latest_economy[column])
    st.markdown(f'<div class="data-signal economy-signal"><span>MARKET SIGNAL</span><strong>In {int(latest_economy["Year"])}, {segment_labels[top_segment].lower()} was the largest measured segment at ${latest_economy[top_segment]:,.1f} in the dataset&apos;s reported USD units.</strong><p>The same observation records a {latest_economy["Commercial Share %"]:.0f}% commercial share, showing how the market mix has shifted in the available data.</p></div>', unsafe_allow_html=True)



elif opt == "Dataset":
    st.title("Welcome to the Dataset Explorer")
    chapter_story("THE EVIDENCE ROOM", "Four datasets. One connected universe.", "Move from raw records to cleaned signals, then return to the story with a clearer view of what each dataset can reveal.", "⌁", "cyan")
    st.markdown('<div class="source-ticker dataset-source-ticker"><div class="source-ticker-label">DATA SOURCES</div><div class="source-ticker-window"><div class="source-ticker-track"><span>NASA OPEN DATA</span><b>/</b><span>EUROPEAN SPACE AGENCY (ESA)</span><b>/</b><span>UNITED NATIONS OFFICE FOR OUTER SPACE AFFAIRS (UNOOSA)</span><b>/</b><span>PUBLIC ROCKET LAUNCH DATABASES</span><b>/</b><span>GOVERNMENT REPORTS &amp; COMMERCIAL INDUSTRY PUBLICATIONS</span><b>/</b><span>DATA CLEANED, STANDARDIZED &amp; INTEGRATED FOR ANALYSIS</span><b>/</b><span>NASA OPEN DATA</span><b>/</b><span>EUROPEAN SPACE AGENCY (ESA)</span><b>/</b><span>UNITED NATIONS OFFICE FOR OUTER SPACE AFFAIRS (UNOOSA)</span><b>/</b></div></div></div>', unsafe_allow_html=True)
    dataset_views = [
        ("overview", "◉", "Overview"),
        ("viewer", "✦", "Viewer"),
        ("nulls", "◎", "Nulls"),
        ("summary", "✧", "Summary"),
    ]
    if "dataset_view" not in st.session_state:
        st.session_state.dataset_view = "overview"
    st.markdown('<span class="dataset-nav-marker" aria-hidden="true"></span>', unsafe_allow_html=True)
    dataset_columns = st.columns(4, gap="small")
    for column, (view_id, icon, label) in zip(dataset_columns, dataset_views):
        with column:
            dataset_view_button(view_id, icon, label)
    datasets = {"AI Missions":{"raw":df1,"clean":df}, "Rocket Dataset":{"raw":df2,"clean":rockets}, "AI Spacecraft":{"raw":df3,"clean":ai1}, "Space Economy":{"raw":df4,"clean":economy}}
    if st.session_state.dataset_view == "overview":
        st.markdown("""
<div class="cosmic-roadmap">

<h2 class="cosmic-title">
Journey Through the Data Universe
</h2>

<div class="journey">

<div class="journey-node">

<div class="node-orbit">
<span class="node-number">01</span>
<span class="node-icon">🌍</span>
</div>

<h3>Where It All Began</h3>

<p>
Historical missions reveal how humanity first reached beyond Earth.
</p>

<div class="node-label">
Mission History
</div>

</div>


<div class="journey-node">

<div class="node-orbit">
<span class="node-number">02</span>
<span class="node-icon">🚀</span>
</div>

<h3>Powering Exploration</h3>

<p>
Rocket technology transformed ambition into repeatable exploration.
</p>

<div class="node-label">
Rocket Database
</div>

</div>


<div class="journey-node">

<div class="node-orbit">
<span class="node-number">03</span>
<span class="node-icon">🤖</span>
</div>

<h3>Intelligence Takes Flight</h3>

<p>
AI is changing how spacecraft explore, operate and make decisions.
</p>

<div class="node-label">
AI in Space
</div>

</div>


<div class="journey-node">

<div class="node-orbit">
<span class="node-number">04</span>
<span class="node-icon">💰</span>
</div>

<h3>The Space Economy</h3>

<p>
Exploration evolves into markets, investment and commercial growth.
</p>

<div class="node-label">
Future Economy
</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)
    elif st.session_state.dataset_view == "viewer":
        name = st.selectbox("Select Dataset", list(datasets), key="viewer")
        raw = datasets[name]["raw"]
        for col, (label, value) in zip(st.columns(4), [("Rows",raw.shape[0]),("Columns",raw.shape[1]),("Numeric Features",raw.select_dtypes(include="number").shape[1]),("Categorical Features",raw.select_dtypes(exclude="number").shape[1])]):
            with col: st.metric(label, value)
        shown = st.slider("Rows to Display", 5, min(100, len(raw)), min(10, len(raw)))
        st.dataframe(raw.head(shown), use_container_width=True, hide_index=True)
    elif st.session_state.dataset_view == "nulls":
        name = st.selectbox("Select Dataset", list(datasets), key="nulls")
        raw, clean = datasets[name]["raw"], datasets[name]["clean"]
        missing = raw.isna().sum().sum()
        for col, (label, value) in zip(st.columns(3), [("Missing Values",f"{missing:,}"),("Columns with Nulls",(raw.isna().sum()>0).sum()),("Completeness",f"{(1-missing/raw.size)*100:.2f}%")]):
            with col: st.metric(label, value)
        missing_df = raw.isna().sum().loc[lambda x: x > 0].rename("Missing Count").reset_index()
        missing_df.columns = ["Column Name", "Missing Count"]
        if missing_df.empty: st.success("No missing values found in this dataset.")
        else: st.dataframe(missing_df, use_container_width=True, hide_index=True)
        st.subheader("After Cleaning")
        st.metric("Completeness", f"{(1-clean.isna().sum().sum()/clean.size)*100:.2f}%")

    elif st.session_state.dataset_view == "summary":
        st.markdown('<div class="summary-connection" aria-hidden="true"><i></i><b></b><i></i><b></b><i></i><b></b><i></i></div>', unsafe_allow_html=True)
        col1,col2,col3,col4 = st.columns(4, gap="medium")

        cards = [
        ("📂","Datasets","4"),
        ("📈","Records","6480+"),
        ("🌍","Domains","4"),
        ("✅","Status","Processed")
        ]

        for col,(icon,label,value) in zip([col1,col2,col3,col4],cards):
            with col:
                st.markdown(f"""
                <div class="square-card summary-card">
                    <div class="square-icon">{icon}</div>
                    <div class="square-value">{value}</div>
                    <div class="square-title">{label}</div>
                </div>
                """,unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        c3,c4 = st.columns(2)

        with c1:
                    st.markdown("""
                <div class="dataset-card">
                <h3>🛰 Space Missions</h3>
                <h6>6418 Historical Launch Records</h6>

                • Mission Name<br>
                • Launch Date<br>
                • Launch Country<br>
                • Space Agency<br>
                • Mission Status<br>
                • Failure Reason
                </div>
                """,unsafe_allow_html=True)

        with c2:
                    st.markdown("""
                <div class="dataset-card">
                <h3>🚀 Rocket Database</h3>
                <h6>23 Rocket Profiles</h6>

                • Rocket Family<br>
                • Manufacturer<br>
                • Payload Capacity<br>
                • Cost per Kg<br>
                • Reusability<br>
                • Rocket Status
                </div>
                """,unsafe_allow_html=True)

        with c3:
                    st.markdown("""
                <div class="dataset-card">
                <h3>🤖 AI in Space</h3>
                <h6>25 AI Applications</h6>

                • AI Technology<br>
                • Mission<br>
                • Space Agency<br>
                • AI Role<br>
                • Category
                </div>
                """,unsafe_allow_html=True)

        with c4:
                    st.markdown("""
                <div class="dataset-card">
                <h3>💰 Space Economy</h3>
                <h6>14 Economic Indicators</h6>

                • Market Size<br>
                • Investments<br>
                • Commercial Share<br>
                • Government Spending<br>
                • Growth Rate
                </div>
                """,unsafe_allow_html=True)

        st.markdown("""
            <div class="control-panel">

            <div>
            <span class="control-label">PRIMARY DATASET</span>
            <strong>Space Missions (6418)</strong>
            </div>

            <div>
            <span class="control-label">SECONDARY DATASETS</span>
            <strong>Rockets • AI • Economy</strong>
            </div>

            <div>
            <span class="control-label">PROCESSING STATUS</span>
            <strong>✔ Cleaned & Analysis Ready</strong>
            </div>

            </div>
            """, unsafe_allow_html=True)

elif opt=="AI in Space":
    st.markdown(f"""<div class="ai-space-page"><div class="ai-hero"><div class="ai-hero-left"><div class="ai-eyebrow">◉ SPACE INTELLIGENCE / AI MISSION CONTROL</div><h1>Artificial Intelligence <span>Beyond Earth</span></h1><h3>Explore how artificial intelligence is transforming spacecraft, autonomous missions, scientific discovery and the future of space exploration.</h3><div class="ai-hero-line"></div><div class="ai-period"><span>MISSION ERA</span><strong>{ai1['year'].min()} — {ai1['year'].max()}</strong></div></div><div class="ai-orbit-visual"><div class="orbit-ring ring-one"></div><div class="orbit-ring ring-two"></div><div class="orbit-ring ring-three"></div><div class="orbit-core"><div class="core-icon">🧠</div><span>AI</span></div><div class="orbit-node node-one">🚀</div><div class="orbit-node node-two">🌍</div><div class="orbit-node node-three">⚙️</div><div class="orbit-node node-four">🛰️</div></div></div><div class="telemetry-section"><div class="section-label">LIVE MISSION TELEMETRY</div><div class="telemetry-grid"><div class="telemetry-item"><span class="telemetry-value">{ai1["mission_or_program"].nunique()}</span><span class="telemetry-label">AI MISSIONS</span></div><div class="telemetry-item"><span class="telemetry-value">{ai1["agency"].nunique()}</span><span class="telemetry-label">SPACE AGENCIES</span></div><div class="telemetry-item"><span class="telemetry-value">{ai1["country"].nunique()}</span><span class="telemetry-label">COUNTRIES</span></div><div class="telemetry-item"><span class="telemetry-value">{ai1["tech_name"].nunique()}</span><span class="telemetry-label">AI TECHNOLOGIES</span></div><div class="telemetry-item"><span class="telemetry-value">{ai1["accuracy_pct"].mean():.1f}%</span><span class="telemetry-label">AVG ACCURACY</span></div><div class="telemetry-item"><span class="telemetry-value">{ai1["data_volume_gb"].mean():.1f}<small> GB</small></span><span class="telemetry-label">AVG DATA VOLUME</span></div></div></div></div>""",unsafe_allow_html=True)
    chapter_story("CHAPTER 04 / INTELLIGENCE TAKES FLIGHT", "When distance grows, intelligence becomes the mission partner.", "AI gives spacecraft a way to sense, classify, adapt, and act when human operators are millions of kilometres away.", "∿", "violet")

    st.markdown("""<div class="ai-section-heading"><div><div class="section-kicker">MISSION EVOLUTION</div><h2>AI activity across the space era</h2></div><div class="section-tag">TEMPORAL INTELLIGENCE</div></div>""",unsafe_allow_html=True)
    ai_space=ai1.copy()
    ai_space=ai_space[(ai_space["year"]>=year[0])&(ai_space["year"]<=year[1])]
    if countries: ai_space=ai_space[ai_space["country"].isin(countries)]
    if agencies: ai_space=ai_space[ai_space["agency"].isin(agencies)]
    if ai_filter=="Yes": ai_space=ai_space[ai_space["open_source"]==1]
    elif ai_filter=="No": ai_space=ai_space[ai_space["open_source"]==0]
    if ai_space.empty:
        st.info("No AI records match the current mission filters. Showing the complete AI dataset for context.")
        ai_space = ai1.copy()
    st.markdown("""<div class="ai-section-heading"><div><div class="section-kicker">MISSION EVOLUTION</div><h2>AI activity across the space era</h2></div><div class="section-tag">TEMPORAL INTELLIGENCE</div></div>""",unsafe_allow_html=True)

    yearly_ai=ai_space.groupby("year").size().reset_index(name="missions")
    fig_ai_timeline=px.area(yearly_ai,x="year",y="missions",markers=True)
    fig_ai_timeline.update_traces(line=dict(width=3),marker=dict(size=7))
    fig_ai_timeline.update_layout(height=350,margin=dict(l=10,r=10,t=20,b=10),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",font=dict(family="Arial",color="#dfe7ff"),xaxis=dict(title="Mission Year",gridcolor="rgba(120,140,190,.12)",zeroline=False),yaxis=dict(title="AI Missions",gridcolor="rgba(120,140,190,.12)",zeroline=False),hovermode="x unified")
    st.plotly_chart(fig_ai_timeline,use_container_width=True,config={"displayModeBar":False})

    left,right=st.columns([1.15,.85])

    with left:
        st.markdown("""<div class="intelligence-panel"><div class="panel-kicker">AI TECHNOLOGY LANDSCAPE</div><h2>Where intelligence is being applied</h2><p class="panel-description">The technology layer behind modern space missions.</p></div>""",unsafe_allow_html=True)
        tech_data=ai_space["ai_category"].value_counts().reset_index()
        tech_data.columns=["category","count"]
        fig_tech=px.bar(tech_data,x="count",y="category",orientation="h",text="count")
        fig_tech.update_traces(textposition="outside")
        fig_tech.update_layout(height=330,margin=dict(l=10,r=40,t=10,b=10),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",font=dict(color="#dfe7ff"),xaxis=dict(showgrid=False,title=""),yaxis=dict(title="",categoryorder="total ascending"))
        st.plotly_chart(fig_tech,use_container_width=True,config={"displayModeBar":False})

    with right:
        st.markdown(f"""<div class="ecosystem-panel"><div class="panel-kicker">MISSION SIGNAL</div><div class="signal-orbit"><div class="signal-ring"></div><div class="signal-core">AI</div><div class="signal-point p1">MISSIONS</div><div class="signal-point p2">ROBOTICS</div><div class="signal-point p3">VISION</div><div class="signal-point p4">AUTONOMY</div></div><div class="signal-summary"><strong>{ai1["ai_category"].nunique()}</strong><span>AI APPLICATION CATEGORIES</span></div></div>""",unsafe_allow_html=True)

    st.markdown('<div class="section-divider">Where AI is making an impact</div>', unsafe_allow_html=True)
    impact_left, impact_right = st.columns(2)
    with impact_left:
        st.caption("Subcategories show the specific mission tasks represented within the AI records.")
        subcategories = ai_space["ai_subcategory"].value_counts().head(10).sort_values().reset_index()
        subcategories.columns = ["AI subcategory", "Records"]
        subcategory_chart = px.bar(subcategories, x="Records", y="AI subcategory", orientation="h", title="Most represented AI mission tasks", color="Records", color_continuous_scale=["#253779", "#62ddff"], hover_data={"Records":True})
        subcategory_chart.update_coloraxes(showscale=False)
        show_chart(subcategory_chart, height=390)
    with impact_right:
        st.caption("This map compares the AI roles represented by each country in the selected records.")
        geography_chart = px.density_heatmap(ai_space, x="country", y="ai_category", title="AI application categories by country", color_continuous_scale=["#0c163b", "#2c559a", "#62ddff"], labels={"country":"Country", "ai_category":"AI category", "count":"Records"})
        show_chart(geography_chart, height=390)

    st.markdown('<div class="section-divider">The AI landscape</div>', unsafe_allow_html=True)
    landscape_left, landscape_right = st.columns(2)
    with landscape_left:
        st.caption("Agency representation identifies the organizations attached to the most AI records.")
        agencies_ai = ai_space["agency"].value_counts().head(10).sort_values().reset_index()
        agencies_ai.columns = ["Agency", "Records"]
        agency_chart = px.bar(agencies_ai, x="Records", y="Agency", orientation="h", title="Agencies represented in AI mission records", color="Records", color_continuous_scale=["#403180", "#a994ff", "#62ddff"])
        agency_chart.update_coloraxes(showscale=False)
        show_chart(agency_chart, height=390)
    with landscape_right:
        st.caption("The dataset records whether an AI application is open-source or not.")
        openness = ai_space["open_source"].map({1:"Open-source", 0:"Not open-source"}).value_counts().rename_axis("Availability").reset_index(name="Records")
        openness_chart = px.pie(openness, names="Availability", values="Records", hole=.6, title="Open-source availability", color="Availability", color_discrete_map={"Open-source":"#62ddff", "Not open-source":"#a994ff"})
        show_chart(openness_chart, height=390)

    st.markdown('<div class="section-divider">Patterns in the data</div>', unsafe_allow_html=True)
    pattern_left, pattern_right = st.columns(2)
    with pattern_left:
        st.caption("Accuracy and data volume reveal the spread of recorded AI application profiles.")
        accuracy_chart = px.scatter(ai_space, x="data_volume_gb", y="accuracy_pct", color="ai_category", size="data_volume_gb", hover_name="mission_or_program", hover_data=["tech_name", "algorithm_type", "agency", "year"], title="Accuracy and data volume by AI application", labels={"data_volume_gb":"Data volume (GB)", "accuracy_pct":"Accuracy (%)", "ai_category":"AI category"}, color_discrete_sequence=px.colors.qualitative.Pastel)
        show_chart(accuracy_chart, height=410)
    with pattern_right:
        st.caption("Stacked records show which application categories appear in each mission year.")
        category_year = ai_space.groupby(["year", "ai_category"]).size().reset_index(name="Records")
        category_year_chart = px.bar(category_year, x="year", y="Records", color="ai_category", barmode="stack", title="AI application categories across mission years", labels={"year":"Mission year", "ai_category":"AI category"}, color_discrete_sequence=px.colors.qualitative.Set3)
        show_chart(category_year_chart, height=410)

    leading_category = ai_space["ai_category"].value_counts().index[0]
    leading_category_count = ai_space["ai_category"].value_counts().iloc[0]
    open_source_share = ai_space["open_source"].mean() * 100
    st.markdown(f'<div class="data-signal ai-signal"><span>INTELLIGENCE SIGNAL</span><strong>{leading_category} is the most represented AI category, appearing in {leading_category_count} of {len(ai_space)} selected records.</strong><p>{open_source_share:.0f}% of the selected applications are recorded as open-source, adding context on how these capabilities are made available.</p></div>', unsafe_allow_html=True)
elif opt == "About":
    st.title("About Space Insights")
    st.markdown("A mission analytics workspace connecting launches, rockets, artificial intelligence, and the global space economy.")
    st.markdown("""
    <div class="section-divider">🚀 ABOUT THE PROJECT</div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="source-ticker"><div class="source-ticker-label">DATA SOURCES</div><div class="source-ticker-window"><div class="source-ticker-track"><span>NASA OPEN DATA</span><b>/</b><span>EUROPEAN SPACE AGENCY (ESA)</span><b>/</b><span>UNITED NATIONS OFFICE FOR OUTER SPACE AFFAIRS (UNOOSA)</span><b>/</b><span>PUBLIC ROCKET LAUNCH DATABASES</span><b>/</b><span>GOVERNMENT REPORTS &amp; COMMERCIAL INDUSTRY PUBLICATIONS</span><b>/</b><span>DATA CLEANED, STANDARDIZED &amp; INTEGRATED FOR ANALYSIS</span><b>/</b><span>NASA OPEN DATA</span><b>/</b><span>EUROPEAN SPACE AGENCY (ESA)</span><b>/</b><span>UNITED NATIONS OFFICE FOR OUTER SPACE AFFAIRS (UNOOSA)</span><b>/</b></div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="about-uvp-line"><span>PROJECT UVP</span><strong>Turn space data into a story people can explore, understand, and remember.</strong></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="dataset-card">

    <h3>🌌 Global Space Mission Intelligence Dashboard</h3>

    <p>
    The <b>Global Space Mission Intelligence Dashboard</b> is an interactive data
    analytics platform that transforms decades of space exploration records into
    meaningful visual insights. Developed using <b>Python</b>, <b>Streamlit</b>,
    <b>Pandas</b> and <b>Plotly</b>, the dashboard combines historical missions,
    rocket technologies, AI innovations and the global space economy into one
    immersive analytical experience.
    </p>

    <h6>🎯 Purpose</h6>

    <p>
    Designed for students, researchers and space enthusiasts, the dashboard
    simplifies complex datasets into interactive stories that reveal how humanity
    has progressed from the first satellite launches to today's commercial space
    industry.
    </p>

    <hr>

    <div class="control-panel">

    <div>
    <span class="control-label">DATASETS</span>
    <strong>4 Integrated Space Datasets</strong>
    </div>

    <div>
    <span class="control-label">MISSIONS</span>
    <strong>6000+ Historical Launch Records</strong>
    </div>

    <div>
    <span class="control-label">TECH STACK</span>
    <strong>Python • Streamlit • Plotly • Pandas</strong>
    </div>

    </div>

    <div class="about-rocket-route" aria-hidden="true"><span class="about-rocket">🚀</span><i></i><b>MISSION ROUTE ACTIVE</b><i></i></div>

    <h6>🔭 Dashboard Modules</h6>

    <ul>
    <li>Start Here — project story and orientation</li>
    <li>Home — global mission overview</li>
    <li>Missions — historical mission intelligence</li>
    <li>Rockets — vehicle performance and reuse</li>
    <li>AI in Space — intelligent mission systems</li>
    <li>Space Economy — market and investment signals</li>
    <li>Dataset — explore, inspect, and validate records</li>
    <li>Mission Lab — design and test a mission profile</li>
    </ul>
    <div class="workflow-title">
    ⚙ Workflow Pipeline
    </div>

    <div class="workflow">

    <div class="step">
    <div class="icon">📥</div>
    <h4>    Dataset Collection</h4>
    <p></p>
    </div>

    <div class="arrow">➜</div>

    <div class="step">
    <div class="icon">🧹</div>
    <h4>Data Cleaning</h4>
    <p></p>
    </div>

    <div class="arrow">➜</div>

    <div class="step">
    <div class="icon">⚙️</div>
    <h4>Feature Engineering</h4>
    <p></p>
    </div>

    <div class="arrow">➜</div>

    <div class="step">
    <div class="icon">📊</div>
    <h4>EDA Analysis</h4>
    <p></p>
    </div>

    <div class="arrow">➜</div>

    <div class="step">
    <div class="icon">📈</div>
    <h4>KPI Generation</h4>
    <p></p>
    </div>

    <div class="arrow">➜</div>

    <div class="step">
    <div class="icon">📉</div>
    <h4>Interactive Visualizations</h4>
    <p></p>
    </div>

    <div class="arrow">➜</div>

    <div class="step">
    <div class="icon">🚀</div>
    <h4>Dashboard Development</h4>
    <p></p>
    </div>

    <div class="arrow">➜</div>

    <div class="step">
    <div class="icon">✨</div>
    <h4>User Experience</h4>
    <p></p>
    </div>

    </div>
    """, unsafe_allow_html=True)

else:
    st.title("About Space Insights")
    st.markdown("A mission analytics workspace connecting launches, rockets, artificial intelligence, and the global space economy.")
