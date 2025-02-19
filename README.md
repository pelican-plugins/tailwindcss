# Tailwind CSS Plugin for Pelican 🌬

[![Build Status](https://img.shields.io/github/actions/workflow/status/pelican-plugins/tailwindcss/main.yml?branch=main)](https://github.com/pelican-plugins/tailwindcss/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-tailwindcss)](https://pypi.org/project/pelican-tailwindcss/)
[![Downloads](https://img.shields.io/pypi/dm/pelican-tailwindcss)](https://pypi.org/project/pelican-tailwindcss/)
![License](https://img.shields.io/pypi/l/pelican-tailwindcss?color=blue)

This plugin helps you use [Tailwind CSS][] in your Pelican web site.

## Why Use This Plugin?

Because you want use [Tailwind CSS][] in seconds. Not hours.

## Requirements

In order to run this plugin, you need to install Node.JS. (Someday this dependency could be replaced with a Python package.)

## Installation

This plugin can be installed via:

    python -m pip install pelican-tailwindcss

As long as you have not explicitly added a `PLUGINS` setting to your Pelican settings file, then the newly-installed plugin should be automatically detected and enabled. Otherwise, you must add `tailwindcss` to your existing `PLUGINS` list. For more information, please see the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.

## Basic Usage

1. Create a `tailwind.config.js` file in your Pelican project root folder containing:

    ```js
    /** @type {import('tailwindcss').Config} */
    module.exports = {
    content: ["./themes/**/*.html", "./themes/**/*.js"],
    theme: {
        extend: {},
    },
    plugins: [],
    };
    ```

    The `content` property values are just suggestions. Feel free to modify them according to your needs.

2. Create a `input.css` file in your Pelican project root folder containing:

    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

3. Add the build file (`output.css`) in your `base.html`.

    ```html
    <link rel="stylesheet" href="/output.css" />
    ```

4. Done! You should be ready to use [Tailwind CSS][] in your website template.

## Advanced Usage

In your settings you can configure the plugin's behavior using the `TAILWIND` setting.

An example of a complete `TAILWIND` setting:

```python
TAILWIND = {
    "version": "3.0.0",
    "plugins": [
        "@tailwindcss/typography",
        "@tailwindcss/forms",
        "@tailwindcss/line-clamp",
        "@tailwindcss/aspect-ratio",
    ],
}
```

### Tailwind Plugin Installation

As you can see from the example above, it is possible to add the `plugins` property to the configuration.
Just add the name of a Tailwind plugin to the list, and the plugin will be installed.

## Useful Information

### Plugins

Your `tailwind.config.js` file will only be copied when Pelican starts. This means that any changes made after starting Pelican will not be recognized. For example, if you want to install a new plugin for Tailwind, you will have to restart Pelican in order for that plugin to become active.

## Contributing

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/tailwindcss/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

## License

This project is licensed under the AGPL-3.0 license.

[Tailwind CSS]: https://github.com/tailwindlabs/tailwindcss
