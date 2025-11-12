"""
Conference-Advisor v3.1 - Research Landscape Analysis
Modules for analyzing speakers and sessions using OpenAlex and citation networks.
"""

from .openalex_client import OpenAlexClient, fetch_speaker_metrics
from .speaker_analyzer import SpeakerAnalyzer, quick_speaker_analysis
from .session_landscape_builder import SessionLandscapeBuilder, build_session_landscape

__version__ = "3.1.0"
__all__ = [
    "OpenAlexClient",
    "fetch_speaker_metrics",
    "SpeakerAnalyzer",
    "quick_speaker_analysis",
    "SessionLandscapeBuilder",
    "build_session_landscape"
]
