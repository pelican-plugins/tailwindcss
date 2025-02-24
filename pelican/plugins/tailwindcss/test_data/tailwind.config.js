/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: "class",
    content: ["./themes/**/*.html", "./themes/**/*.js"],
    theme: {
        extend: {
            fontFamily: {
                sans: ['-apple-system','BlinkMacSystemFont','"segoe ui"','Roboto','Oxygen','Ubuntu','Cantarell','"open sans"','"helvetica neue"','"sans-serif"'],
          'display': ['Georama',]
            },
            typography: {
                DEFAULT: {
                    css: {
                        'code::before': {
                            content: '""'
                        },
                        'code::after': {
                            content: '""'
                        }
                    }
                }
            },
        },
    },
    plugins: [
        require("@tailwindcss/typography"),
        require("@tailwindcss/aspect-ratio"),
    ],
};
