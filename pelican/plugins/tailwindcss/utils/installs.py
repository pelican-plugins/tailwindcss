from .commands import run_in_plugin
from .utils import LOG_PREFIX


def another_tailwind(settings, installed_tailwind_version):
    desired_version = settings.get("version", None)

    if installed_tailwind_version != desired_version:
        mismatch_message = "Different Tailwind version specified in settings"
        print(f"{LOG_PREFIX} {mismatch_message}: v{desired_version}")

        print(f"{LOG_PREFIX} Uninstall current Tailwind version")
        run_in_plugin("npm uninstall tailwindcss")

        print(f"{LOG_PREFIX} Install different Tailwind version")
        run_in_plugin(f"npm i tailwindcss@{desired_version}")


def tailwind(settings):
    desired_version = settings.get("version", None)

    if desired_version:
        run_in_plugin(f"npm i tailwindcss@{desired_version}")


def plugins(settings):
    plugins = settings.get("plugins", None)

    if plugins and len(plugins):
        run_in_plugin(f"npm i {' '.join(plugins)}")
