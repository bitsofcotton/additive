import sys
import numpy as np
from scipy.linalg import svdvals

# we suppose symmetric matrix.
m = []
for y in range(0, int(sys.argv[1])):
  m.append([])
  for x in range(0, int(sys.argv[1])):
    m[- 1].append(eval(sys.argv[2]))
print(svdvals(np.matrix(m))[- 1])

