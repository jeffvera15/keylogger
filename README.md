# Keylogger



A Python-based educational cybersecurity project demonstrating input monitoring capabilities with explicit user consent. This tool captures keyboard and mouse activity for productivity analysis and security research purposes.

## ⚠️ Legal Disclaimer

**FOR EDUCATIONAL AND DEMONSTRATION PURPOSES ONLY.**

This software is intended solely for:
- Educational cybersecurity demonstrations
- Personal productivity tracking on your own devices
- Security research in controlled environments

**You must:**
- Only use on systems you own
- Obtain explicit permission before monitoring any system
- Comply with all applicable laws and regulations

Unauthorized use of keylogging software may violate computer fraud, privacy, and wiretapping laws. The author assumes no liability for misuse of this software.

## 🎯 Project Purpose

This project demonstrates:
- Real-time input event monitoring using Python
- Ethical security tool design with consent mechanisms
- File I/O and data logging techniques
- Object-oriented programming in Python
- Understanding of how keyloggers function at a technical level

## ✨ Features

- **Dual Logging System:**
  - Activity log: High-level event timestamps
  - Keystroke log: Detailed character-by-character capture with line reconstruction

- **Mouse Tracking:** Records click positions and button types

- **Statistics Generation:** Session duration, keystroke count, clicks per minute

- **Explicit Consent Mechanism:** Requires user to type "I CONSENT" before monitoring begins

- **Transparent Operation:** Clear warnings about data collection

- **User Control:** Stop monitoring anytime with Ctrl+C

## 📋 Prerequisites

Before running this project, ensure you have:

### 1. Python Installation

**Check if Python is installed:**
```bash
python --version
```

**If not installed:**
- **Windows:** Download from [python.org](https://www.python.org/downloads/) (Python 3.11 or higher)
  - ✅ Check "Add Python to PATH" during installation
- **Mac:** `brew install python3`
- **Linux:** `sudo apt install python3 python3-pip`

### 2. pip (Python Package Manager)

Usually comes with Python. Verify with:
```bash
pip --version
```

## 🚀 Installation

### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/jeffvera15/keylogger.git
cd keylogger
```

Or download the ZIP file and extract it.

### Step 2: Install Required Libraries
```bash
pip install pynput
```

**What this installs:**
- `pynput` - Library for monitoring and controlling input devices
- `six` - Python 2/3 compatibility library (dependency)

## 💻 Usage

### Running the Program

1. **Open a terminal/command prompt**

2. **Navigate to the project directory:**
```bash
   cd C:\path\to\keylogger
```
   *(Replace with your actual path)*

3. **Run the script:**
```bash
   python logger.py
```

4. **Provide Consent:**
   - Read the warning message
   - Type exactly: `I CONSENT`
   - Press Enter

5. **Monitoring Begins:**
   - Use your computer normally
   - All keyboard and mouse activity is logged
   - Files are saved to `productivity_logs/` folder

6. **Stop Monitoring:**
   - Press `Ctrl+C` in the terminal
   - View session summary
   - Check output files

### Running with Custom Output Directory
```bash
# Save logs to a USB drive
python logger.py E:\logs

# Save to a specific folder
python logger.py C:\Users\YourUsername\Documents\monitor_logs
```

## 📁 Output Files

The program generates three types of files in `productivity_logs/`:

### 1. `activity_log_[timestamp].txt`
Generic event log showing:
```
[2025-12-08 17:33:36] KEYBOARD: Key press detected
[2025-12-08 17:33:37] MOUSE: Click at (542, 318) - Button.left
[2025-12-08 17:33:38] KEYBOARD: Key press detected
```

### 2. `keystroke_log_[timestamp].txt`
Detailed keystroke capture showing:
```
[17:33:36] h
[17:33:36] e
[17:33:37] l
[17:33:37] l
[17:33:37] o
[17:33:38] [SPACE]
[17:33:38] w
[17:33:38] o
[17:33:39] r
[17:33:39] l
[17:33:39] d
[17:33:40] [ENTER]

--- Complete line at [17:33:40] ---
hello world
--------------------------------------------------
```

### 3. `statistics.json`
Session summary with metrics:
```json
{
    "session_start": "2025-12-08 17:33:35",
    "session_end": "2025-12-08 17:45:12",
    "duration_seconds": 697.43,
    "total_keystrokes": 487,
    "total_mouse_clicks": 23,
    "average_keys_per_minute": 41.89
}
```

## 🏗️ Project Structure
```
keylogger/
├── logger.py              # Main application script
├── requirements.txt       # Python dependencies
├── productivity_logs/     # Output directory (created automatically)
│   ├── activity_log_*.txt
│   ├── keystroke_log_*.txt
│   └── statistics.json
└── README.md             # This file
```

## 🧪 Testing the Project

For demonstration purposes:

1. Run the program
2. Open Notepad or any text editor
3. Type some test sentences
4. Click around with your mouse
5. Stop the program (Ctrl+C)
6. Review the generated log files to see captured data

## 🛠️ Technical Details

**Built with:**
- Python 3.11+
- `pynput` library for input monitoring

**Key Components:**
- `InputMonitor` class: Main application logic
- Event listeners: Background threads monitoring keyboard/mouse
- File handlers: UTF-8 encoded logging system
- Buffer system: Reconstructs typed lines from individual keystrokes

**Design Patterns:**
- Object-oriented design
- Event-driven architecture
- Consent-first approach

## 🎓 Learning Objectives

By studying this project, you'll understand:
- How input monitoring works at a system level
- Python event handling and threading
- File I/O operations and data persistence
- Ethical considerations in security tools
- Real-world application of OOP principles

## 🐛 Troubleshooting

**"pynput could not be resolved"**
- Solution: Run `pip install pynput` again
- Or create a virtual environment (see Advanced Setup)

**"Permission denied" errors**
- Solution: Run terminal as Administrator (Windows) or use `sudo` (Linux/Mac)

**Logs not capturing special characters**
- This is expected - some keys like function keys are logged as `[F1]`, `[CTRL]`, etc.

**Program crashes on startup**
- Ensure Python 3.11+ is installed
- Check that pynput installed correctly: `pip show pynput`

## 🔒 Privacy & Security Notes

- All data is stored locally - nothing is transmitted over the network
- Log files contain sensitive information - protect them accordingly
- Delete log files when no longer needed
- Consider encrypting output files for added security

## 📝 License

MIT License - For educational use only.

## 👨‍💻 Author

Created for educational cybersecurity demonstrations.

## 🤝 Contributing

This is an educational project. If you're using it for learning:
- Fork the repository
- Add features (encrypted logs, GUI, etc.)
- Document your changes
- Share your improvements

## 📚 Further Reading

- [pynput documentation](https://pynput.readthedocs.io/)
- [CFAA Overview](https://www.justice.gov/criminal-ccips/ccmanual)
- [Ethical Hacking Resources](https://www.offensive-security.com/)
