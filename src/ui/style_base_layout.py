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

    /* Apply Fraunces globally */
    html, body, .stApp,
    h1, h2, h3, h4, h5, h6,
    p, label, input, button, textarea, select,
    [data-testid="stHeadingWithActionElements"],
    [data-testid="stMarkdownContainer"],
    [data-testid="stDialog"],
    div[role="dialog"],
    [data-testid^="stAlert"],
    div[role="alert"],
    div[data-baseweb="notification"],
    [data-testid="stToast"] {
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

    /* Subheaders, labels, captions, and markdown text (excluding buttons & alerts) */
    .stApp [data-testid="stHeadingWithActionElements"] *,
    .stApp [data-testid="stWidgetLabel"] *,
    .stApp .stTextInput label,
    .stApp .stSelectbox label,
    .stApp .stCameraInput label,
    .stApp .stAudioInput label,
    .stApp [data-testid="stCaptionContainer"] *,
    .stApp [data-testid="stMarkdownContainer"]:not(button *):not([data-testid^="stAlert"] *):not([role="alert"] *):not([data-baseweb="notification"] *) p {
        color: #1e293b !important;
        opacity: 1 !important;
    }

    /* All alert banners (st.error, st.warning, st.info, st.success) in RED with white text & clean single border */
    .stApp [data-testid^="stAlert"],
    .stApp div[role="alert"],
    .stApp div[data-baseweb="notification"],
    [data-testid="stDialog"] [data-testid^="stAlert"],
    [data-testid="stDialog"] div[role="alert"],
    [data-testid="stDialog"] div[data-baseweb="notification"],
    div[role="dialog"] [data-testid^="stAlert"],
    div[role="dialog"] div[role="alert"],
    div[role="dialog"] div[data-baseweb="notification"] {
        background: #DC2626 !important;
        background-color: #DC2626 !important;
        border: 1.5px solid #991B1B !important;
        border-radius: 14px !important;
        box-shadow: 0 6px 18px rgba(153, 27, 27, 0.22) !important;
    }

    .stApp [data-testid^="stAlert"] > div,
    .stApp div[role="alert"] > div,
    .stApp div[data-baseweb="notification"] > div,
    .stApp [data-testid^="stAlert"] [data-testid="stMarkdownContainer"],
    .stApp [data-testid^="stAlert"] p,
    div[role="dialog"] [data-testid^="stAlert"] > div,
    div[role="dialog"] div[role="alert"] > div,
    div[role="dialog"] div[data-baseweb="notification"] > div,
    div[role="dialog"] [data-testid^="stAlert"] [data-testid="stMarkdownContainer"],
    div[role="dialog"] [data-testid^="stAlert"] p {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }

    .stApp [data-testid^="stAlert"] *,
    .stApp div[role="alert"] *,
    .stApp div[data-baseweb="notification"] *,
    [data-testid="stDialog"] [data-testid^="stAlert"] *,
    [data-testid="stDialog"] div[role="alert"] *,
    [data-testid="stDialog"] div[data-baseweb="notification"] *,
    div[role="dialog"] [data-testid^="stAlert"] *,
    div[role="dialog"] div[role="alert"] *,
    div[role="dialog"] div[data-baseweb="notification"] * {
        color: #ffffff !important;
        fill: #ffffff !important;
        opacity: 1 !important;
    }

    /* Toasts */
    [data-testid="stToast"] {
        background: #FFFBEB !important;
        background-color: #FFFBEB !important;
        border: 1.5px solid #0f172a !important;
        border-radius: 14px !important;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.12) !important;
    }

    [data-testid="stToast"] * {
        color: #0F172A !important;
        fill: #0F172A !important;
        opacity: 1 !important;
    }

    /* @st.dialog modals */
    [data-testid="stDialog"] [role="dialog"],
    div[role="dialog"] {
        background-color: #FAF9F6 !important;
        color: #1e293b !important;
        border: 1px solid #0f172a !important;
        border-radius: 20px !important;
    }

    [data-testid="stDialog"] [data-testid="stHeadingWithActionElements"] *,
    [data-testid="stDialog"] [data-testid="stMarkdownContainer"]:not([data-testid^="stAlert"] *):not([role="alert"] *):not([data-baseweb="notification"] *):not(button *) *,
    [data-testid="stDialog"] [data-testid="stCaptionContainer"] *,
    [data-testid="stDialog"] [data-testid="stWidgetLabel"] *,
    div[role="dialog"] [data-testid="stHeadingWithActionElements"] *,
    div[role="dialog"] [data-testid="stMarkdownContainer"]:not([data-testid^="stAlert"] *):not([role="alert"] *):not([data-baseweb="notification"] *):not(button *) *,
    div[role="dialog"] [data-testid="stCaptionContainer"] *,
    div[role="dialog"] [data-testid="stWidgetLabel"] * {
        color: #1e293b !important;
        opacity: 1 !important;
    }

    /* Button styles */
    button,
    [data-testid="stBaseButton-primary"] {
        border-radius: 1.5rem !important;
        background: #5865F2 !important;
        color: #ffffff !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    button[kind="secondary"],
    [data-testid="stBaseButton-secondary"] {
        border-radius: 1.5rem !important;
        background: #EB459E !important;
        color: #ffffff !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    button[kind="tertiary"],
    [data-testid="stBaseButton-tertiary"] {
        border-radius: 1.5rem !important;
        background: black !important;
        color: #ffffff !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    /* Keep ALL button text white (including inside @st.dialog) */
    .stApp button,
    .stApp button *,
    .stApp button [data-testid="stMarkdownContainer"] *,
    .stApp [data-testid^="stBaseButton-"],
    .stApp [data-testid^="stBaseButton-"] *,
    [data-testid="stDialog"] button,
    [data-testid="stDialog"] button *,
    [data-testid="stDialog"] button [data-testid="stMarkdownContainer"] *,
    [data-testid="stDialog"] [data-testid^="stBaseButton-"] *,
    div[role="dialog"] button,
    div[role="dialog"] button *,
    div[role="dialog"] button [data-testid="stMarkdownContainer"] * {
        color: #ffffff !important;
        opacity: 1 !important;
    }

    button:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)