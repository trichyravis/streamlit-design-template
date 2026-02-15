"""
The Mountain Path - Streamlit Design Template
Components Module: Reusable UI Components

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence
"""

import streamlit as st
from config import COLORS, BRANDING, FONTS


# ============================================================================
# HEADER COMPONENTS
# ============================================================================

def header_container(title: str, subtitle: str = None, description: str = None):
    """
    Display main page header with Mountain Path branding.
    
    Parameters:
    -----------
    title : str
        Main title of the page/app
    subtitle : str, optional
        Subtitle line (shown in gold, larger font)
    description : str, optional
        Additional description line(s)
    
    Example:
    --------
    header_container(
        title="Portfolio Optimization Platform",
        subtitle="Modern Portfolio Theory & Mean-Variance Analysis",
        description="Efficient Frontier | Sharpe Ratio | Risk-Return Trade-offs"
    )
    """
    subtitle_html = f"""
        <p style="font-size:1rem; color:{COLORS['accent_gold']}; font-weight:600; margin:0.5rem 0;">
            {subtitle}
        </p>
    """ if subtitle else ""
    
    description_html = f"""
        <p style="font-size:0.85rem; color:{COLORS['text_primary']}; margin:0.3rem 0;">
            {description}
        </p>
    """ if description else ""
    
    st.markdown(f"""
    <div class="header-container">
        <h1>{BRANDING['icon']} {title}</h1>
        {subtitle_html}
        {description_html}
        <p>{BRANDING['name']}</p>
        <p style="font-size:0.8rem; color:{COLORS['text_secondary']};">
            {BRANDING['instructor']} | {BRANDING['credentials']}
        </p>
    </div>
    """, unsafe_allow_html=True)


def sidebar_header(title: str = "ANALYTICS", subtitle: str = None):
    """
    Display sidebar branding header.
    
    Parameters:
    -----------
    title : str, optional
        Main sidebar title (default: "ANALYTICS")
    subtitle : str, optional
        Subtitle text below title
    
    Example:
    --------
    sidebar_header("RISK ANALYTICS", "Advanced Financial Models")
    """
    subtitle_html = f"""
        <p style="color:{COLORS['text_secondary']}; font-size:0.75rem; margin:5px 0 0;">
            {subtitle}
        </p>
    """ if subtitle else ""
    
    st.sidebar.markdown(f"""
    <div style="text-align:center; padding:1.2rem; background:rgba(255,215,0,0.08);
         border-radius:10px; margin-bottom:1.5rem; border:2px solid {COLORS['accent_gold']};">
        <h3 style="color:{COLORS['accent_gold']}; margin:0;">{BRANDING['icon']} {title}</h3>
        {subtitle_html}
    </div>
    """, unsafe_allow_html=True)


def section_title(title: str):
    """
    Display section title with gold underline.
    
    Parameters:
    -----------
    title : str
        Section title text (can include emoji)
    
    Example:
    --------
    section_title("📊 Data Analysis")
    """
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def sidebar_section(title: str):
    """
    Display sidebar section header.
    
    Parameters:
    -----------
    title : str
        Section title with emoji
    
    Example:
    --------
    sidebar_section("📊 Stock Selection")
    """
    st.sidebar.markdown(
        f"<p style='color:{COLORS['accent_gold']}; font-weight:700;'>{title}</p>",
        unsafe_allow_html=True
    )


# ============================================================================
# METRIC COMPONENTS
# ============================================================================

def metric_card(label: str, value: str, help_text: str = None):
    """
    Display a metric card with label and value.
    
    Parameters:
    -----------
    label : str
        Metric label (displayed in small caps)
    value : str
        Metric value (displayed large in gold)
    help_text : str, optional
        Tooltip help text
    
    Example:
    --------
    metric_card("Portfolio VaR", "2.34%", "95% confidence level")
    """
    help_html = f' title="{help_text}"' if help_text else ''
    
    st.markdown(f"""
    <div class="metric-card"{help_html}>
        <div class="label">{label}</div>
        <div class="value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def metric_card_advanced(label: str, value: str, change: float = None, 
                        change_label: str = None):
    """
    Display metric card with optional change indicator.
    
    Parameters:
    -----------
    label : str
        Metric label
    value : str
        Current metric value
    change : float, optional
        Change amount (positive or negative)
    change_label : str, optional
        Label for change (e.g., "vs. yesterday")
    
    Example:
    --------
    metric_card_advanced("VaR", "2.34%", -0.12, "vs. yesterday")
    """
    change_html = ""
    if change is not None:
        color = COLORS['success'] if change < 0 else COLORS['danger']
        arrow = "↓" if change < 0 else "↑"
        change_text = f"{arrow} {abs(change):.2f}%"
        change_label_text = f" {change_label}" if change_label else ""
        
        change_html = f"""
        <div style="color:{color}; font-size:0.9rem; margin-top:0.3rem;">
            {change_text}{change_label_text}
        </div>
        """
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="label">{label}</div>
        <div class="value">{value}</div>
        {change_html}
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# INFO COMPONENTS
# ============================================================================

def info_box(content: str, title: str = None):
    """
    Display information box with optional title.
    
    Parameters:
    -----------
    content : str
        HTML content (can include lists, paragraphs, etc.)
    title : str, optional
        Box title (shown in gold)
    
    Example:
    --------
    info_box('''
        <strong>Key Points:</strong>
        <ul>
            <li>Point 1</li>
            <li>Point 2</li>
        </ul>
    ''', title="Important Information")
    """
    title_html = f"<h4 style='color:{COLORS['accent_gold']}; margin-top:0;'>{title}</h4>" if title else ""
    
    st.markdown(f"""
    <div class="info-box">
        {title_html}
        {content}
    </div>
    """, unsafe_allow_html=True)


def formula_box(formula: str, description: str = None):
    """
    Display mathematical formula in a styled box.
    
    Parameters:
    -----------
    formula : str
        Formula text (plain text or LaTeX)
    description : str, optional
        Formula description or variable definitions
    
    Example:
    --------
    formula_box(
        "VaR = μ + σ × z_α",
        "where μ = mean, σ = std dev, z_α = z-score"
    )
    """
    desc_html = f"<p style='margin-top:0.5rem; font-size:0.85rem;'>{description}</p>" if description else ""
    
    st.markdown(f"""
    <div class="formula-box">
        <pre style="margin:0;">{formula}</pre>
        {desc_html}
    </div>
    """, unsafe_allow_html=True)


def success_box(message: str):
    """Display success message in styled box."""
    st.markdown(f"""
    <div class="info-box" style="border-color:{COLORS['success']};">
        <span style="color:{COLORS['success']};">✓</span> {message}
    </div>
    """, unsafe_allow_html=True)


def warning_box(message: str):
    """Display warning message in styled box."""
    st.markdown(f"""
    <div class="info-box" style="border-color:{COLORS['warning']};">
        <span style="color:{COLORS['warning']};">⚠</span> {message}
    </div>
    """, unsafe_allow_html=True)


def error_box(message: str):
    """Display error message in styled box."""
    st.markdown(f"""
    <div class="info-box" style="border-color:{COLORS['danger']};">
        <span style="color:{COLORS['danger']};">✕</span> {message}
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# FOOTER COMPONENT
# ============================================================================

def footer(include_social: bool = True):
    """
    Display standard Mountain Path footer.
    
    Parameters:
    -----------
    include_social : bool, optional
        Include social media links (default: True)
    
    Example:
    --------
    footer()  # Standard footer with links
    footer(include_social=False)  # Minimal footer
    """
    social_html = ""
    if include_social:
        social_html = f"""
        <div style="margin-top:1rem; padding-top:1rem; border-top:1px solid rgba(255,215,0,0.3);">
            <p style="color:{COLORS['text_primary']}; font-size:0.9rem; margin:0.5rem 0;">
                <a href="{BRANDING['linkedin']}" target="_blank" 
                   style="color:{COLORS['accent_gold']}; text-decoration:none; margin:0 1rem;">
                    🔗 LinkedIn Profile
                </a>
                <a href="{BRANDING['github']}" target="_blank" 
                   style="color:{COLORS['accent_gold']}; text-decoration:none; margin:0 1rem;">
                    💻 GitHub
                </a>
            </p>
        </div>
        """
    
    st.divider()
    st.markdown(f"""
    <div style="text-align:center; padding:1.5rem;">
        <p style="color:{COLORS['accent_gold']}; font-family:{FONTS['display']}; 
                  font-weight:700; font-size:1.1rem; margin-bottom:0.5rem;">
            {BRANDING['icon']} {BRANDING['name']}
        </p>
        <p style="color:{COLORS['text_secondary']}; font-size:0.85rem; margin:0.3rem 0;">
            {BRANDING['instructor']} | {BRANDING['credentials']}
        </p>
        {social_html}
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# UTILITY COMPONENTS
# ============================================================================

def display_dataframe(df, title: str = None, caption: str = None):
    """
    Display DataFrame with optional title and caption.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to display
    title : str, optional
        Title above the table
    caption : str, optional
        Caption below the table
    """
    if title:
        section_title(title)
    if caption:
        st.caption(caption)
    st.dataframe(df, use_container_width=True)


def two_column_layout(left_content, right_content, ratio=[1, 1]):
    """
    Create two-column layout with custom content.
    
    Parameters:
    -----------
    left_content : callable
        Function to render left column content
    right_content : callable
        Function to render right column content
    ratio : list, optional
        Column width ratio (default: [1, 1])
    
    Example:
    --------
    def left():
        st.write("Left content")
    
    def right():
        st.write("Right content")
    
    two_column_layout(left, right, ratio=[2, 1])
    """
    col1, col2 = st.columns(ratio)
    with col1:
        left_content()
    with col2:
        right_content()


def three_metric_row(metrics: list):
    """
    Display three metrics in a row.
    
    Parameters:
    -----------
    metrics : list of tuples
        Each tuple: (label, value) or (label, value, help_text)
    
    Example:
    --------
    three_metric_row([
        ("VaR", "2.34%", "95% confidence"),
        ("ES", "3.12%", "Expected Shortfall"),
        ("Vol", "18.5%", "Annualized")
    ])
    """
    cols = st.columns(3)
    for i, metric_data in enumerate(metrics[:3]):
        with cols[i]:
            if len(metric_data) == 2:
                metric_card(metric_data[0], metric_data[1])
            else:
                metric_card(metric_data[0], metric_data[1], metric_data[2])


# ============================================================================
# EXPORT ALL
# ============================================================================
__all__ = [
    # Headers
    'header_container',
    'sidebar_header',
    'section_title',
    'sidebar_section',
    
    # Metrics
    'metric_card',
    'metric_card_advanced',
    
    # Info boxes
    'info_box',
    'formula_box',
    'success_box',
    'warning_box',
    'error_box',
    
    # Footer
    'footer',
    
    # Utilities
    'display_dataframe',
    'two_column_layout',
    'three_metric_row',
]
