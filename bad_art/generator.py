#!/usr/bin/env python3
"""
Abstract art generator using random algorithms
Results: Uniformly terrible
Preserved for posterity
"""

from PIL import Image, ImageDraw
import random
import numpy as np

def generate_chaos_art(width=800, height=600, seed=None):
    """Generate chaotic abstract art"""
    if seed:
        random.seed(seed)
        np.random.seed(seed)
    
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Random shapes
    for _ in range(random.randint(50, 200)):
        shape_type = random.choice(['rectangle', 'ellipse', 'line', 'polygon'])
        color = tuple(random.randint(0, 255) for _ in range(3))
        
        if shape_type == 'rectangle':
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            draw.rectangle([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], fill=color, outline=color)

        elif shape_type == 'ellipse':
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            draw.ellipse([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], fill=color, outline=color)
        
        elif shape_type == 'line':
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            thickness = random.randint(1, 10)
            draw.line([x1, y1, x2, y2], fill=color, width=thickness)
        
        elif shape_type == 'polygon':
            points = [(random.randint(0, width), random.randint(0, height)) 
                     for _ in range(random.randint(3, 8))]
            draw.polygon(points, fill=color, outline=color)
    
    return img

if __name__ == "__main__":
    print("Generating 100 pieces of bad art...")
    for i in range(100):
        img = generate_chaos_art(seed=i)
        img.save(f"samples/chaos_{i:03d}.png")
        if (i + 1) % 10 == 0:
            print(f"Generated {i + 1}/100")
    print("Complete. All pieces are terrible.")