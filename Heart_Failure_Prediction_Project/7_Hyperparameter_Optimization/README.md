# 7. Hyperparameter Optimization

## Method: Particle Swarm Optimization (PSO)
Used AIW_PSO (Adaptive Inertia Weight PSO) from the mealpy library to search for optimal GBM hyperparameters.

## Why PSO over Grid Search?
| Aspect | Grid Search | PSO |
|--------|-------------|-----|
| Search strategy | Exhaustive | Intelligent swarm |
| Speed | Slow | Fast |
| Scalability | Poor | Good |
| Local optima | Trapped | Escapes via inertia |

## Search Space
| Parameter | Range | Type |
|-----------|-------|------|
| n_estimators | [50, 300] | Integer |
| max_depth | [2, 8] | Integer |
| learning_rate | [0.01, 0.3] | Float |
| subsample | [0.5, 1.0] | Float |
| min_samples_split | [2, 20] | Integer |

## PSO Configuration
```python
from mealpy.swarm_based.PSO import AIW_PSO

optimizer = AIW_PSO(epoch=30, pop_size=20)
```
- **30 epochs** — number of iterations
- **20 particles** — population size exploring the search space

## Objective Function
```python
def objective_function(solution):
    # Map PSO solution to GBM hyperparameters
    # Evaluate using 5-fold cross-validation
    # Return negative F1 score (PSO minimizes)
```
