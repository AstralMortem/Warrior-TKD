/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  safelist: [
    {
      pattern: /ring-(red|green|blue)-(100|200|300|400|500|600|700|800|900)/,
    }
  ]
  ,
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
          'yellow': {
            '50': '#fbf9f1',
            '100': '#f6f1de',
            '200': '#ede1bb',
            '300': '#e1cc90',
            '400': '#d7b56d',
            '500': '#cb9a44',
            '600': '#bd8439',
            '700': '#9d6931',
            '800': '#7e542e',
            '900': '#664628',
            '950': '#372313',
            DEFAULT: '#d7b56d'
        },
          'black': {
          '50': '#f6f6f6',
          '100': '#e7e7e7',
          '200': '#d1d1d1',
          '300': '#b0b0b0',
          '400': '#888888',
          '500': '#6d6d6d',
          '600': '#5d5d5d',
          '700': '#4f4f4f',
          '800': '#454545',
          '900': '#3d3d3d',
          '950': '#0d0d0d',
          DEFAULT: '#0d0d0d',
        },
          'woodsmoke': {
        '50': '#f5f5f6',
        '100': '#e6e6e7',
        '200': '#cfd0d2',
        '300': '#adaeb3',
        '400': '#84858c',
        '500': '#696a71',
        '600': '#5a5b60',
        '700': '#4d4d51',
        '800': '#434347',
        '900': '#3b3b3e',
        '950': '#111112',
        DEFAULT: '#111112',
        },
          'alabaster': {
          '50': '#f8f8f8',
          '100': '#efefef',
          '200': '#dcdcdc',
          '300': '#bdbdbd',
          '400': '#989898',
          '500': '#7c7c7c',
          '600': '#656565',
          '700': '#525252',
          '800': '#464646',
          '900': '#3d3d3d',
          '950': '#292929',
          DEFAULT: '#f8f8f8',
        },
          'silver': {
        '50': '#f7f7f7',
        '100': '#f0f0f0',
        '200': '#e3e3e3',
        '300': '#d1d1d1',
        '400': '#bdbdbd',
        '500': '#aaaaaa',
        '600': '#969696',
        '700': '#818181',
        '800': '#6a6a6a',
        '900': '#585858',
        '950': '#333333',
        DEFAULT:'#bdbdbd',
        },
      },
      fontFamily: {
        'display': ['Roboto', 'sans-serif'],
        'logo': ['Limelight', 'sans-serif'],
        'title': ['Tektur', 'sans-serif']
      },
    },
    
    
  },
  plugins: [
  ],
}