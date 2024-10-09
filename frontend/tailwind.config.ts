import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    // Add any other directories where Tailwind classes are used
  ],
  theme: {
    extend: {
      colors: {
        background: 'var(--background)', // Ensure these variables are defined in your CSS
        foreground: 'var(--foreground)',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Example of setting a default font family
      },
    },
  },
  plugins: [
    // Add any Tailwind CSS plugins here
  ],
};

export default config;
