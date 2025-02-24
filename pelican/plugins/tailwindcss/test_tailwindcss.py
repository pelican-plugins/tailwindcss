import hashlib
import pathlib

from .utils.utils import (
    build_tailwind_css,
    get_env_var_prefix,
    get_tailwind_css_version,
)


def test_get_tailwind_css_version_specified():
    tailwind_settings = {"TAILWIND": {"version": "3.0.24"}}
    version = get_tailwind_css_version(settings=tailwind_settings)
    assert version == "3.0.24"


def test_get_tailwind_css_version_unspecified():
    tailwind_settings = {}
    version = get_tailwind_css_version(settings=tailwind_settings)
    assert version == "latest"


def test_generate_tailwind_css(tmp_path_factory):
    tailwind_settings = {"TAILWIND": {"version": "3.0.24"}}
    tailwind_version = get_tailwind_css_version(settings=tailwind_settings)
    prefix = get_env_var_prefix(tailwind_version)
    output_file_path = tmp_path_factory.mktemp("output") / "output.css"
    datadir = pathlib.Path(__file__).parent / "test_data"
    input_file_path = datadir / "input.css"
    twconfig_file_path = datadir / "tailwind.config.js"

    assert twconfig_file_path.exists()

    build_tailwind_css(prefix, input_file_path, output_file_path, twconfig_file_path)

    # Generate SHA256 hash of generated Tailwind CSS file.
    with open(output_file_path, "rb", buffering=0) as f:
        tw_hash = hashlib.file_digest(f, "sha256").hexdigest()

    assert tw_hash == "05599a21494f832940e7596085192244df93f753297d524a70ce9c4ed21e792f"
