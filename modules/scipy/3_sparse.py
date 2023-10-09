"""
Sparse data is when the data is rare and spread out. 
Theres a lot of zeros in the data. 
CSR = Commpressed Sparse Row matrix
"""
import numpy as np
from scipy.sparse import csr_matrix



_1x9_arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
_3x3_arr = np.array([[0, 0, 0], 
                     [0, 0, 1], 
                     [1, 0, 2]])
_4x4_arr = np.array([[5, 0, 0, 0], 
                     [0, 8, 0, 0],
                     [0, 0, 3, 0], 
                     [0, 6, 0, 0]])

print("- Basic CSR Matrix ----")
print(_1x9_arr.size)
csr = csr_matrix(_1x9_arr)
print(csr)


print("- 3x3 CSR data ----")
csr = csr_matrix(_3x3_arr)
print(csr)
print(csr.data)

print("- 4x4 CSR data ----")
csr = csr_matrix(_4x4_arr)
print(csr)
print(csr.data)

print("- Count Zeros ----")
csr = csr_matrix(_3x3_arr)
print(csr.data)
print("# zeros: {} ".format(csr.count_nonzero()))

print("- Eliminate Zeros ----")
mat = csr_matrix(_3x3_arr)
mat.eliminate_zeros()
print(mat)
print("# zeros: {} ".format(csr.count_nonzero()))

print("- Sum Dublicates ----")
mat = csr_matrix(_3x3_arr)
mat.sum_duplicates()
print(mat)

print("- CSC Matrix ----")
csr = csr_matrix(_3x3_arr)
csc = csr.tocsc()
print(csc)