import os
import subprocess

from pelican import signals

from .utils import utils

BASE_DIR = os.path.dirname(__file__)


def initialize(po):
    node_modules_path = os.path.join(BASE_DIR, "node_modules/")
    if os.path.isdir(node_modules_path):
        j_version = subprocess.check_output(
            "npm -j ls tailwindcss",
            cwd=BASE_DIR,
            shell=True,
        ).decode("utf-8")

        installed_tailwind_version = utils.get_npm_package_version(j_version=j_version)

        print(
            f"{utils.LOG_PREFIX} The version is right (v{installed_tailwind_version})"
        )

        settings = po.settings.get("TAILWIND", None)
        if settings:
            print(f"{utils.LOG_PREFIX} Settings were found")
            desired_version = settings.get("version", None)
            if installed_tailwind_version != desired_version:
                mismatch_message = "Different Tailwind version specified in settings"
                print(f"{utils.LOG_PREFIX} {mismatch_message}: v{desired_version}")
                print(f"{utils.LOG_PREFIX} Uninstall current Tailwind version")
                subprocess.run(
                    f"npm uninstall -C {BASE_DIR} tailwindcss",
                    shell=True,
                )
                print(f"{utils.LOG_PREFIX} Install different Tailwind version")
                subprocess.run(
                    f"npm i -C {BASE_DIR} tailwindcss@{desired_version}",
                    shell=True,
                )
        else:
            print(f"{utils.LOG_PREFIX} No settings were found")
    else:
        print("{utils.LOG_PREFIX} Initialization required, first start")
        settings = po.settings.get("TAILWIND", None)
        if settings:
            print(f"{utils.LOG_PREFIX} Settings were found")
            desired_version = settings.get("version", None)
            subprocess.run(
                f"npm i -C {BASE_DIR} tailwindcss@{desired_version}",
                shell=True,
            )
        subprocess.run(
            f"npm install -C {BASE_DIR}",
            shell=True,
        )


def generate_css(po):
    output_path = po.output_path
    input_file_path = os.path.join(f"{output_path}", "../input.css")
    output_file_path = os.path.join(f"{output_path}", "output.css")
    twconfig_file_path = os.path.join(output_path, "../tailwind.config.js")

    input_output = f"-i {input_file_path} -o {output_file_path}"
    print(f"{utils.LOG_PREFIX} Build css ({output_file_path})")
    subprocess.run(
        f"npx tailwindcss -c {twconfig_file_path} {input_output}",
        shell=True,
    )


def register():
    signals.initialized.connect(initialize)
    signals.finalized.connect(generate_css)
