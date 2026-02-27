from pydoc import text
from pyexpat.errors import messages
import tkinter as tk
from tkinter import ttk
from llama_cpp import Llama
import threading
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,      
    "../models",   
    "qwen2.5-coder-3b-instruct-q4_k_m.gguf"
)

if not os.path.exists(model_path):
    raise ValueError(f"Model file not found at {model_path}")

llm = Llama(model_path=model_path)

llm_modes = {
    "Code Generation": "You are a coding assistant. Write clean, correct code in the requested language. Explain briefly what the code does. Always format code in markdown style.",
    "Bug Fixing": "You are a debugging assistant. Analyze the user’s code, identify errors, and suggest corrections step by step. Explain clearly what was wrong.",

}

chat_history = []

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter App")
        self.root.state("zoomed")
        self.combo_var = tk.StringVar()
        self.options = ["Code Generation","Bug fixing"]

        self.label = ttk.Label(self.root, text="Hello, Tkinter!")
        self.label.pack(pady=10)
    
        self.entry = ttk.Entry(self.root)
        self.entry.pack(pady=10)


        self.dropdown = ttk.Combobox(self.root, values=self.options, textvariable=self.combo_var)
        self.dropdown.pack(pady=20, padx=20) 


        self.text_area = tk.Text(self.root, height=30, width=70)
        self.text_area.pack(pady=10)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_ai)
        self.start_button.pack(pady=10) 

        
        
    def change_ai_type(self):
          mode = self.combo_var.get()
          if mode in llm_modes:
            self.custom_prompt = llm_modes[mode]
          else: 
            self.custom_prompt = llm_modes["Code Generation"]
    
    def start_ai(self,):
        self.change_ai_type()
        user_input = self.entry.get()
        threading.Thread(target=self.thread_ai, args=(user_input,), daemon=True).start()



    def thread_ai(self, user_input):
        messages = [{"role": "system", "content": self.custom_prompt}]
        for role, text in chat_history[-6:]:
            messages.append({"role": role.lower(), "content": text})

        messages.append({"role": "user", "content": user_input})

        response = llm.create_chat_completion(messages=messages, max_tokens=512)
        reply = response["choices"][0]["message"]["content"].strip()

        chat_history.append(("user", user_input))
        chat_history.append(("assistant", reply))

        self.root.after(0, lambda: self.text_area.insert(tk.END, reply + "\n\n"))

   
        
    
root = tk.Tk()
app = App(root)
root.mainloop()