import sys
import numpy as np

# we suppose symmetric matrix.
m = []
for y in range(0, int(sys.argv[1])):
  m.append([])
  for x in range(0, int(sys.argv[1])):
    m[- 1].append(eval(sys.argv[2]))
m = np.matrix(m)
m = m * m.transpose()
q, r = np.linalg.qr(m * m.transpose())
print(np.sqrt(abs(r[int(sys.argv[1]) - 1, int(sys.argv[1]) - 1])))

