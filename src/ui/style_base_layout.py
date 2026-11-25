import streamlit as st


def style_background_home():
    st.markdown("""
    <style>
    .stApp {
        background:#5865F2 !important;
    }
    .stApp div[data-testid="stColumn"] {
        background-color:#FAF9F6 !important;
        padding:2.5rem !important;
        border-radius:5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #E0E3FF !important;
        }

        .stApp h2.dashboard-brand-title {
            color: #5865F2 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700;9..144,800&display=swap');

    /* Hide Top Bar of Streamlit */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .block-container {
        padding-top: 1.5rem !important;
    }

    /* Apply Fraunces globally across headings, body, and widgets */
    html, body, .stApp,
    h1, h2, h3, h4, h5, h6,
    p, label, input, button, textarea, select,
    [data-testid="stHeadingWithActionElements"],
    [data-testid="stMarkdownContainer"] {
        font-family: 'Fraunces', Georgia, serif !important;
    }

    h1 {
        font-family: 'Fraunces', Georgia, serif !important;
        font-weight: 800 !important;
        font-size: 3.5rem !important;
        line-height: 1.2 !important;
        margin-bottom: 0rem !important;
        color: #1e293b !important;
    }

    h2 {
        font-family: 'Fraunces', Georgia, serif !important;
        font-weight: 800 !important;
        font-size: 2rem !important;
        line-height: 1.1 !important;
        margin-bottom: 0rem !important;
        color: #292929 !important;
    }

    h3, h4 {
        font-family: 'Fraunces', Georgia, serif !important;
        font-weight: 700 !important;
        color: #1e293b !important;
    }

    p {
        font-family: 'Fraunces', Georgia, serif !important;
    }

    /* Dark-mode contrast fix for subheaders ("Welcome, sahil"), labels ("Enter username", "Select Subject"), and text */
    .stApp [data-testid="stHeadingWithActionElements"] *,
    .stApp [data-testid="stWidgetLabel"],
    .stApp [data-testid="stWidgetLabel"] p,
    .stApp [data-testid="stWidgetLabel"] label,
    .stApp [data-testid="stWidgetLabel"] span,
    .stApp .stTextInput label,
    .stApp .stSelectbox label,
    .stApp .stCameraInput label,
    .stApp .stAudioInput label,
    .stApp [data-testid="stMarkdownContainer"] p {
        color: #1e293b !important;
    }

    /* Keep button text white despite the markdown/label dark color rules above */
    button,
    [data-testid="stBaseButton-primary"] {
        border-radius: 1.5rem !important;
        background: #5865F2 !important;
        color: white !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    button[kind="secondary"],
    [data-testid="stBaseButton-secondary"] {
        border-radius: 1.5rem !important;
        background: #EB459E !important;
        color: white !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    button[kind="tertiary"],
    [data-testid="stBaseButton-tertiary"] {
        border-radius: 1.5rem !important;
        background: black !important;
        color: white !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    /* Keep ALL button text white (overrides the .stApp markdown dark text rule above) */
    .stApp button,
    .stApp button *,
    .stApp button p,
    .stApp button span,
    .stApp button [data-testid="stMarkdownContainer"] p,
    .stApp [data-testid="stBaseButton-primary"] *,
    .stApp [data-testid="stBaseButton-secondary"] *,
    .stApp [data-testid="stBaseButton-tertiary"] * {
        color: #ffffff !important;
    }

    button:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)