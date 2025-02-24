import importlib.resources
import os
from pathlib import Path
import subprocess
import sysconfig

from rich import print

from pelican import signals

from .utils.utils import (
    LOG_PREFIX,
    build_tailwind_css,
    get_env_var_prefix,
    get_tailwind_css_version,
)

PLUGIN_BASE_DIR = importlib.resources.files(__package__)
SITE_PACKAGES_DIR = Path(sysconfig.get_path("purelib"))


def initialize(po):
    # Print notice if TAILWIND settings are found.
    tailwind_settings = po.settings.get("TAILWIND")
    if tailwind_settings:
        print(f"{LOG_PREFIX} Settings were found")

    # Get Tailwind CSS version if specified in settings.
    prefix = ""
    tailwind_version = get_tailwind_css_version(po.settings)
    if tailwind_version != "latest":
        tailwind_version = f"v{tailwind_version}"
        prefix = f"TAILWINDCSS_VERSION={tailwind_version} "

    # Download Tailwind CSS version if not already present.
    tailwind_cli = Path(
        SITE_PACKAGES_DIR / "pytailwindcss" / "bin" / tailwind_version / "tailwindcss"
    )
    if not tailwind_cli.exists():
        print(f"Downloading Tailwind CSS CLI {tailwind_version} to {tailwind_cli}")
        subprocess.run(f"{prefix}tailwindcss_install", shell=True, check=False)


def generate_css(po):
    prefix = suffix = ""
    # Get Tailwind CSS version if specified in settings.
    # If not the latest version, compose prefix for Tailwind CLI & suffix for logging.
    tailwind_version = get_tailwind_css_version(po.settings)
    if tailwind_version != "latest":
        prefix = get_env_var_prefix(tailwind_version)
        suffix = f" via Tailwind CSS v{tailwind_version}"

    project_root = os.path.abspath(os.path.join(po.path, ".."))
    input_file_path = os.path.join(project_root, "input.css")
    output_dir = po.settings.get("OUTPUT_PATH", f"{project_root}/output")
    output_file_path = Path(f"{output_dir}/output.css")
    twconfig_file_path = os.path.join(project_root, "tailwind.config.js")

    print(f"{LOG_PREFIX} Build CSS @ {output_file_path}{suffix}")

    build_tailwind_css(prefix, input_file_path, output_file_path, twconfig_file_path)


def register():
    signals.initialized.connect(initialize)
    signals.finalized.connect(generate_css)
