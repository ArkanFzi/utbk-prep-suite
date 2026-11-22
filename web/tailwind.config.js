/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        canvas: '#0B0D11',
        surface: '#12161E',
        surfaceHighlight: '#1A202C',
        borderSubtle: '#252B38',
        accentPk: '#EF4444',
        accentPu: '#10B981',
        accentPm: '#3B82F6',
        accentLit: '#F59E0B',
        accentReview: '#8B5CF6'
      }
    },
  },
  plugins: [],
}
