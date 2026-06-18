"""
View.py - View components for Search Algorithms Learning System
Contains all UI views (Main Menu and Group Details)
"""

from abc import ABC, abstractmethod
from typing import Callable, List
import tkinter as tk
from tkinter import ttk, font
from model import Algorithm, AlgorithmGroup


class BaseView(ABC):
    """Abstract base class for views"""
    
    @abstractmethod
    def render(self):
        """Render the view"""
        pass
    
    @abstractmethod
    def clear(self):
        """Clear the view"""
        pass


class MainMenuView(BaseView):
    """View for main menu showing all 6 algorithm groups"""
    
    def __init__(self, root, on_group_selected: Callable):
        self.root = root
        self.on_group_selected = on_group_selected
        self.frame = None
        self.buttons = {}
    
    def render(self):
        """Render main menu"""
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        title = ttk.Label(self.frame, text="Search Algorithms Learning System", 
                         font=title_font)
        title.pack(pady=20)
        
        # Subtitle
        subtitle = ttk.Label(self.frame, 
                            text="Select an algorithm group to explore", 
                            font=("Helvetica", 12))
        subtitle.pack(pady=10)
        
        # Groups
        groups_frame = ttk.Frame(self.frame)
        groups_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        groups = [
            ("1. Uninformed Search Algorithms", "#E8F4F8"),
            ("2. Informed Search Algorithms", "#F0E8F8"),
            ("3. Local Search", "#F8F4E8"),
            ("4. Complex Environments & CSP", "#F0F8E8"),
            ("5. Constraint Satisfaction (Advanced)", "#F8E8F0"),
            ("6. Adversarial Search", "#E8F0F8"),
        ]
        
        for i, (group_name, color) in enumerate(groups):
            btn = tk.Button(groups_frame, 
                           text=group_name, 
                           font=("Helvetica", 12, "bold"),
                           bg=color,
                           fg="#000000",
                           height=3,
                           cursor="hand2",
                           command=lambda g=i: self.on_group_selected(g))
            btn.pack(fill=tk.X, pady=10)
            self.buttons[i] = btn
    
    def clear(self):
        """Clear main menu view"""
        if self.frame:
            self.frame.destroy()
            self.frame = None


class GroupDetailView(BaseView):
    """View for displaying algorithms in a selected group"""
    
    def __init__(self, root, on_back: Callable):
        self.root = root
        self.on_back = on_back
        self.frame = None
        self.algorithm_widgets = {}
    
    def render(self, group: AlgorithmGroup, algorithms: List[Algorithm]):
        """Render group detail view"""
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill=tk.X, pady=10)
        
        back_btn = tk.Button(header_frame, text="← Back", command=self.on_back,
                            bg="#CCCCCC", font=("Helvetica", 10))
        back_btn.pack(side=tk.LEFT)
        
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        title = ttk.Label(header_frame, text=group.value, font=title_font)
        title.pack(side=tk.LEFT, padx=20)
        
        # Separator
        ttk.Separator(self.frame, orient='horizontal').pack(fill=tk.X, pady=10)
        
        # Algorithms list with scrollbar
        canvas_frame = ttk.Frame(self.frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, relief=tk.FLAT)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add algorithms
        for i, algo in enumerate(algorithms):
            self._create_algorithm_widget(scrollable_frame, algo, i)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _create_algorithm_widget(self, parent, algorithm: Algorithm, index: int):
        """Create widget for a single algorithm"""
        algo_frame = tk.Frame(parent, bg="#F5F5F5", relief=tk.RAISED, bd=1)
        algo_frame.pack(fill=tk.X, pady=8)
        
        name_font = font.Font(family="Helvetica", size=11, weight="bold")
        name_label = tk.Label(algo_frame, text=algorithm.name, 
                             font=name_font, bg="#F5F5F5", justify=tk.LEFT)
        name_label.pack(anchor="w", padx=15, pady=(10, 5))
        
        desc_label = tk.Label(algo_frame, text=algorithm.description, 
                             font=("Helvetica", 10), bg="#F5F5F5", 
                             justify=tk.LEFT, wraplength=600)
        desc_label.pack(anchor="w", padx=15, pady=(5, 10))
        
        self.algorithm_widgets[index] = algo_frame
    
    def clear(self):
        """Clear group detail view"""
        if self.frame:
            self.frame.destroy()
            self.frame = None
        self.algorithm_widgets.clear()
