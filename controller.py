"""
Controller.py - Controller for Search Algorithms Learning System
Manages interaction between Model and View
"""

from typing import Callable
import tkinter as tk
from model import SearchAlgorithmsModel, AlgorithmGroup
from view import MainMenuView, GroupDetailView


class SearchAlgorithmsController:
    """Controller for managing views and models"""
    
    def __init__(self, root):
        self.root = root
        self.model = SearchAlgorithmsModel()
        self.main_view = MainMenuView(root, self.on_group_selected)
        self.group_view = GroupDetailView(root, self.on_back_to_main)
        self.current_view = None
        
        self._setup_window()
        self.show_main_menu()
    
    def _setup_window(self):
        """Setup main window"""
        self.root.title("Search Algorithms Learning System")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
    
    def show_main_menu(self):
        """Display main menu"""
        if self.current_view == "main":
            return
        
        if self.current_view == "group":
            self.group_view.clear()
        
        self.main_view.render()
        self.current_view = "main"
    
    def on_group_selected(self, group_index: int):
        """Handle group selection"""
        groups = self.model.get_all_groups()
        if 0 <= group_index < len(groups):
            selected_group = groups[group_index]
            self.show_group_detail(selected_group)
    
    def show_group_detail(self, group: AlgorithmGroup):
        """Display algorithms in selected group"""
        if self.current_view == "main":
            self.main_view.clear()
        
        algorithms = self.model.get_algorithms_by_group(group)
        self.group_view.render(group, algorithms)
        self.current_view = "group"
    
    def on_back_to_main(self):
        """Handle back to main menu"""
        self.show_main_menu()
