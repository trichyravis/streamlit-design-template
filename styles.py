"""
The Mountain Path - Streamlit Design Template
Styling Module: CSS Injection and Custom Styles

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence
"""

import streamlit as st
from config import COLORS, FONTS, SPACING, BRANDING


def apply_styles():
    """
    Apply all custom CSS styling to Streamlit app.
    
    Call this function immediately after st.set_page_config() in your app.
    
    This function injects CSS that:
    - Sets background gradients
    - Forces light text in main area
    - Styles sidebar with Mountain Path branding
    - Creates custom component classes
    - Styles tabs, tables, and other Streamlit elements
    """
    st.markdown(f"""
    <style>
        /* ============================================================
           GOOGLE FONTS IMPORT
           ============================================================ */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+Pro:wght@300;400;600;700&display=swap');

        /* ============================================================
           MAIN APP BACKGROUND
           ============================================================ */
        .stApp {{
            background: linear-gradient(135deg, {COLORS['gradient_start']} 0%, {COLORS['gradient_mid']} 50%, {COLORS['gradient_end']} 100%);
        }}
        
        /* ============================================================
           TEXT COLOR ENFORCEMENT - CRITICAL FOR READABILITY
           ============================================================ */
        /* Force ALL text in main area to be light */
        .main {{
            color: {COLORS['text_primary']} !important;
        }}
        
        .main * {{
            color: {COLORS['text_primary']} !important;
        }}
        
        .main p, .main span, .main div, .main li, .main label {{
            color: {COLORS['text_primary']} !important;
        }}
        
        /* Headings in gold */
        .main h1, .main h2, .main h3, .main h4, .main h5, .main h6 {{
            color: {COLORS['accent_gold']} !important;
            font-family: {FONTS['display']};
        }}
        
        /* Markdown elements */
        .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown div {{
            color: {COLORS['text_primary']} !important;
        }}
        
        /* Text elements */
        [data-testid="stText"], [data-testid="stMarkdownContainer"] {{
            color: {COLORS['text_primary']} !important;
        }}

        /* ============================================================
           SIDEBAR STYLING
           ============================================================ */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {COLORS['bg_dark']} 0%, {COLORS['dark_blue']} 100%);
            border-right: 1px solid rgba(255,215,0,0.2);
        }}

        /* All sidebar text light colored */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] .stSlider label,
        section[data-testid="stSidebar"] .stNumberInput label,
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] .stMarkdown p,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] label {{
            color: {COLORS['text_primary']} !important;
        }}

        /* Sidebar input fields - keep dark text on white background */
        section[data-testid="stSidebar"] input {{
            color: {COLORS['text_dark']} !important;
            background-color: #ffffff !important;
        }}

        /* ============================================================
           HEADER CONTAINER
           ============================================================ */
        .header-container {{
            background: linear-gradient(135deg, {COLORS['dark_blue']}, {COLORS['medium_blue']});
            border: 2px solid {COLORS['accent_gold']};
            border-radius: {SPACING['border_radius']};
            padding: {SPACING['header_padding']};
            margin-bottom: {SPACING['section_margin']};
            text-align: center;
        }}
        
        .header-container h1 {{
            font-family: {FONTS['display']};
            color: {COLORS['accent_gold']};
            margin: 0;
            font-size: 2rem;
        }}
        
        .header-container p {{
            color: {COLORS['text_primary']};
            font-family: {FONTS['body']};
            margin: 0.3rem 0 0;
            font-size: 0.9rem;
        }}

        /* ============================================================
           METRIC CARDS
           ============================================================ */
        .metric-card {{
            background: {COLORS['card_bg']};
            border: 1px solid rgba(255,215,0,0.3);
            border-radius: {SPACING['border_radius']};
            padding: {SPACING['card_padding']};
            text-align: center;
            margin-bottom: 0.8rem;
        }}
        
        .metric-card .label {{
            color: {COLORS['text_secondary']};
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-family: {FONTS['body']};
        }}
        
        .metric-card .value {{
            color: {COLORS['accent_gold']};
            font-size: 1.6rem;
            font-weight: 700;
            font-family: {FONTS['display']};
            margin-top: 0.3rem;
        }}

        /* ============================================================
           INFO BOX
           ============================================================ */
        .info-box {{
            background: rgba(0,51,102,0.5);
            border: 1px solid {COLORS['accent_gold']};
            border-radius: {SPACING['border_radius_small']};
            padding: 1rem 1.5rem;
            font-family: {FONTS['body']};
            color: {COLORS['text_primary']};
            margin: 0.8rem 0;
        }}
        
        .info-box h3, .info-box h4 {{
            color: {COLORS['accent_gold']} !important;
            margin-top: 0;
        }}
        
        .info-box ul {{
            margin: 0.5rem 0;
            padding-left: 1.5rem;
        }}
        
        .info-box li {{
            margin: 0.3rem 0;
        }}

        /* ============================================================
           SECTION TITLE
           ============================================================ */
        .section-title {{
            font-family: {FONTS['display']};
            color: {COLORS['accent_gold']};
            font-size: 1.3rem;
            border-bottom: 2px solid rgba(255,215,0,0.3);
            padding-bottom: 0.5rem;
            margin: {SPACING['section_margin']} 0 1rem;
        }}

        /* ============================================================
           FORMULA BOX
           ============================================================ */
        .formula-box {{
            background: rgba(0,51,102,0.5);
            border: 1px solid {COLORS['accent_gold']};
            border-radius: {SPACING['border_radius_small']};
            padding: 1rem 1.5rem;
            font-family: {FONTS['code']};
            color: {COLORS['text_primary']};
            margin: 0.8rem 0;
        }}

        /* ============================================================
           TABS STYLING
           ============================================================ */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background: {COLORS['card_bg']};
            border: 1px solid rgba(255,215,0,0.3);
            border-radius: {SPACING['border_radius_small']};
            color: {COLORS['text_primary']};
            font-family: {FONTS['body']};
            padding: 0.5rem 1rem;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: {COLORS['dark_blue']};
            border: 2px solid {COLORS['accent_gold']};
            color: {COLORS['accent_gold']};
        }}

        /* ============================================================
           DATA TABLES
           ============================================================ */
        div[data-testid="stDataFrame"] {{
            border: 1px solid rgba(255,215,0,0.2);
            border-radius: {SPACING['border_radius_small']};
        }}
        
        /* ============================================================
           ALERT BOXES - Keep dark text for readability
           ============================================================ */
        .stAlert {{
            background-color: rgba(255, 255, 255, 0.95) !important;
        }}
        
        .stAlert p, .stAlert span, .stAlert div {{
            color: {COLORS['text_dark']} !important;
        }}
        
        /* ============================================================
           CODE BLOCKS
           ============================================================ */
        .stCodeBlock {{
            background: rgba(20, 30, 48, 0.8) !important;
            border: 1px solid rgba(255,215,0,0.2);
        }}
        
        .stCodeBlock code {{
            color: {COLORS['text_primary']} !important;
            background: transparent !important;
        }}
        
        pre {{
            background: rgba(20, 30, 48, 0.8) !important;
            color: {COLORS['text_primary']} !important;
        }}

        /* ============================================================
           BUTTONS
           ============================================================ */
        .stButton > button {{
            background: {COLORS['dark_blue']};
            color: {COLORS['text_primary']};
            border: 1px solid {COLORS['accent_gold']};
            border-radius: {SPACING['border_radius_small']};
            font-family: {FONTS['body']};
            transition: all 0.3s ease;
        }}
        
        .stButton > button:hover {{
            background: {COLORS['medium_blue']};
            border-color: {COLORS['accent_gold']};
            transform: translateY(-2px);
        }}

        /* ============================================================
           DIVIDERS
           ============================================================ */
        hr {{
            border: none;
            border-top: 1px solid rgba(255,215,0,0.3);
            margin: {SPACING['section_margin']} 0;
        }}

        /* ============================================================
           FOOTER
           ============================================================ */
        footer {{
            visibility: hidden;
        }}

        /* ============================================================
           EXPANDER
           ============================================================ */
        .streamlit-expanderHeader {{
            background: {COLORS['card_bg']};
            border: 1px solid rgba(255,215,0,0.3);
            border-radius: {SPACING['border_radius_small']};
            color: {COLORS['text_primary']};
        }}

        /* ============================================================
           DOWNLOAD BUTTON
           ============================================================ */
        .stDownloadButton > button {{
            background: {COLORS['dark_blue']};
            color: {COLORS['text_primary']};
            border: 1px solid {COLORS['accent_gold']};
        }}
        
        .stDownloadButton > button:hover {{
            background: {COLORS['medium_blue']};
        }}

        /* ============================================================
           FILE UPLOADER
           ============================================================ */
        [data-testid="stFileUploader"] {{
            background: {COLORS['card_bg']};
            border: 1px solid rgba(255,215,0,0.3);
            border-radius: {SPACING['border_radius_small']};
            padding: 1rem;
        }}

        /* ============================================================
           METRICS (Streamlit Native)
           ============================================================ */
        [data-testid="stMetricValue"] {{
            color: {COLORS['accent_gold']} !important;
            font-family: {FONTS['display']};
        }}
        
        [data-testid="stMetricLabel"] {{
            color: {COLORS['text_secondary']} !important;
        }}
    </style>
    """, unsafe_allow_html=True)


def inject_custom_css(css: str):
    """
    Inject additional custom CSS.
    
    Parameters:
    -----------
    css : str
        Custom CSS code to inject
    
    Usage:
    ------
    inject_custom_css('''
        .my-custom-class {
            color: red;
        }
    ''')
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# ============================================================================
# EXPORT ALL
# ============================================================================
__all__ = [
    'apply_styles',
    'inject_custom_css',
]
