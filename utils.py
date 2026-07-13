import streamlit as st


def section_title(title):
    """Display a section title with a divider."""
    st.divider()
    st.header(title)


def show_insight(text):
    """Display a business insight box."""
    st.info(f"**Business Insight**\n\n{text}")