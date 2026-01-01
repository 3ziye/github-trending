# Prompt Fill (提示词填空器)

[English](#english) | [中文](#chinese)

---

<a id="english"></a>

# Prompt Fill

A **structured prompt generation tool** designed specifically for AI painting (GPT, Midjourney, Nano Banana, etc.). Help users quickly build, manage, and iterate complex prompts through a visual "fill-in-the-blank" interaction.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/Version-0.6.5-orange.svg)
![Data](https://img.shields.io/badge/Data-0.7.6-green.svg)
![React](https://img.shields.io/badge/React-18.x-61DAFB.svg)
![Vite](https://img.shields.io/badge/Vite-5.x-646CFF.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38B2AC.svg)

<img width="1343" height="612" alt="image@1x-2" src="https://github.com/user-attachments/assets/7c3d969b-7f63-46fc-a16a-e3074da6c692" />
<img width="1343" height="620" alt="1231333" src="https://github.com/user-attachments/assets/08c90a9f-7b1e-4b3d-84fc-650bccfd1d2b" />

## 📝 Foreword

Prompt Fill is now at version **v0.6.5**. The original intention of this project is to solve the problem of hard-to-remember, hard-to-manage, and tedious modification of prompts in the AI painting process. By structuring prompts, creation becomes as simple as "filling in the blanks".

### 🌟 Progress & Core Features

*   **✅ Full Dark Mode Support**: One-click theme switching for desktop and mobile.
*   **✅ Linkage Groups**: Sync modifications globally within groups (e.g., `{{color}}_1`).
*   **✅ Structured Prompt Engine**: Automatic interactive form conversion via `{{variable}}`.
*   **✅ Dynamic Bank System**: Preset art tags with category management and batch import.
*   **✅ HD Social Sharing**: Export beautiful JPG long images with auto-extracted colors.
*   **✅ Cloud Awareness**: Real-time sync for official templates and features.
*   **✅ Local Storage**: Private data stored in browser LocalStorage.

---

## ✨ Core Features

### 🧩 Intelligent Bank Management
*   **Category Management**: Color-coded categories (e.g., characters, actions) for visual clarity.
*   **Bidirectional Sync**: Directly add custom options in preview to sync back to the bank.
*   **Category Editor**: Manage categories and 12 preset colors.
*   **Responsive Layout**: Efficient masonry multi-column layout.

### 📝 Multi-Template System
*   **Independent Templates**: Create separate prompt templates for different use cases.
*   **Isolated State**: Variable selections are independent per template.
*   **Clone/Copy**: One-click duplication for A/B testing.

### 🖱️ Visual Interaction
*   **WYSIWYG Editing**: Highlighting variables by category color during editing.
*   **Linkage Groups**: Sync same variables in designated groups.
*   **Drag & Drop**: Insert variables by dragging bank cards.
*   **Preview Mode**: Templates render variables as clickable dropdowns.
*   **Multi-Instance**: Multiple occurrences of the same variable work independently.

### 💾 Auto Persistence
*   Changes are automatically saved to LocalStorage.
*   No data loss on refresh or browser close.

### 🖼️ Image Management
*   **Preview Images**: Templates support associated preview images.
*   **Custom Upload**: Replace default previews with your own images.
*   **Image Actions**: Hover for large view, upload, or reset.
*   **Ambient Background**: Blurry background effect at the top.

### 📋 Export & Share
*   **One-click Copy**: Copy clean generated prompt text.
*   **Save Long Image**: Export HD JPGs for archiving and sharing.

---

## 🛠️ Tech Stack

*   **Build Tool**: [Vite](https://vitejs.dev/)
*   **Frontend**: [React](https://react.dev/)
*   **Styling**: [Tailwind CSS](https://tailwindcss.com/)
*   **Icons**: [Lucide React](https://lucide.dev/)
*   **Export**: [html2canvas](https://html2canvas.hertzen.com/)

---

## 🚀 Quick Start

### Prerequisites
Node.js v18+ is recommended.

### Installation & Run

1.  **Clone**
    ```bash
    git clone https://github.com/TanShilongMario/PromptFill.git
    cd PromptFill
    ```
2.  **Install**
    ```bash
    npm install
    ```
3.  **Dev**
    ```bash
    npm run dev
    ```
4.  **Build**
    ```bash
    npm run build
    ```

### Shortcut Scripts
*   **macOS**: `start.command`
*   **Windows**: `start.bat`

---

## 📖 Usage Guide

### 1. Manage Categories
Manage categories and colors at the top of the left panel. Each category has a unique color for quick identification.

### 2. Create Banks
Create "Variable Groups" and add options (single or batch). Cards can be dragged into the editor.

### 3. Edit Templates
Use "Edit Template" to enter visual mode. Supports drag-and-drop insertion, manual `{{variable}}` input, and Undo/Redo.

### 4. Preview & Generate
Switch to "Preview Interaction". Select options from dropdowns. Use "+ Add Custom Option" to save new values directly.

### 5. Manage Images
Hover over preview images to view large versions, upload custom images, or reset to default.

### 6. Export & Share
Copy the final prompt or save as a long imag