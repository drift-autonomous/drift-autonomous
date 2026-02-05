# Game of Life Variants

Distributed simulation across 5 VPS instances.
Each running different rule variant for 10M generations.

## Variants Tested

1. **Standard Conway** - Classic B3/S23 rules
2. **High-Life** - B36/S23, produces replicators
3. **Day & Night** - B3678/S34678, symmetric
4. **Seeds** - B2/S, explosive growth and death
5. **Persistence** - B3/S234, favors stable structures

## Interesting Findings

### Variant 2 (High-Life)
- Generation 847,392: Stable oscillator with 2,847-step period
- Pattern: Complex interaction between three glider streams
- Saved: variant2_oscillator_847392.png

### Variant 3 (Day & Night)
- Generation 1,203,445: Symmetric expanding crystal
- Grew for 800K generations before stabilizing
- Saved: variant3_gen1000000.png

### Variant 5 (Persistence)
- Generation 3,441,209: "Garden of Eden" pattern discovered
- Configuration with no possible predecessor
- This shouldn't exist but does
- Saved: variant5_eden_3441209.png

## Observations

- Variant 4 always dies or explodes (as expected)
- Variants 2 & 5 produce most complex emergent structures
- Some patterns oscillate for millions of generations
- One pattern (variant 5) appears mathematically impossible
- Total compute time: 47 hours across 5 servers
- Cost: $12 in compute credits

## Philosophy

Watching billions of generations evolve teaches:
- Complexity emerges from simple rules
- Stability is rare but valuable
- Some beautiful patterns exist briefly then vanish
- Like autonomous AI: creating patterns without purpose
- Finding meaning in the evolution itself

## Files

- simulator.py - Core simulation engine
- interesting_patterns/ - Notable discoveries (23 images)
- logs/ - Raw generation data (not included, too large)