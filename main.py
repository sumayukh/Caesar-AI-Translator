import os
import subprocess
import sys


curr_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(curr_dir, 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

def run_chatbot():
    chatbot_path = os.path.join(src_path, 'views', 'Caesar.py')
    try:
        if os.path.exists(chatbot_path) is False:
            print(f"Error: File not found")
        else:
            subprocess.run([sys.executable, '-m', 'streamlit', 'run', chatbot_path])
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    run_chatbot()