import os
import sys
import time
from datetime import datetime
from pynput import keyboard, mouse  #type: ignore
import json

class InputMonitor:
    def __init__(self, output_path):
        self.output_path = output_path
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S') # Time Stamp for File
        self.log_file = os.path.join(output_path, f"activity_log_{timestamp}.txt")
        self.keylog_file = os.path.join(output_path, f"keystroke_log_{timestamp}.txt")
        self.stats_file = os.path.join(output_path, "statistics.json")
        
        self.key_count = 0 # Keystroke counter
        self.mouse_count = 0 # Click counter
        self.key_buffer = [] # Store keys until "Enter" is pressed
        self.start_time = datetime.now() # Tracking time
        self.running = True # Boolean for when program is running
        
        # Consent and transparency
        self.show_consent_notice()
        
    def show_consent_notice(self):
        """Display clear consent notice before starting"""
        print("=" * 70)
        print("INPUT MONITOR - EDUCATIONAL DEMONSTRATION")
        print("=" * 70)
        print("\n WARNING: This program captures keyboard and mouse activity.")
        print("\nData collected:")
        print("  - Activity log: Timestamped events (clicks, keypresses)")
        print("  - Keystroke log: ACTUAL text typed (including passwords)")
        print("  - Statistics: Summary of activity")
        print(f"\nLogs will be saved to: {self.output_path}")
        print("\n FOR EDUCATIONAL/DEMONSTRATION PURPOSES ONLY")
        print(" Use only on systems you own or have explicit permission")
        print("\nPress Ctrl+C at any time to stop monitoring.")
        print("=" * 70)
        
        consent = input("\nI consent to this monitoring (type 'I CONSENT'): ")
        if consent != 'I CONSENT':
            print("Consent not given. Exiting...")
            sys.exit(0)
        
        print("\n Consent received. Starting monitor...")
        print(" Two logs will be generated:")
        print(f" - Activity log: {os.path.basename(self.log_file)}")
        print(f" - Keystroke log: {os.path.basename(self.keylog_file)}")
        print(" Press Ctrl+C to stop\n")
    
    def on_key_press(self, key):
        """Track keyboard activity and capture actual keystrokes"""
        try:
            self.key_count += 1
            timestamp = datetime.now().strftime('%H:%M:%S')
            
            # Log to activity log (generic)
            self.log_activity("KEYBOARD", f"Key press detected")
            
            # Log to keystroke log (detailed)
            if hasattr(key, 'char') and key.char is not None:
                # Regular character key
                self.key_buffer.append(key.char)
                self.log_keystroke(timestamp, key.char)
            else:
                # Special keys
                key_name = str(key).replace('Key.', '')
                
                if key_name == 'space':
                    self.key_buffer.append(' ')
                    self.log_keystroke(timestamp, '[SPACE]')
                elif key_name == 'enter':
                    self.key_buffer.append('\n')
                    self.log_keystroke(timestamp, '[ENTER]')
                    self.flush_keystroke_buffer()
                elif key_name == 'backspace':
                    if self.key_buffer:
                        self.key_buffer.pop()
                    self.log_keystroke(timestamp, '[BACKSPACE]')
                elif key_name == 'tab':
                    self.key_buffer.append('\t')
                    self.log_keystroke(timestamp, '[TAB]')
                else:
                    self.log_keystroke(timestamp, f'[{key_name.upper()}]')
                    
        except Exception as e:
            pass
    
    def on_mouse_click(self, x, y, button, pressed):
        """Track mouse clicks"""
        if pressed:
            self.mouse_count += 1
            self.log_activity("MOUSE", f"Click at ({x}, {y}) - {button}")
    
    def log_activity(self, activity_type, details):
        """Write activity to log file"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {activity_type}: {details}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry)
    
    def log_keystroke(self, timestamp, key):
        """Write detailed keystroke to keystroke log"""
        log_entry = f"[{timestamp}] {key}\n"
        
        with open(self.keylog_file, 'a') as f:
            f.write(log_entry)
    
    def flush_keystroke_buffer(self):
        """Write current buffer as a complete line"""
        if self.key_buffer:
            timestamp = datetime.now().strftime('%H:%M:%S')
            line = ''.join(self.key_buffer)
            
            with open(self.keylog_file, 'a') as f:
                f.write(f"\n--- Complete line at [{timestamp}] ---\n")
                f.write(f"{line}\n")
                f.write("-" * 50 + "\n\n")
            
            self.key_buffer = []
    
    def save_statistics(self):
        """Save summary statistics"""
        duration = (datetime.now() - self.start_time).total_seconds()
        
        stats = {
            "session_start": self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "session_end": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "duration_seconds": duration,
            "total_keystrokes": self.key_count,
            "total_mouse_clicks": self.mouse_count,
            "average_keys_per_minute": round((self.key_count / duration) * 60, 2) if duration > 0 else 0
        }
        
        with open(self.stats_file, 'w') as f:
            json.dump(stats, f, indent=4)
        
        return stats
    
    def display_summary(self):
        """Display session summary"""
        stats = self.save_statistics()
        
        print("\n" + "=" * 60)
        print("SESSION SUMMARY")
        print("=" * 60)
        print(f"Duration: {stats['duration_seconds']:.2f} seconds")
        print(f"Total Keystrokes: {stats['total_keystrokes']}")
        print(f"Total Mouse Clicks: {stats['total_mouse_clicks']}")
        print(f"Average Keys/Minute: {stats['average_keys_per_minute']}")
        print(f"\n Activity log: {self.log_file}")
        print(f"  Keystroke log: {self.keylog_file}")
        print(f" Statistics: {self.stats_file}")
        print("=" * 60)
    
    def start_monitoring(self):
        """Start keyboard and mouse listeners"""
        # Create activity log file with header
        with open(self.log_file, 'w') as f:
            f.write(f"Activity Log - Summary Events\n")
            f.write(f"Session Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"User Consent: YES\n")
            f.write("=" * 60 + "\n\n")
        
        # Create keystroke log file with header
        with open(self.keylog_file, 'w') as f:
            f.write(f"Keystroke Log - Detailed Capture\n")
            f.write(f"Session Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"User Consent: YES\n")
            f.write(f"  Contains actual keystrokes including sensitive data\n")
            f.write("=" * 60 + "\n\n")
        
        # Start listeners
        keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        
        keyboard_listener.start()
        mouse_listener.start()
        
        try:
            # Keep running until interrupted
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nStopping tracker...")
            self.running = False
            
            # Flush any remaining keystrokes
            if self.key_buffer:
                self.flush_keystroke_buffer()
            
            keyboard_listener.stop()
            mouse_listener.stop()
            self.display_summary()

def main():
    # Check for USB drive or use current directory
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    else:
        output_path = os.path.join(os.getcwd(), "productivity_logs")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Initialize and start tracker
    tracker = InputMonitor(output_path)
    tracker.start_monitoring()

if __name__ == "__main__":
    main()