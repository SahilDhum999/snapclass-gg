import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        stat_items = "".join(
            f'<div style="background:#EB459E10; padding:5px 12px; border-radius:12px; font-size:0.9rem;">'
            f"{icon} <b>{value}</b> {label}</div>"
            for icon, label, value in stats
        )
        stats_html = f'<div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:10px;">{stat_items}</div>'

    html = (
        '<div style="background:#FAF9F6; border-left:8px solid #EB459E; padding:25px; '
        'border-radius:20px; border:1px solid black; margin-bottom:20px;">'
        f'<h3 style="margin:0; color:#1e293b; font-size:1.5rem;">{name}</h3>'
        f'<p style="color:#64748b; margin:10px 0;">Code : '
        f'<span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px;">{code}</span>'
        f" | Section : {section}</p>"
        f"{stats_html}"
        "</div>"
    )

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()