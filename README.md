
# 🕸️ WebSnark — The Snarky Website Summarizer  
*A Gemini-powered tool that reads websites so you don’t have to.*

Welcome to **WebSnark**, the tiny Python project with a big attitude.  
Paste in a URL, and our sarcastic little AI gremlin will fetch the site’s text, ignore the usual internet nonsense (menus, ads, cookie popups, life regrets), and return a **structured, witty Markdown summary**.

Because reading entire websites is so 2010.



## ✨ Features

- 🤖 **AI-powered summarization** using Gemini 2.5 Flash  
- 🎭 **Snarky personality** for summaries that actually entertain  
- 🧹 **Navigation & UI noise filtering** (menus? gone. cookie popups? unalived.)  
- 🧱 **Clean, modular code**  
- 🧩 Easy to integrate into Jupyter, scripts, or full apps  
- 📝 Output delivered as **beautiful, structured Markdown**



## 🚀 Quick Start

### 1. Clone the repo  
```bash
git clone https://github.com/selimbenhajbraiek/WebSnark-The-Snarky-Website-Summarizer.git
cd websnark
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

### 3. Add your \`.env\` file  

Create a `.env` file:

```bash
GOOGLE_API_KEY= your-real-key-here
GEMINI_API_KEY = the same as in GOOGLE_API_KEY
```

---

## 🧠 How It Works

1. **fetch_website_contents(url)** scrapes the raw readable text.  
2. The text is fed into a **snarky system prompt**.  
3. Gemini creates a summary with:
   - Humor  
   - Markdown formatting  
   - Minimal emotional damage  
4. The result is displayed via Jupyter Markdown.

---
## 👨‍💻 Author

**Selim Ben Haj Braiek**  
🎓 Master’s Student in **Data Science & Artificial Intelligence**  
🏫 *Budapest University of Technology and Economics (BME)*  
 
---

## 🪪 License

This project is licensed under the **MIT License**.  
You’re free to use, modify, and share it for **educational or personal purposes**.  
If you find it useful, feel free to ⭐ star the repo and share it with others! 🚀  

