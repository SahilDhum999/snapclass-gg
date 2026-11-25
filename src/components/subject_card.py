import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    st.markdown(
        """
        <style>
        .snap-subject-card {
            background: #FAF9F6 !important;
            color: #1e293b !important;
            border-left: 8px solid #EB459E !important;
            padding: 25px !important;
            border-radius: 20px !important;
            border: 1px solid #0f172a !important;
            margin-bottom: 20px !important;
        }
        .snap-subject-title {
            margin: 0 !important;
            color: #0f172a !important;
            font-size: 1.5rem !important;
        }
        .snap-subject-meta {
            color: #475569 !important;
            margin: 10px 0 !important;
        }
        .snap-subject-code {
            background: #E0E3FF !important;
            color: #4338ca !important;
            padding: 2px 8px !important;
            border-radius: 5px !important;
            font-weight: 600 !important;
        }
        .snap-stat-pill {
            background: #FCE7F3 !important;
            color: #0f172a !important;
            padding: 5px 12px !important;
            border-radius: 12px !important;
            font-size: 0.9rem !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 5px !important;
        }
        .snap-stat-pill,
        .snap-stat-pill b,
        .snap-stat-pill span {
            color: #0f172a !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    stats_html = ""
    if stats:
        stat_items = "".join(
            f'<div class="snap-stat-pill">'
            f'<span>{icon}</span> <b>{value}</b> <span>{label}</span></div>'
            for icon, label, value in stats
        )
        stats_html = f'<div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:10px;">{stat_items}</div>'

    html = (
        '<div class="snap-subject-card">'
        f'<h3 class="snap-subject-title">{name}</h3>'
        f'<p class="snap-subject-meta">Code : '
        f'<span class="snap-subject-code">{code}</span>'
        f" | Section : {section}</p>"
        f"{stats_html}"
        "</div>"
    )

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()