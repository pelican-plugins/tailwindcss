# TailwindCSS Plugin for Pelican 🌬

[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/tailwindcss/build)](https://github.com/pelican-plugins/tailwindcss/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-tailwindcss)](https://pypi.org/project/pelican-tailwindcss/)
![License](https://img.shields.io/pypi/l/pelican-tailwindcss?color=blue)

This plugin helps you use [TailwindCSS][] in your Pelican website.

|    Author     |                       GitHub                       |                        Twitter                         |
| :-----------: | :------------------------------------------------: | :----------------------------------------------------: |
| Luca Fedrizzi | [https://github.com/lcfd](https://github.com/lcfd) | [https://twitter.com/lc_fd](https://twitter.com/lc_fd) |

## Why Use This Plugin?

Because you want use [TailwindCSS][] in seconds.
Not hours.

## Requirements

In order to run this plugin, you need to install NodeJS. (I'm looking to replace this dependency by using a Python package. – Luca)

## Installation

This plugin can be installed via:

`python -m pip install pelican-tailwindcss`

or

`poetry add pelican-tailwindcss`

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

4. Done! You should be ready to use [TailwindCSS][] in your website template.

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

### Tailwind plugins install

As you can see from the example above it is possible to add the `plugins` property to the configuration.
Just add the name of a Tailwind plugin in this property and the plugin will be installed.

## Useful informations

### Plugins

Your `tailwind.config.js` file will only be copied when Pelican starts. This means that any changes after starting Pelican will not be considered. For example if you want to install a new plugin for Tailwind you will have to restart Pelican.

## Contributing

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/tailwindcss/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

## License

This project is licensed under the AGPL-3.0 license.

[TailwindCSS]: https://github.com/tailwindlabs/tailwindcss
