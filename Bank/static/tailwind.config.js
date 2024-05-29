/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["Bank/templates/*.html", "Bank/static/*.js"],
  theme: {
    extend: {},
  },
  plugins: [],
}

//npx tailwindcss -w -i Bank/static/index.css -o Bank/static/style.css -c Bank/static/tailwind.config.js