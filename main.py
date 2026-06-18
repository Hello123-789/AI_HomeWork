"""
main.py - Main Application Entry Point
MVC Architecture for Search Algorithms Learning System
"""

import tkinter as tk
from controller import SearchAlgorithmsController


class SearchAlgorithmsApp:
    """Main application class"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.controller = SearchAlgorithmsController(self.root)
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = SearchAlgorithmsApp()
    app.run()
