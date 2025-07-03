# DoniArt Portfolio - Developer Documentation

A modern, responsive art portfolio website showcasing the work of Donia Liu Neekman, featuring character design, visual development, and illustration.

## Features

- **Modern Design**: Clean, minimalist interface that lets the artwork shine
- **Responsive Layout**: Works beautifully on all devices
- **Portfolio Categories**: Filter works by Character Design, Visual Development, and Storyboards
- **Lightbox Gallery**: Click any artwork for full-screen viewing
- **Smooth Animations**: Professional transitions and effects
- **Dark Mode Support**: Automatically adapts to system preferences

## Quick Start

1. Run the local server:
   ```bash
   python3 serve.py
   ```

2. Open your browser to `http://localhost:8000`

## Project Structure

```
DoniArt/
├── index.html          # Main portfolio page
├── serve.py           # Local development server
├── images/           # All image assets
│   ├── artwork/      # Portfolio pieces
│   │   ├── character-design/
│   │   ├── visdev/
│   │   ├── storyboards/
│   │   └── about/
│   ├── favicon/      # Favicon files
│   └── logo.png      # Site logo
└── cv/
    └── DoniArt-CV.pdf  # Resume file
```

## Technologies Used

- **Tailwind CSS**: Utility-first CSS framework
- **Alpine.js**: Lightweight JavaScript framework
- **Modern CSS**: Custom animations and effects
- **Responsive Design**: Mobile-first approach

## Portfolio Sections

1. **Character Design**: Fantasy characters with unique personalities
2. **Visual Development**: Environment art and atmospheric studies
3. **Storyboards**: Professional narrative sequences
4. **About**: Artist information and background

## Dynamic Image Loading

The portfolio is set up for easy dynamic image loading. Currently using static data, but can be easily modified to fetch from a server endpoint by updating the `loadArtworks()` function in `index.html`.

---

Built with passion for showcasing incredible artistic talent.