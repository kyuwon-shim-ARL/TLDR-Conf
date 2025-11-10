"""
Conference-Advisor v3.0 - Research Landscape Analysis
Modules for analyzing speakers using OpenAlex and citation networks.
"""

from .openalex_client import OpenAlexClient, fetch_speaker_metrics
from .speaker_analyzer import SpeakerAnalyzer, quick_speaker_analysis

__version__ = "3.0.0-mvp"
__all__ = [
    "OpenAlexClient",
    "fetch_speaker_metrics",
    "SpeakerAnalyzer",
    "quick_speaker_analysis"
]
