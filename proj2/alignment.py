# alignment.py: Reads from standard input, the output produced by
# edit_distance.py, i.e., input strings x and y, and the opt matrix. The
# program then recovers an optimal alignment from opt, and writes to
# standard output the edit distance between x and y and the alignment itself.

import stdarray
import stdio

# Read x, y, and opt from standard input.
x = stdio.readLine()
y = stdio.readLine()
di = stdio.readLine()

# Compute M and N.
M = len(x)
N = len(y)
opt = stdarray.create2D(M+1, N+1, 0)

for i in range(M+1):
    for j in range(N+1):
        opt[i][j] = stdio.readInt()

# Write edit distance between x and y.
stdio.writef('Edit distance = %d', opt[0][0])
stdio.writeln()

# Recover and write an optimal alignment.
i = 0
j = 0
while i in range(M):
    while j in range(N):
        if i in range(M):
            if (opt[i][j] == opt[i+1][j]+2):
                stdio.writeln(str(x[i]) + ' - ' + '2')
                i += 1
            elif (opt[i][j] == opt[i][j+1]+2):
                stdio.writeln('- ' + str(y[j]) + ' 2')
                j += 1
            else:
                if (x[i] == y[j]):
                    stdio.writeln(str(x[i]) + ' ' + str(y[j]) + ' 0')
                else:
                    stdio.writeln(str(x[i]) + ' ' + str(y[j]) + ' 1')
                i += 1
                j += 1
        elif j in range(N):
            if (opt[i][j] == opt[i][j+1]+2):
                stdio.writeln('- ' + str(y[j]) + ' 2')
                j += 1
            else:
                if (x[i] == y[j]):
                    stdio.writeln(str(x[i]) + ' ' + str(y[j]) + ' 0')
                else:
                    stdio.writeln(str(x[i]) + ' ' + str(y[j]) + ' 1')
                i += 1
                j += 1
        else:
            if (x[i] == y[j]):
                stdio.writeln(str(x[i]) + ' ' + str(y[j]) + ' 0')
            else:
                stdio.writeln(str(x[i]) + ' ' + str(y[j]) + ' 1')
            i += 1
            j += 1
