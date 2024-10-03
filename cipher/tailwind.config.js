/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "color-1": "hsl(var(--color-1))",
        "color-2": "hsl(var(--color-2))",
        "color-3": "hsl(var(--color-3))",
        "color-4": "hsl(var(--color-4))",
        "color-5": "hsl(var(--color-5))",
      },
      animation: {
        rainbow: "rainbow var(--speed, 2s) infinite linear",
        shine: "shine var(--duration) infinite linear",
        rainbow: "rainbow var(--speed, 2s) infinite linear",
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
        "border-beam": "border-beam calc(var(--duration)*1s) infinite linear",
        shine: "shine var(--duration) infinite linear",
        move: "move 5s linear infinite",
      },
      keyframes: {
        shine: {
          "0%": {
            "background-position": "0% 0%",
          },
          "50%": {
            "background-position": "100% 100%",
          },
          to: {
            "background-position": "0% 0%",
          },
        },
        rainbow: {
          "0%": { "background-position": "0%" },
          "100%": { "background-position": "200%" },
        },
          rainbow: {
            '0%': { 'background-position': '0%' },
            '100%': { 'background-position': '200%' },
          },
          'accordion-down': {
            from: { height: '0' },
            to: { height: 'var(--radix-accordion-content-height)' },
          },
          'accordion-up': {
            from: { height: 'var(--radix-accordion-content-height)' },
            to: { height: '0' },
          },
          'border-beam': {
            '100%': { 'offset-distance': '100%' },
          },
          shine: {
            '0%': { 'background-position': '0% 0%' },
            '50%': { 'background-position': '100% 100%' },
            to: { 'background-position': '0% 0%' },
          },
          move: {
            '0%': { transform: 'translateX(-200px)' },
            '100%': { transform: 'translateX(200px)' },
        },
      },
    },
  },
};
