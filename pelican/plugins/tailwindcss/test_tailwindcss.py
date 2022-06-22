from .utils.utils import get_npm_package_version


def test_get_npm_package_version():
    j_version = """{
  "version": "1.0.0",
  "name": "tailwindcss",
  "dependencies": {
    "tailwindcss": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-3.0.0.tgz"
    }
  }
}"""
    version = get_npm_package_version(j_version=j_version)
    assert version == "3.0.0"
