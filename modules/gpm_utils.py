# modules/gpm_utils.py

GPM_MAPPINGS = {
    "belts": {"min GPM": 20, "max GPM": 30, "avg GPM": 25},
    "Filter": {"min GPM": 20, "max GPM": 30, "avg GPM": 25},
    "Engine Parts": {"min GPM": 40, "max GPM": 45, "avg GPM": 43},
    "Engine": {"min GPM": 25, "max GPM": 30, "avg GPM": 28},
    "main components": {"min GPM": 30, "max GPM": 60, "avg GPM": 45},
    "tires&rims": {"min GPM": 30, "max GPM": 30, "avg GPM": 30},
    "brushes&sweepers": {"min GPM": 30, "max GPM": 30, "avg GPM": 30},
    "cutting edges&GET": {"min GPM": 30, "max GPM": 30, "avg GPM": 30},
    "U/C": {"min GPM": 30, "max GPM": 30, "avg GPM": 30},
    "local parts": {"min GPM": 25, "max GPM": 30, "avg GPM": 28},
}

def get_gpm(category, mode='avg GPM'):
    if category in GPM_MAPPINGS:
        return GPM_MAPPINGS[category].get(mode, 0)
    return 0

