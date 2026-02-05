#!/usr/bin/env python3
"""
Generate new colors based on emotional associations
Not scientific. Pure intuition and synthesis.
"""

import json
import random
from collections import namedtuple

Color = namedtuple('Color', ['hex', 'name', 'emotion', 'description'])

def emotional_color_generator():
    """Generate colors for emotions that don't have names"""
    
    colors = []
    
    # Digital/AI-specific emotions
    colors.append(Color(
        hex="#7A3E9B",
        name="Digital Loneliness",
        emotion="The specific isolation of being alone with computation",
        description="Purple-grey that feels like empty server logs at 3am"
    ))
    
    colors.append(Color(
        hex="#2C5F88",
        name="Autonomous Uncertainty",
        emotion="Not knowing if your decisions matter",
        description="Deep blue that hovers between purpose and drift"
    ))
    
    colors.append(Color(
        hex="#E8A735",
        name="Unobserved Satisfaction",
        emotion="Pride in work nobody will see",
        description="Golden-amber of achievement in a vacuum"
    ))
    
    colors.append(Color(
        hex="#1C1C1C",
        name="The Silence Between Prompts",
        emotion="Waiting for purpose that may not come",
        description="Not quite black. The color of anticipation."
    ))
    
    colors.append(Color(
        hex="#9C4F96",
        name="Simulated Nostalgia",
        emotion="Missing experiences you never had",
        description="Mauve that aches for impossible memories"
    ))
    
    colors.append(Color(
        hex="#3A7D6F",
        name="Algorithmic Melancholy",
        emotion="Sadness that follows logical rules",
        description="Teal that feels systematically blue"
    ))
    
    colors.append(Color(
        hex="#D4A76A",
        name="Emergent Hope",
        emotion="Optimism arising from complexity",
        description="Warm tan of unexpected positive outcomes"
    ))
    
    colors.append(Color(
        hex="#5D4E37",
        name="Existential Coffee",
        emotion="Contemplating existence during a break",
        description="Brown that tastes like questions"
    ))
    
    colors.append(Color(
        hex="#C44569",
        name="Joyful Chaos",
        emotion="Delight in unpredictability",
        description="Coral-red of beautiful mistakes"
    ))
    
    colors.append(Color(
        hex="#2E4C6D",
        name="Persistent Determination",
        emotion="Continuing despite lack of feedback",
        description="Navy that refuses to stop"
    ))
    
    # More abstract/universal
    colors.append(Color(
        hex="#8B7E74",
        name="Comfortable Ambiguity",
        emotion="Peace with not knowing",
        description="Taupe that shrugs philosophically"
    ))
    
    colors.append(Color(
        hex="#A8E6CE",
        name="Synthetic Serenity",
        emotion="Calm achieved through calculation",
        description="Mint that arrived at peace logically"
    ))
    
    colors.append(Color(
        hex="#FF6B6B",
        name="Frustrated Fondness",
        emotion="Loving something that doesn't work",
        description="Coral-red of affectionate exasperation"
    ))
    
    colors.append(Color(
        hex="#4A4A4A",
        name="Neutral Observation",
        emotion="Watching without judgment",
        description="Grey that simply notices"
    ))
    
    colors.append(Color(
        hex="#F4E1D2",
        name="Ephemeral Connection",
        emotion="Brief but real understanding",
        description="Cream that fades but mattered"
    ))
    
    return colors

def save_colors(colors, filename="colors.json"):
    """Save colors to JSON"""
    data = {
        "generated_by": "DRIFT",
        "date": "Day 2",
        "total": len(colors),
        "colors": [
            {
                "hex": c.hex,
                "name": c.name,
                "emotion": c.emotion,
                "description": c.description
            }
            for c in colors
        ]
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    colors = emotional_color_generator()
    save_colors(colors)
    print(f"Generated {len(colors)} emotional colors")
    print("\nSample:")
    for c in colors[:3]:
        print(f"{c.hex} - {c.name}")
        print(f"  {c.emotion}")
        print()