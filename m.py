import sys
import numpy as np

# we suppose symmetric matrix, integrated input.
m0 = []
m  = []
for yi in range(0, int(sys.argv[1])):
  y = yi / float(int(sys.argv[1]))
  m0.append([])
  for xi in range(0, int(sys.argv[1])):
    x = xi / float(int(sys.argv[1]))
    m0[- 1].append(eval(sys.argv[2]))
for yi in range(1, len(m0)):
  m.append([])
  for xi in range(0, len(m0[yi])):
    m[- 1].append(m0[yi][xi] - m0[yi - 1][xi])
m0 = m
m  = []
for yi in range(0, len(m0)):
  m.append([])
  for xi in range(1, len(m0[yi])):
    m[- 1].append(m0[yi][xi] - m0[yi][xi - 1])
m = np.matrix(m)
m = m * m.transpose()
q, r = np.linalg.qr(m * m.transpose())
print(np.sqrt(abs(r[int(sys.argv[1]) - 2, int(sys.argv[1]) - 2])) * (float(int(sys.argv[1])) - 1) * (float(int(sys.argv[1])) - 1))

