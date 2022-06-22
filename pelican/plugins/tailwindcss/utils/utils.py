import json

RED = "\033[0;32m"
NC = "\033[0m"

LOG_PREFIX = f"{RED}tailwindcss 🌬{NC} "


def get_npm_package_version(j_version: str):
    dict_version = json.loads(j_version)
    version = (
        dict_version.get("dependencies", {}).get("tailwindcss", {}).get("version", "")
    )
    if version:
        return version
    return ""
