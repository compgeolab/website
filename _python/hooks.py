"""
Pre-processing of the page metadata before rendering.
"""
from datetime import datetime
import subprocess


def process_info(info, site):
    """
    Alter the page metadata before rendering.
    """
    # Urubu doesn't split the 'tags' into multiple strings
    if "tags" in info:
        if isinstance(info["tags"], str):
            info["tags"] = info["tags"].split(", ")
    # Identify to which folder the item belongs (paper, blog, etc)
    if "type" not in info:
        info["type"] = "/{}".format(info["id"].split("/")[1])
    # Add the current date to the site metadata
    if "now" not in site:
        site["now"] = datetime.utcnow()
    # Add the last git commit hash to the site metadata
    if "commit" not in site:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True
        )
        site["commit"] = completed.stdout.strip()
