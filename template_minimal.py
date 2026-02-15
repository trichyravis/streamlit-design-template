"""
The Mountain Path - Streamlit App Template (Minimal)

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence

This is a minimal starting template for quickly building new Streamlit apps
with Mountain Path branding.
"""

import streamlit as st
import pandas as pd
import numpy as np

from config import COLORS, BRANDING, get_page_config
from styles import apply_styles
from components import header_container, sidebar_header, section_title, metric_card, footer

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(**get_page_config(
    title="Your App Name Here",
    icon="🏔️"
))
apply_styles()

# ============================================================================
# HEADER
# ============================================================================
header_container(
    title="Your Application Title",
    subtitle="Brief Description of Your App",
    description="Key Features | Capabilities | Methods"
)

# ============================================================================
# SIDEBAR
# ============================================================================
sidebar_header("CONTROLS", "Configure your analysis")

st.sidebar.markdown(f"<p style='color:{COLORS['accent_gold']}; font-weight:700;'>⚙️ Parameters</p>",
                    unsafe_allow_html=True)

# Add your sidebar controls here
param1 = st.sidebar.slider("Parameter 1", 0.0, 10.0, 5.0, 0.1)
param2 = st.sidebar.selectbox("Parameter 2", ["Option A", "Option B", "Option C"])

# ============================================================================
# MAIN CONTENT
# ============================================================================

# Example section
section_title("📊 Analysis Results")

# Example metrics
col1, col2, col3 = st.columns(3)
with col1:
    metric_card("Metric 1", "123.45")
with col2:
    metric_card("Metric 2", "67.89")
with col3:
    metric_card("Metric 3", "42.0")

# Add your main content here
st.write("Your main application content goes here...")

# Example data display
with st.expander("📈 Show Sample Data"):
    sample_data = pd.DataFrame({
        'Column 1': np.random.randn(10),
        'Column 2': np.random.randn(10),
        'Column 3': np.random.randn(10),
    })
    st.dataframe(sample_data, use_container_width=True)

# ============================================================================
# FOOTER
# ============================================================================
footer()
