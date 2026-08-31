from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.generate_assets import load_profile, profile_card


def test_load_profile_reads_yaml_values():
    profile = load_profile()
    assert profile["identity"]["name"] == "Subrata Bag"
    assert profile["identity"]["headline"] == "Creative Developer"
    assert profile["identity"]["education"] == "B.Tech Computer Science & Engineering"


def test_profile_card_uses_name_and_headline_from_config():
    rendered = profile_card(False)
    assert "SUBRATA BAG" in rendered
    assert "CREATIVE DEVELOPER" in rendered
