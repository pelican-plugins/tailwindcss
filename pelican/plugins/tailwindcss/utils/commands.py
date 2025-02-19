from os import path
import subprocess

PLUGIN_BASE_DIR = path.abspath(path.join(__file__, "../../"))


def run_in_plugin(command: str):
    subprocess.run(
        args=command,
        cwd=PLUGIN_BASE_DIR,
        shell=True,
        check=False,
    )
