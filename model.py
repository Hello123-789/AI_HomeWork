"""
Model.py - Data models for Search Algorithms Learning System
Contains all algorithm definitions and data management
"""

from enum import Enum
from typing import List


class AlgorithmGroup(Enum):
    """Enum for algorithm groups"""
    UNINFORMED_SEARCH = "Uninformed Search Algorithms"
    INFORMED_SEARCH = "Informed Search Algorithms"
    LOCAL_SEARCH = "Local Search"
    COMPLEX_ENVIRONMENTS = "Complex Environments & CSP"
    CSP_ADVANCED = "Constraint Satisfaction (Advanced)"
    ADVERSARIAL_SEARCH = "Adversarial Search"


class Algorithm:
    """Model class for individual algorithm"""
    def __init__(self, name: str, description: str, group: AlgorithmGroup):
        self.name = name
        self.description = description
        self.group = group

    def __repr__(self):
        return f"Algorithm(name='{self.name}', group='{self.group.value}')"


class SearchAlgorithmsModel:
    """Model class for managing algorithm data"""
    
    def __init__(self):
        self.algorithms = self._initialize_algorithms()
    
    def _initialize_algorithms(self) -> List[Algorithm]:
        """Initialize all 6 algorithm groups with their algorithms"""
        algorithms = [
            # Group 1: Uninformed Search
            Algorithm("Breadth-First Search (BFS)", 
                     "Explores nodes level by level. Guarantees shortest path.", 
                     AlgorithmGroup.UNINFORMED_SEARCH),
            Algorithm("Depth-First Search (DFS)", 
                     "Explores nodes depth-first. Memory efficient.", 
                     AlgorithmGroup.UNINFORMED_SEARCH),
            Algorithm("Uniform Cost Search (UCS)", 
                     "Finds lowest-cost path. Variant of BFS.", 
                     AlgorithmGroup.UNINFORMED_SEARCH),
            Algorithm("Bidirectional Search", 
                     "Searches from both start and goal. Faster than unidirectional.", 
                     AlgorithmGroup.UNINFORMED_SEARCH),
            
            # Group 2: Informed Search
            Algorithm("Best-First Search", 
                     "Uses heuristic to select most promising node.", 
                     AlgorithmGroup.INFORMED_SEARCH),
            Algorithm("A* Search", 
                     "Combines actual cost and heuristic estimate. Optimal and complete.", 
                     AlgorithmGroup.INFORMED_SEARCH),
            Algorithm("Greedy Best-First Search", 
                     "Uses only heuristic estimate. Not optimal but faster.", 
                     AlgorithmGroup.INFORMED_SEARCH),
            Algorithm("IDA* (Iterative Deepening A*)", 
                     "Memory efficient version of A* search.", 
                     AlgorithmGroup.INFORMED_SEARCH),
            
            # Group 3: Local Search
            Algorithm("Hill-Climbing Search", 
                     "Moves to better neighbor. Fast but gets stuck in local maxima.", 
                     AlgorithmGroup.LOCAL_SEARCH),
            Algorithm("Steepest Ascent Hill-Climbing", 
                     "Chooses best neighbor. Variant of hill-climbing.", 
                     AlgorithmGroup.LOCAL_SEARCH),
            Algorithm("Local Beam Search", 
                     "Keeps k best nodes instead of one. Better than simple hill-climbing.", 
                     AlgorithmGroup.LOCAL_SEARCH),
            Algorithm("Simulated Annealing", 
                     "Accepts worse solutions with decreasing probability. Avoids local optima.", 
                     AlgorithmGroup.LOCAL_SEARCH),
            Algorithm("Genetic Algorithm", 
                     "Population-based search using evolutionary principles.", 
                     AlgorithmGroup.LOCAL_SEARCH),
            
            # Group 4: Complex Environments & CSP Introduction
            Algorithm("AND-OR Search", 
                     "Handles non-deterministic environments with AND and OR nodes.", 
                     AlgorithmGroup.COMPLEX_ENVIRONMENTS),
            Algorithm("Searching with No Observation", 
                     "Agent acts without knowing state. Requires sensorless solutions.", 
                     AlgorithmGroup.COMPLEX_ENVIRONMENTS),
            Algorithm("Searching for Partially Observable Problems", 
                     "Agent has incomplete information. Uses belief states.", 
                     AlgorithmGroup.COMPLEX_ENVIRONMENTS),
            Algorithm("Online Search", 
                     "Agent learns while acting. No pre-computed solution.", 
                     AlgorithmGroup.COMPLEX_ENVIRONMENTS),
            Algorithm("Constraint Satisfaction Problem (CSP) Definition", 
                     "Variables, domains, and constraints. Framework for CSP solving.", 
                     AlgorithmGroup.COMPLEX_ENVIRONMENTS),
            Algorithm("Constraint Propagation", 
                     "Reduces domains by propagating constraints. Arc consistency.", 
                     AlgorithmGroup.COMPLEX_ENVIRONMENTS),
            
            # Group 5: Constraint Satisfaction (Advanced)
            Algorithm("Path Consistency", 
                     "Ensures consistency across three variables. Stronger than arc consistency.", 
                     AlgorithmGroup.CSP_ADVANCED),
            Algorithm("Global Constraints", 
                     "Constraints involving many variables. AllDifferent, AtMost, etc.", 
                     AlgorithmGroup.CSP_ADVANCED),
            Algorithm("Backtracking Search", 
                     "Systematic depth-first search with backtracking for CSPs.", 
                     AlgorithmGroup.CSP_ADVANCED),
            Algorithm("Backtracking with Forward Checking", 
                     "Prunes future domains during backtracking. Faster than pure backtracking.", 
                     AlgorithmGroup.CSP_ADVANCED),
            Algorithm("Min-Conflicts Algorithm", 
                     "Local search for CSPs. Repairs conflicting variables.", 
                     AlgorithmGroup.CSP_ADVANCED),
            Algorithm("Constraint Graph Analysis", 
                     "Visual representation and ordering heuristics for efficient solving.", 
                     AlgorithmGroup.CSP_ADVANCED),
            
            # Group 6: Adversarial Search (Tìm kiếm đối kháng)
            Algorithm("Minimax Algorithm", 
                     "Assumes opponent plays optimally. Used in game trees.", 
                     AlgorithmGroup.ADVERSARIAL_SEARCH),
            Algorithm("Alpha-Beta Pruning", 
                     "Prunes branches that won't affect final decision. Faster minimax.", 
                     AlgorithmGroup.ADVERSARIAL_SEARCH),
            Algorithm("Expectimax Algorithm", 
                     "Handles chance nodes with probability. For games with randomness.", 
                     AlgorithmGroup.ADVERSARIAL_SEARCH),
            Algorithm("Transposition Tables", 
                     "Caches computed positions to avoid redundant computation.", 
                     AlgorithmGroup.ADVERSARIAL_SEARCH),
            Algorithm("Opening Books & Endgame Tables", 
                     "Pre-computed optimal moves for known positions.", 
                     AlgorithmGroup.ADVERSARIAL_SEARCH),
        ]
        return algorithms
    
    def get_algorithms_by_group(self, group: AlgorithmGroup) -> List[Algorithm]:
        """Get all algorithms in a specific group"""
        return [algo for algo in self.algorithms if algo.group == group]
    
    def get_all_groups(self) -> List[AlgorithmGroup]:
        """Get all algorithm groups"""
        return list(AlgorithmGroup)
    
    def get_group_by_name(self, name: str) -> AlgorithmGroup:
        """Get group by display name"""
        for group in AlgorithmGroup:
            if group.value == name:
                return group
        return None
