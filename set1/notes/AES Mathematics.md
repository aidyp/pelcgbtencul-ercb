# AES Mathematics



## Overview

This document contains notes about the algebraic structure behind AES. It's better to write it here so I can come back to it later, rather than try and remember all the various notebooks I've made



## Modular Multiplication

AES defines the modular product $d(x) = a(x) \otimes b(x)$ is defined as,
$$
\begin{align*}
d(x) &= d_3x^3 + d_2x^2 + d_1x + d_0 \\
\text{with,} \\
d_0 &= (a_0 \cdot b_0) \oplus (a_3 \cdot b_1) \oplus (a_2 \cdot b_2) \oplus (a_1 \cdot b_3) \\
d_1 &= (a_1 \cdot b_0) \oplus (a_0 \cdot b_1) \oplus (a_3 \cdot b_2) \oplus (a_2 \cdot b_3) \\
d_2 &= (a_2 \cdot b_0) \oplus (a_1 \cdot b_1) \oplus (a_0 \cdot b_2) \oplus (a_3 \cdot b_3) \\
d_3 &= (a_3 \cdot b_0) \oplus (a_2 \cdot b_1) \oplus (a_1 \cdot b_2) \oplus (a_0 \cdot b_3) \\
\end{align*}
$$

During the `mixColumns()` stage of AES encryption, each 4-byte word in the state is multiplied by the polynomial $a(x) = \{03\}x^3 + \{01\}x^2 + \{01\}x + \{02\}$. Let the 4-byte word be $w(x)$, then,
$$
\begin{align*}
d(x) &= a(x) \otimes w(x) \\
d_0 &= (\{03\} \cdot b_0) \oplus (a_3 \cdot b_1) \oplus (a_2 \cdot b_2) \oplus (a_1 \cdot b_3) \\
d_0 &= (\{03\} \cdot b_0) \oplus (a_3 \cdot b_1) \oplus (a_2 \cdot b_2) \oplus (a_1 \cdot b_3) \\
d_0 &= (\{03\} \cdot b_0) \oplus (a_3 \cdot b_1) \oplus (a_2 \cdot b_2) \oplus (a_1 \cdot b_3) \\
d_0 &= (\{03\} \cdot b_0) \oplus (a_3 \cdot b_1) \oplus (a_2 \cdot b_2) \oplus (a_1 \cdot b_3) \\
\end{align*}
$$

$$
\begin{align*}
d(x) &= a(x) \otimes w(x) \\
d_0 &= (\{03\} \cdot w_0) \oplus (\{02\} \cdot w_1) \oplus (\{01\}\cdot w_2) \oplus (\{01\} \cdot w_3) \\
d_1 &= (\{01\} \cdot w_0) \oplus (\{03\} \cdot w_1) \oplus (\{02\} \cdot w_2) \oplus (\{01\} \cdot w_3) \\
d_2 &= (\{02\} \cdot w_0) \oplus (\{01\} \cdot w_1) \oplus (\{03\} \cdot w_2) \oplus (\{02\} \cdot w_3) \\
d_3 &= (\{02\} \cdot w_0) \oplus (\{02\} \cdot w_1) \oplus (\{01\} \cdot w_2) \oplus (\{03\} \cdot w_3) \\
\end{align*}
$$

