#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test different
		operations with matrices in Python, using NumPy matrices
		and other 2-D arrays.





	References:
	+ [Schlomer2021]
		- Nico Schl{\"{o}}mer, "Answer to `How do I add an extra column to a NumPy array?'," Stack Exchange Inc., New York, NY, October 4, 2021. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/40218298/1531728 and https://stackoverflow.com/questions/8486294/how-do-i-add-an-extra-column-to-a-numpy-array/40218298#40218298; February 9, 2023 was the last accessed date.
	+ [Schlomer2022]
		- Nico Schl{\"{o}}mer, "perfplot," GitHub, Inc., San Francisco, CA, June 6, 2022. Available online from *GitHub: Nico Schl{\"{o}}mer* at: https://github.com/nschloe/perfplot; February 10, 2023 was the last accessed date.
"""




__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'January 17, 2020'

#	The MIT License (MIT)

#	Copyright (c) <2020> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?











###############################################################
#	Import packages and modules from the Python Standard Library.
import math


###############################################################
#	Import Custom Python Packages and Modules


###############################################################
#	Import packages and modules Python libraries

import numpy as np



import numpy as np
import perfplot

b = perfplot.bench(
    setup=np.random.rand,
    kernels=[
        lambda a: np.c_[a, a],
        lambda a: np.ascontiguousarray(np.stack([a, a]).T),
        lambda a: np.ascontiguousarray(np.vstack([a, a]).T),
        lambda a: np.column_stack([a, a]),
        lambda a: np.concatenate([a[:, None], a[:, None]], axis=1),
        lambda a: np.ascontiguousarray(np.concatenate([a[None], a[None]], axis=0).T),
        lambda a: np.stack([a, a]).T,
        lambda a: np.vstack([a, a]).T,
        lambda a: np.concatenate([a[None], a[None]], axis=0).T,
    ],
    labels=[
        "c_",
        "ascont(stack)",
        "ascont(vstack)",
        "column_stack",
        "concat",
        "ascont(concat)",
        "stack (non-cont)",
        "vstack (non-cont)",
        "concat (non-cont)",
    ],
    n_range=[2 ** k for k in range(23)],
    xlabel="len(a)",
)
b.save("y_matrix_operations.png")
"""
	@Modified by Zhiyang Ong, February 9, 2023.
	Successful attempt to save the plot/figure in PDF format.
"""
b.save("y_matrix_operations.pdf")