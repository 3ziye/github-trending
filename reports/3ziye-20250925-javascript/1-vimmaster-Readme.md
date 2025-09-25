# VIM Master

VIM Master -- in-browser game that teaches core Vim motions and editing commands through short, focused levels. 

## Try the Online Demo
[![Demo Online](https://img.shields.io/badge/demo-online-brightgreen?logo=github&style=for-the-badge)](https://renzorlive.github.io/vimmaster/)

> 💡 **Tip:** For the best experience, use a desktop/laptop (full keyboard support).

## Screenshot
![VIM Master Screenshot](images/vm.gif)

## Features
- **Normal/Insert modes** with an on-screen status bar
- **Command log** showing your keystrokes
- **16 Progressive Levels** that validate your action outcomes (not just keystrokes)
- **Complete Vim Support**: `h j k l`, `w b e`, `gg G`, `0 $`, `x`, `dd`, `dw`, `yy`, `p`, `i`, `a`, `o/O`, `cw`, `D`, `r`, ex-commands `:q`, `:wq`
- **Numeric counts** for motions/operators (e.g., `3w`, `2dd`, `5x`, `5G`)
- **Undo/redo support** (`u`, `Ctrl+r`)
- **Vim-style search**: `/` and `?`, with `n`/`N` navigation and match highlighting
- **Challenge Mode**: Fast-paced timed challenges to test your Vim skills
- **Cheat Mode**: Interactive command reference with instant practice sessions
- **Progress Management**: Auto-save, export/import codes, and progress tracking
- **Badge System**: Earn visual badges as you learn (Beginner, Search Master)
- **Profile Page**: Beautiful showcase of achievements with social media sharing
- **Canvas-Based Achievement Cards**: Generate downloadable and shareable images
- **Modular Architecture**: Clean, maintainable codebase for easy development

## Recent UI/UX Improvements
- **Streamlined Layout**: ASCII logo at top, title under text editor, buttons above instructions
- **Compact Achievements**: Achievements container positioned before instructions for better flow
- **Collapsible Progress Management**: Click to expand/collapse progress information, reducing UI clutter
- **Responsive Design**: Optimized layout for better focus on gameplay elements
- **Auto-Focus Editor**: Editor automatically focuses when lessons start for seamless UX
- **Challenge Points Integration**: Challenge points now properly tracked and displayed in progress summary
- **Enhanced Cheat Mode**: All cheat mode lessons now work with proper auto-focus and completion tracking

## Latest Bug Fixes & Improvements
- **Fixed "undefined challenge points"**: Challenge points now properly display in progress summary
- **Enhanced Cheat Mode**: All practice lessons now auto-focus and validate completion correctly
- **Improved Challenge Mode**: Better validation and scoring system for challenge tasks
- **Auto-Focus UX**: Editor automatically focuses when starting lessons for better user experience
- **Progress System**: Robust error handling and fallback values for all progress data

## Progress Management System
VIM Master features a comprehensive client-side progress tracking system that works entirely in your browser:

### **Features**
- **Auto-save**: Progress automatically saved every 5 seconds and after earning badges
- **Export/Import Codes**: Generate compact Base64-encoded progress codes for backup and sharing
- **Local Storage**: Progress persists between browser sessions
- **Progress Summary**: Real-time display of current level, badges earned, and commands practiced
- **Clear Progress**: Reset all progress with a single click

### **How It Works**
1. **Export Progress**: Click "Export Progress" to generate a shareable code
2. **Import Progress**: Paste a code and click "Import Progress" to restore your game state
3. **Progress Codes**: Compact, shareable strings containing all your achievements and progress
4. **Privacy First**: All data stays on your device - no accounts or backend required

### **Progress Data Tracked**
- Current level and challenge mode status
- Earned badges (Beginner, Search Master, etc.)
- Commands practiced during gameplay
- Challenge points earned from challenge mode
- Timestamp of last save

## Profile Page & Social Sharing
Showcase your VIM mastery journey with a beautiful profile page and share achievements on social media.

### **Profile Page Features**
- **Beautiful Achievement Cards**: Eye-catching cards for each earned badge
- **Progress Overview**: Visual representation of your learning journey with circular progress indicators
- **ASCII Logo Integration**: The iconic VIM Master logo prominently displayed
- **Social Media Integration**: Share achievements on Twitter, Facebook, and other platforms
- **Progress Code Management**: Copy and share your progress codes easily
- **GitHub Integration**: Links to view source code and contribute to the project

### **Canvas-Based Achievement Cards**
- **Dynamic Image Generation**: Create custom achievement cards using HTML5 Canvas
- **Downloadable Images**: Save achievement cards as PNG files for sharing
- **Social Media Ready**: Optimized dimensions and styling for social platforms
- **Custom Branding**: Features the VIM Master ASCII logo and your progress data
- **Professional Design**: Beautiful blue/pu