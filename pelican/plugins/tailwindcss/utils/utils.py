import pathlib
import subprocess

LOG_PREFIX = "[green]tailwindcss 🌬[/green] "


def get_tailwind_css_version(settings: dict):
    tailwind_settings = settings.get("TAILWIND")
    if tailwind_settings and tailwind_settings.get("version"):
        version = tailwind_settings.get("version")
    else:
        version = "latest"

    return version


def get_env_var_prefix(version: str):
    if version != "latest":
        env_var_prefix = f"TAILWINDCSS_VERSION=v{version} "

    return env_var_prefix


def build_tailwind_css(prefix, input_file_path, output_file_path, twconfig_file_path):
    tailwind_root = pathlib.Path(twconfig_file_path).parent
    input_output = f"-i {input_file_path} -o {output_file_path}"
    subprocess.run(
        f"{prefix}tailwindcss -c {twconfig_file_path} {input_output}",
        cwd=tailwind_root,
        shell=True,
        check=True,
    )
