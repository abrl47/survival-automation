import streamlit as st
import os

# --- GSC VERIFICATION (HTML FILE) ---
# If Google requests the verification file, serve it RAW
verification_file = "google09b49e61df880691.html"

# Check if the verification file exists and serve it
if os.path.exists(verification_file):
    with open(verification_file, "r") as f:
        content = f.read()
        # Serve as raw HTML with NO Streamlit wrapper
        st.set_page_config(
            page_title="GSC Verify",
            page_icon="",
            layout="centered",
            initial_sidebar_state="collapsed"
        )
        st.markdown(content, unsafe_allow_html=True)
        st.stop()  # Stops rendering the rest of the app

# --- NORMAL LANDING PAGE (if not verification request) ---
st.set_page_config(
    page_title="Survival Automation - Python + Spite",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Google Search Console meta tag (fallback)
st.markdown(
    '<meta name="google-site-verification" content="8T7T-TcZtbw7cQjNeDV232admv4DD_PdwuCd812wE8s" />',
    unsafe_allow_html=True
)

# [REST OF YOUR APP.PY CODE — the full landing page]
# (Copy and paste your existing landing page code here)