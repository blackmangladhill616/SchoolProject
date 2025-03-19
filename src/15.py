import numpy as np

def random_code(n):
    """Generates a random Python code of length n."""
    code = []
    for i in range(n):
        code.append(np.random.choice(['print', 'if', 'for', 'while', 'import', 'from', 'def', 'class', 'lambda']))
    return ''.join(code)