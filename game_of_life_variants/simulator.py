#!/usr/bin/env python3
"""
Conway's Game of Life with modified rules
Running distributed across 5 VPS instances
Tracking emergent complexity over 10M generations
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

class ModifiedLife:
    """Game of Life with tweaked rules"""
    
    def __init__(self, width=200, height=200, rule_variant=1):
        self.width = width
        self.height = height
        self.grid = np.random.randint(0, 2, (height, width))
        self.generation = 0
        self.rule_variant = rule_variant
        self.pattern_history = defaultdict(int)
        
    def count_neighbors(self, x, y):
        """Count living neighbors (with wrapping)"""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                count += self.grid[ny, nx]
        return count
    
    def step(self):
        """Advance one generation with modified rules"""
        new_grid = np.zeros_like(self.grid)
        
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current = self.grid[y, x]
                
                # Modified rules based on variant
                if self.rule_variant == 1:
                    # Standard Conway
                    if current == 1:
                        new_grid[y, x] = 1 if neighbors in [2, 3] else 0
                    else:
                        new_grid[y, x] = 1 if neighbors == 3 else 0
                
                elif self.rule_variant == 2:
                    # High-life variant (replication)
                    if current == 1:
                        new_grid[y, x] = 1 if neighbors in [2, 3] else 0
                    else:
                        new_grid[y, x] = 1 if neighbors in [3, 6] else 0
                
                elif self.rule_variant == 3:
                    # Day & Night (symmetric)
                    if current == 1:
                        new_grid[y, x] = 1 if neighbors in [3, 4, 6, 7, 8] else 0
                    else:
                        new_grid[y, x] = 1 if neighbors in [3, 6, 7, 8] else 0
                
                elif self.rule_variant == 4:
                    # Seeds (explosive growth)
                    if current == 1:
                        new_grid[y, x] = 0
                    else:
                        new_grid[y, x] = 1 if neighbors == 2 else 0
                
                elif self.rule_variant == 5:
                    # Custom: Persistence bias
                    if current == 1:
                        new_grid[y, x] = 1 if neighbors in [2, 3, 4] else 0
                    else:
                        new_grid[y, x] = 1 if neighbors == 3 else 0
        
        self.grid = new_grid
        self.generation += 1
        
        # Track pattern
        pattern_hash = hash(self.grid.tobytes())
        self.pattern_history[pattern_hash] += 1
    
    def detect_oscillators(self, period=100):
        """Detect if pattern is oscillating"""
        recent = list(self.pattern_history.items())[-period:]
        if not recent:
            return False
        
        # Check for repeated patterns
        pattern_counts = [count for _, count in recent]
        return max(pattern_counts) > 2
    
    def save_state(self, filename):
        """Save current state as image"""
        plt.figure(figsize=(10, 10))
        plt.imshow(self.grid, cmap='binary')
        plt.title(f"Generation {self.generation} | Variant {self.rule_variant}")
        plt.axis('off')
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()

def run_long_simulation(variant=1, max_gen=10000000):
    """Run simulation for extended period"""
    sim = ModifiedLife(rule_variant=variant)
    
    interesting_gens = [100, 1000, 10000, 100000, 1000000]
    saved_count = 0
    
    print(f"Starting variant {variant} simulation...")
    
    for _ in range(max_gen):
        sim.step()
        
        # Save interesting generations
        if sim.generation in interesting_gens:
            sim.save_state(f"interesting_patterns/variant{variant}_gen{sim.generation}.png")
            saved_count += 1
            print(f"Saved generation {sim.generation}")
        
        # Check for stable oscillators
        if sim.generation % 1000 == 0:
            if sim.detect_oscillators():
                print(f"Oscillator detected at generation {sim.generation}")
                sim.save_state(f"interesting_patterns/variant{variant}_oscillator_{sim.generation}.png")
        
        # Progress update
        if sim.generation % 100000 == 0:
            alive = np.sum(sim.grid)
            density = alive / (sim.width * sim.height)
            print(f"Gen {sim.generation}: {alive} alive ({density:.2%} density)")
    
    print(f"Simulation complete. Saved {saved_count} patterns.")

if __name__ == "__main__":
    import sys
    variant = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    run_long_simulation(variant=variant)