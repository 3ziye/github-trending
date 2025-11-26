# 📝 MH-TextEditor

A powerful, lightweight text editor for Android with syntax highlighting, smooth editing experience, and professional code editing features.

> ⚠️ **Note:** This editor may not fully support some Android keyboards yet.  
> Compatibility improvements are under active development as part of ongoing research.

---

## 📱 Screenshots

| ![Screenshot 1](https://raw.githubusercontent.com/developer-krushna/MH-TextEditor/refs/heads/main/java.jpg) | ![Screenshot 2](https://raw.githubusercontent.com/developer-krushna/MH-TextEditor/refs/heads/main/smali.jpg) |
|------------------------------------------|------------------------------------------|
| ![Screenshot 3](https://raw.githubusercontent.com/developer-krushna/MH-TextEditor/refs/heads/main/xml.jpg) | ![Screenshot 4](https://raw.githubusercontent.com/developer-krushna/MH-TextEditor/refs/heads/main/syntax_select.jpg) |
|------------------------------------------|------------------------------------------|
| ![Screenshot 5](https://raw.githubusercontent.com/developer-krushna/MH-TextEditor/refs/heads/main/menu.jpg) | ![Screenshot 6](https://raw.githubusercontent.com/developer-krushna/MH-TextEditor/refs/heads/main/menu2.jpg) |
---

## ✨ Features

### 🧩 Core Editing

- **Smooth Text Editing** — Fast and responsive typing experience  
- **Syntax Highlighting** — Support for multiple programming languages (Java, XML, JSON, etc.)  
- **Line Numbers** — Clean, right-aligned line numbers with proper margins  
- **Customizable Text Size** — Pinch-to-zoom and manual text size adjustment  
- **Multiple Font Support** — Custom typeface support for better readability  

### ✂️ Advanced Text Manipulation

- **Smart Selection** — Word selection, line selection, and text range selection  
- **Copy / Cut / Paste** — Full clipboard support with system integration  
- **Find & Replace** — Regex-powered search and replace functionality  
- **Undo / Redo** — Unlimited undo/redo operations with gap buffer implementation  
- **Auto-Indent** — Smart indentation preservation on new lines  

### ⚙️ Professional Tools

- **Magnifier** — Built-in magnifier for precise cursor positioning  
- **Selection Handles** — Visual drag handles for text selection  
- **Floating Clipboard Panel** — Context-aware clipboard actions  
- **Keyboard Support** — Full hardware keyboard support with meta keys  
- **Input Method Support** — Optimized for various soft keyboards  

### 🚀 Performance & UX

- **Gap Buffer Implementation** — Efficient text storage for large files  
- **Smooth Scrolling** — Physics-based scrolling with fling gestures  
- **Cursor Blink** — Visual cursor indication with customizable blink rate  
- **Touch Gestures** — Double-tap, long-press, and scroll gestures  
- **Auto-complete** — Intelligent word completion and suggestions  

---

## 🚀 Getting Started

### Basic Usage

```xml
<!-- In your layout XML -->
<modder.hub.editor.EditView
    android:id="@+id/editView"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
	android:layout_marginTop="0dp"
    android:layout_marginStart="0dp"
    android:paddingTop="0dp"
    android:paddingStart="0dp" 
    android:focusable="true"
    android:focusableInTouchMode="true"/>
```

```java
// In your Activity
EditView editView = findViewById(R.id.editView);
editView.setText("Your code here");
editView.setSyntaxLanguageFileName("java.json");
```

### Advanced Configuration

```java
// Set text size
editView.setTextSize(16); // in pixels

// Enable features
editView.setMagnifierEnabled(true);
editView.setAutoIndentEnabled(true);

// Set typeface
Typeface typeface = Typeface.MONOSPACE;
editView.setTypeface(typeface);

// Set listeners
editView.setOnTextChangedListener(new OnTextChangedListener() {
    @Override
    public void onTextChanged() {
        // Handle text changes
    }
});
```

---

## 🛠️ API Reference

### Core Methods

| Method | Description |
|--------|--------------|
| `setText(String text)` | Set editor content |
| `getText()` | Get current text |
| `setTextSize(float size)` | Set text size in pixels |
| `setTypeface(Typeface typeface)` | Set custom typeface |
| `setSyntaxHighlightingEnabled(boolean enabled)` | Toggle syntax highlighting |

### Editing Operations

| Method | Description |
|--------|--------------|
| `undo()` | Undo last operation |
| `redo()` | Redo last operation |
| `copy()` | Copy selected text |
| `cut()` | Cut selected text |
| `paste()` | Paste from clipboard |
| `selectAll()` | Select all text |
| `clearSelection()` | Clear current selection |

### Navigation & Search

| Method | Description |
|--------|--------------|
| `gotoLine(int line)` | Navigate to specific line |
| `find(String regex)` | Find text using regex |
| `replaceFirst(String replacement)` | Replace first match |
| `replaceAll(String replacement)` | Replace all matches |

### Configuration

| Method | Description |
|--------|--------------|
| `setEditedMode(boolean editMode)` | Enable/disable editing 