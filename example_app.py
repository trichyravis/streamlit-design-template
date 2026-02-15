"""
The Mountain Path - Streamlit Design Template
Complete Example Application

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence

This example demonstrates all available components and styling options.
Use this as a reference when building your own applications.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from config import COLORS, BRANDING, get_page_config
from styles import apply_styles
from components import (
    header_container, sidebar_header, section_title, sidebar_section,
    metric_card, metric_card_advanced, info_box, formula_box,
    success_box, warning_box, error_box, footer, three_metric_row
)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(**get_page_config(
    title="Design Template Example",
    icon="🏔️"
))
apply_styles()

# ============================================================================
# HEADER
# ============================================================================
header_container(
    title="Mountain Path Design Template",
    subtitle="Complete Component Showcase & Style Guide",
    description="Demonstrates all available components, styling, and best practices"
)

# ============================================================================
# SIDEBAR
# ============================================================================
sidebar_header("DEMO CONTROLS", "Explore components")

sidebar_section("📊 Sample Parameters")
sample_slider = st.sidebar.slider("Sample Slider", 0.0, 100.0, 50.0, 1.0)
sample_select = st.sidebar.selectbox(
    "Sample Dropdown",
    ["Option 1", "Option 2", "Option 3"]
)

sidebar_section("🎨 Display Options")
show_charts = st.sidebar.checkbox("Show Charts", value=True)
show_tables = st.sidebar.checkbox("Show Tables", value=True)

# ============================================================================
# MAIN CONTENT - TABS
# ============================================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Components",
    "📈 Metrics & Cards",
    "📚 Info Boxes",
    "🎨 Styling Examples"
])

# ========== TAB 1: COMPONENTS ==========
with tab1:
    section_title("🎯 Header Components")
    
    st.write("**Standard Header** (already shown at top)")
    st.code('''
header_container(
    title="Your App Title",
    subtitle="Subtitle in gold",
    description="Additional description"
)
    ''')
    
    st.write("**Section Title**")
    section_title("📊 This is a Section Title")
    
    st.code('''section_title("📊 Your Section Name")''')
    
    # ---------------
    section_title("📊 Data Display Components")
    
    st.write("**DataFrame with Styling**")
    sample_df = pd.DataFrame({
        'Metric': ['VaR', 'Expected Shortfall', 'Volatility', 'Sharpe Ratio'],
        'Value': [2.34, 3.12, 18.5, 1.42],
        'Status': ['✓', '✓', '⚠', '✓']
    })
    st.dataframe(sample_df, use_container_width=True, hide_index=True)
    
    # ---------------
    section_title("📈 Charts & Visualizations")
    
    if show_charts:
        # Generate sample data
        x = np.linspace(0, 10, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(x, y1, label='Sin(x)', color=COLORS['accent_gold'], linewidth=2)
        ax.plot(x, y2, label='Cos(x)', color=COLORS['light_blue'], linewidth=2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Sample Chart with Mountain Path Colors')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        st.code('''
# Use Mountain Path colors in your charts
fig, ax = plt.subplots()
ax.plot(x, y, color=COLORS['accent_gold'], linewidth=2)
ax.grid(True, alpha=0.3)
st.pyplot(fig)
plt.close()
        ''')

# ========== TAB 2: METRICS & CARDS ==========
with tab2:
    section_title("💳 Metric Cards")
    
    st.write("**Basic Metric Cards**")
    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Portfolio VaR", "2.34%")
    with col2:
        metric_card("Expected Shortfall", "3.12%")
    with col3:
        metric_card("Sharpe Ratio", "1.42")
    
    st.code('''
col1, col2, col3 = st.columns(3)
with col1:
    metric_card("Label", "Value")
    ''')
    
    # ---------------
    section_title("📊 Advanced Metric Cards")
    
    st.write("**Metric Cards with Change Indicators**")
    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card_advanced("VaR", "2.34%", -0.12, "vs. yesterday")
    with col2:
        metric_card_advanced("Volatility", "18.5%", 0.34, "vs. last week")
    with col3:
        metric_card_advanced("Beta", "1.05", 0.02, "vs. benchmark")
    
    st.code('''
metric_card_advanced(
    label="VaR",
    value="2.34%",
    change=-0.12,  # Negative = improvement (green)
    change_label="vs. yesterday"
)
    ''')
    
    # ---------------
    section_title("⚡ Quick Three-Metric Row")
    
    st.write("**Convenient helper for three metrics**")
    three_metric_row([
        ("Alpha", "0.15%", "Annualized excess return"),
        ("Beta", "1.05", "Market sensitivity"),
        ("R²", "0.87", "Correlation strength")
    ])
    
    st.code('''
three_metric_row([
    ("Label 1", "Value 1", "Help text 1"),
    ("Label 2", "Value 2", "Help text 2"),
    ("Label 3", "Value 3", "Help text 3")
])
    ''')

# ========== TAB 3: INFO BOXES ==========
with tab3:
    section_title("ℹ️ Information Boxes")
    
    st.write("**Standard Info Box**")
    info_box("""
        <strong>Key Points:</strong>
        <ul>
            <li>Point 1: Important information here</li>
            <li>Point 2: Additional context</li>
            <li>Point 3: More details</li>
        </ul>
    """, title="Important Information")
    
    st.code('''
info_box("""
    <strong>Key Points:</strong>
    <ul>
        <li>Point 1</li>
        <li>Point 2</li>
    </ul>
""", title="Title Here")
    ''')
    
    # ---------------
    section_title("📐 Formula Boxes")
    
    st.write("**Display mathematical formulas**")
    formula_box(
        """VaR_α = μ + σ × z_α
        
where:
• μ = expected return
• σ = standard deviation  
• z_α = z-score at confidence level α""",
        description="Value at Risk calculation using normal distribution"
    )
    
    st.code('''
formula_box(
    "VaR_α = μ + σ × z_α",
    description="Variable definitions"
)
    ''')
    
    # ---------------
    section_title("🎨 Status Boxes")
    
    st.write("**Success, Warning, Error boxes**")
    
    success_box("Model estimation completed successfully!")
    warning_box("Low number of observations may affect accuracy")
    error_box("Insufficient data: need at least 100 observations")
    
    st.code('''
success_box("Success message")
warning_box("Warning message")
error_box("Error message")
    ''')

# ========== TAB 4: STYLING EXAMPLES ==========
with tab4:
    section_title("🎨 Color Palette")
    
    st.write("**Mountain Path Colors**")
    
    color_samples = [
        ("Dark Blue", COLORS['dark_blue'], "Primary brand"),
        ("Medium Blue", COLORS['medium_blue'], "Secondary brand"),
        ("Light Blue", COLORS['light_blue'], "Accents"),
        ("Gold", COLORS['accent_gold'], "Important elements"),
        ("Card Background", COLORS['card_bg'], "Containers"),
        ("Text Primary", COLORS['text_primary'], "Main text"),
    ]
    
    for name, hex_color, usage in color_samples:
        col1, col2, col3 = st.columns([2, 1, 3])
        with col1:
            st.markdown(f"**{name}**")
        with col2:
            st.markdown(
                f'<div style="background:{hex_color}; height:30px; border-radius:5px; '
                f'border:1px solid rgba(255,255,255,0.2);"></div>',
                unsafe_allow_html=True
            )
        with col3:
            st.code(f"{hex_color}  // {usage}")
    
    # ---------------
    section_title("📝 Typography Examples")
    
    st.markdown(f"""
    <div style="font-family: {FONTS['display']}; font-size: 2rem; color: {COLORS['accent_gold']};">
        Display Font: Playfair Display
    </div>
    <div style="font-family: {FONTS['body']}; font-size: 1rem; color: {COLORS['text_primary']}; margin-top: 1rem;">
        Body Font: Source Sans Pro - Used for paragraphs and UI elements
    </div>
    <div style="font-family: {FONTS['code']}; font-size: 0.9rem; color: {COLORS['text_primary']}; 
                margin-top: 1rem; background: rgba(0,0,0,0.3); padding: 0.5rem; border-radius: 5px;">
        Code Font: Source Sans Pro Monospace - For formulas and code
    </div>
    """, unsafe_allow_html=True)
    
    # ---------------
    section_title("🎭 Streamlit Native Elements")
    
    st.write("**Tabs** (styled automatically)")
    t1, t2, t3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    with t1:
        st.write("Content in Tab 1")
    
    st.write("**Expander** (styled automatically)")
    with st.expander("Click to expand"):
        st.write("Hidden content revealed!")
    
    st.write("**Native Metrics** (styled automatically)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Temperature", "70 °F", "1.2 °F")
    c2.metric("Wind", "9 mph", "-8%")
    c3.metric("Humidity", "86%", "4%")
    
    st.write("**Alerts** (styled automatically)")
    st.success("This is a success message")
    st.info("This is an info message")
    st.warning("This is a warning message")
    st.error("This is an error message")

# ============================================================================
# ADDITIONAL EXAMPLES
# ============================================================================

section_title("💡 Best Practices & Tips")

col1, col2 = st.columns(2)

with col1:
    info_box("""
        <strong>✅ DO:</strong>
        <ul>
            <li>Use <code>section_title()</code> for major sections</li>
            <li>Group metrics in rows of 3 with <code>three_metric_row()</code></li>
            <li>Use info boxes for important callouts</li>
            <li>Include help text on metric cards</li>
            <li>Close matplotlib figures after display</li>
        </ul>
    """, title="Best Practices")

with col2:
    info_box("""
        <strong>❌ DON'T:</strong>
        <ul>
            <li>Mix custom and native metric displays</li>
            <li>Forget to call <code>apply_styles()</code></li>
            <li>Override text colors in main area</li>
            <li>Use more than 3 columns for metrics</li>
            <li>Create duplicate component code</li>
        </ul>
    """, title="Common Pitfalls")

# ============================================================================
# CODE EXAMPLE
# ============================================================================

section_title("💻 Complete App Template")

st.write("Copy this template to start a new project:")

st.code('''
import streamlit as st
from config import get_page_config, COLORS
from styles import apply_styles
from components import header_container, sidebar_header, section_title, metric_card, footer

# Configure
st.set_page_config(**get_page_config("Your App", "🏔️"))
apply_styles()

# Header
header_container(
    title="Your App Title",
    subtitle="Description",
    description="Features"
)

# Sidebar
sidebar_header("CONTROLS")
param = st.sidebar.slider("Parameter", 0.0, 10.0, 5.0)

# Main content
section_title("📊 Results")

col1, col2, col3 = st.columns(3)
with col1:
    metric_card("Metric 1", "Value 1")
with col2:
    metric_card("Metric 2", "Value 2")
with col3:
    metric_card("Metric 3", "Value 3")

# Footer
footer()
''', language='python')

# ============================================================================
# FOOTER
# ============================================================================
footer()
