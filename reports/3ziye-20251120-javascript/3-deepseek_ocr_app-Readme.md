# 🚀 DeepSeek OCR - React + FastAPI

Modern OCR web application powered by DeepSeek-OCR with a stunning React frontend and FastAPI backend. **Now with PDF processing and multi-format document conversion!**

![DeepSeek OCR in Action](assets/multi-bird.png)

## ✨ What's New in v2.2.0 - PDF Processing & Document Conversion

We've added powerful PDF processing capabilities based on community feedback! Here's what you can do now:

### 📄 Process Entire PDF Documents
- Upload PDF files up to 100MB
- Automatic multi-page OCR processing
- Real-time progress tracking for large documents
- Extract text from scanned PDFs or image-based documents

### 🔄 Convert to Multiple Formats
Export your OCR results in the format you need:
- **Markdown (.md)** - Clean, structured text perfect for documentation
- **HTML (.html)** - Styled documents with embedded images and tables
- **Word (.docx)** - Professional documents with formatting, tables, and images
- **JSON** - Structured data for programmatic access

### 🖼️ Automatic Image Extraction
- Detects and extracts images from PDF pages
- Embeds images in exported documents
- Preserves image placement and context

### 📐 Formula & Formatting Preservation
- Maintains mathematical formulas (LaTeX syntax)
- Preserves tables, headings, and document structure
- Cleans up special characters while keeping formatting intact

### 🎯 Use Cases
- **Document Digitization** - Convert scanned PDFs to editable formats
- **Data Extraction** - Pull structured data from forms and invoices
- **Content Migration** - Convert PDFs to Markdown for wikis/documentation
- **Academic Papers** - Extract text and formulas from research papers
- **Business Documents** - Convert reports to Word for editing

---

> **Latest Updates (v2.2.0)** - November 2025
> - 🎉 **NEW: PDF Processing** - Upload PDFs and extract text from all pages
> - 🎉 **NEW: Multi-Format Export** - Convert to Markdown, HTML, DOCX, or JSON
> - 🎉 **NEW: Automatic Image Extraction** - Extract and preserve images from PDFs
> - 🎉 **NEW: Progress Tracking** - Real-time progress for multi-page documents
> - ✅ Dual mode: Image OCR + PDF Processing with format conversion
> - ✅ Enhanced document processing with formula and formatting preservation
>
> **Previous Updates (v2.1.1)**
> - ✅ Fixed image removal button - now properly clears and allows re-upload
> - ✅ Fixed multiple bounding boxes parsing - handles `[[x1,y1,x2,y2], [x1,y1,x2,y2]]` format
> - ✅ Simplified to 4 core working modes for better stability
> - ✅ Fixed bounding box coordinate scaling (normalized 0-999 → actual pixels)
> - ✅ Fixed HTML rendering (model outputs HTML, not Markdown)
> - ✅ Increased file upload limit to 100MB (configurable)
> - ✅ Added .env configuration support

## Quick Start

1. **Clone and configure:**
   ```bash
   git clone <repository-url>
   cd deepseek_ocr_app
   
   # Copy and customize environment variables
   cp .env.example .env
   # Edit .env to configure ports, upload limits, etc.
   ```

2. **Start the application:**
   ```bash
   docker compose up --build
   ```

   The first run will download the model (~5-10GB), which may take some time.

3. **Access the application:**
   - **Frontend**: http://localhost:3000 (or your configured FRONTEND_PORT)
   - **Backend API**: http://localhost:8000 (or your configured API_PORT)
   - **API Docs**: http://localhost:8000/docs

## 🎓 How to Use

### Processing Images (Single Image OCR)

1. Select **"Image OCR"** mode in the toggle
2. Upload an image (PNG, JPG, WEBP, etc.)
3. Choose your OCR mode:
   - **Plain OCR** - Extract all text
   - **Describe** - Get image description
   - **Find** - Locate specific terms
   - **Freeform** - Use custom prompts
4. Click **"Analyze Image"**
5. View results with bounding boxes (if enabled)
6. Copy or download the extracted text

### Processing PDFs (Multi-Page Documents) - NEW!

1. Select **"PDF Processing"** mode in the toggle
2. Upload a PDF file (up to 100MB)
3. Choose your OCR mode (same as above)
4. Select **output format**:
   - 📝 **Markdown** - For documentation, wikis, GitHub
   - 🌐 **HTML** - For web publishing, styled viewing
   - 📄 **DOCX** - For Word editing, professional documents
   - 📊 **JSON** - For programmatic access, data extraction
5. Click **"Process PDF"**
6. Watch the progress bar as pages are processed
7. Your file downloads automatically when complete!

### Tips for Best Results

- **For scanned documents**: Use higher DPI (144-300) in advanced settings
- **For tables**: The model excels at extracting structured data
- **For formulas**: Mathematical notation is preserved in output
- **For images in PDFs**: Enable "Extract Images" to include them in output
- **For large PDFs**: JSON format is fastest, DOCX takes longer due to formatting

### Output Format Comparison

| Format | Best For | Features | File Size |
|--------|----------|----------|-----------|
| **Markdown** | Documentation, GitHub, wikis | Clean text, tables, code blocks | Smallest |
| **HTML** | Web