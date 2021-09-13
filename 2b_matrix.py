import numpy as np
import time

# Generate two integer matrices.
def create_int_matrices():
    m1 = np.random.randint(100, size=(250, 500), dtype=np.intc)
    m2 = np.random.randint(100, size=(500, 250), dtype=np.intc)
    return (m1, m2)

# Generate two double matrices.
def create_double_matrices():
    m1 = np.random.rand(250, 500)
    m2 = np.random.rand(500, 250)
    return (m1, m2)

# Multiple the matrices together.
def multiply_matrices(matrices):
    sum = 0
    count = 0
    # Collect 10 samples.
    for i in range(10):
        start = time.time()
        m1, m2 = matrices
        npdot = np.dot(m1, m2)
        time_elapsed = time.time() - start
        print(time_elapsed)
        sum += time_elapsed
        count += 1
    avg_time_elapsed = sum / count
    print("Average: ", avg_time_elapsed)

def main():
    print('2b. Improved method\nInteger Matrix Execution Time:')
    multiply_matrices(create_int_matrices())
    print('\nDouble Matrix Execution Time:')
    multiply_matrices(create_double_matrices())

if __name__ == "__main__":
    main()
