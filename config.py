"""
The Mountain Path - Streamlit Design Template
Configuration Module: Colors, Branding, Page Settings

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence
"""

# ============================================================================
# COLOR SCHEME
# ============================================================================
COLORS = {
    # Primary Brand Colors
    'dark_blue': '#003366',
    'medium_blue': '#004d80',
    'light_blue': '#ADD8E6',
    'accent_gold': '#FFD700',
    
    # Background Colors
    'bg_dark': '#0a1628',
    'card_bg': '#112240',
    'gradient_start': '#1a2332',
    'gradient_mid': '#243447',
    'gradient_end': '#2a3f5f',
    
    # Text Colors
    'text_primary': '#e6f1ff',
    'text_secondary': '#8892b0',
    'text_dark': '#1a1a2e',
    
    # Status Colors
    'success': '#28a745',
    'warning': '#ffc107',
    'danger': '#dc3545',
    'info': '#17a2b8',
}

# ============================================================================
# BRANDING
# ============================================================================
BRANDING = {
    'name': 'The Mountain Path - World of Finance',
    'instructor': 'Prof. V. Ravichandran',
    'credentials': '28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence',
    'icon': '🏔️',
    
    # Social Links
    'linkedin': 'https://www.linkedin.com/in/trichyravis',
    'github': 'https://github.com/trichyravis',
}

# ============================================================================
# TYPOGRAPHY
# ============================================================================
FONTS = {
    'display': "'Playfair Display', serif",
    'body': "'Source Sans Pro', sans-serif",
    'code': "'Source Sans Pro', monospace",
}

# ============================================================================
# PAGE CONFIGURATION (Default)
# ============================================================================
PAGE_CONFIG = {
    'page_title': 'The Mountain Path - Finance Analytics',
    'page_icon': '🏔️',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
}

# ============================================================================
# SPACING & SIZING
# ============================================================================
SPACING = {
    'section_margin': '1.5rem',
    'card_padding': '1.2rem',
    'header_padding': '1.5rem 2rem',
    'border_radius': '10px',
    'border_radius_small': '8px',
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_page_config(title: str = None, icon: str = None) -> dict:
    """
    Get customized page configuration.
    
    Parameters:
    -----------
    title : str, optional
        Custom page title (default: from PAGE_CONFIG)
    icon : str, optional
        Custom page icon (default: from PAGE_CONFIG)
    
    Returns:
    --------
    dict : Streamlit page configuration
    """
    config = PAGE_CONFIG.copy()
    if title:
        config['page_title'] = f"{title} | Mountain Path"
    if icon:
        config['page_icon'] = icon
    return config


def rgba_from_hex(hex_color: str, alpha: float = 1.0) -> str:
    """
    Convert hex color to rgba string.
    
    Parameters:
    -----------
    hex_color : str
        Hex color code (e.g., '#003366')
    alpha : float
        Alpha transparency (0.0 to 1.0)
    
    Returns:
    --------
    str : RGBA color string
    """
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f'rgba({r}, {g}, {b}, {alpha})'


def get_gradient_background(start: str = None, end: str = None) -> str:
    """
    Get gradient background CSS.
    
    Parameters:
    -----------
    start : str, optional
        Starting gradient color (default: gradient_start)
    end : str, optional  
        Ending gradient color (default: gradient_end)
    
    Returns:
    --------
    str : CSS gradient string
    """
    start = start or COLORS['gradient_start']
    end = end or COLORS['gradient_end']
    mid = COLORS['gradient_mid']
    return f"linear-gradient(135deg, {start} 0%, {mid} 50%, {end} 100%)"


# ============================================================================
# COMPONENT STYLES (CSS Classes)
# ============================================================================
COMPONENT_CLASSES = {
    'header': 'header-container',
    'metric': 'metric-card',
    'info': 'info-box',
    'formula': 'formula-box',
    'section': 'section-title',
}

# ============================================================================
# EXPORT ALL
# ============================================================================
__all__ = [
    'COLORS',
    'BRANDING', 
    'FONTS',
    'PAGE_CONFIG',
    'SPACING',
    'COMPONENT_CLASSES',
    'get_page_config',
    'rgba_from_hex',
    'get_gradient_background',
]
