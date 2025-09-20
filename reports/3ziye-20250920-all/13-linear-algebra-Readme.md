# The Little Book of Linear Algebra

A concise, beginner-friendly introduction to the core ideas of linear algebra.

## Formats

- [Download PDF](book.pdf) – print-ready version
- [Download EPUB](book.epub) – e-reader friendly
- [View LaTeX](book.tex) – Latex source

# Chapter 1. Vectors

## 1.1 Scalars and Vectors

A scalar is a single numerical quantity, most often taken from the real numbers, denoted by $\mathbb{R}$. Scalars are
the fundamental building blocks of arithmetic: they can be added, subtracted, multiplied, and, except in the case of
zero, divided. In linear algebra, scalars play the role of coefficients, scaling factors, and entries of larger
structures such as vectors and matrices. They provide the weights by which more complex objects are measured and
combined. A vector is an ordered collection of scalars, arranged either in a row or a column. When the scalars are real
numbers, the vector is said to belong to *real* $n$-dimensional space, written

$$
\mathbb{R}^n = \{ (x_1, x_2, \dots, x_n) \mid x_i \in \mathbb{R} \}.
$$

An element of $\mathbb{R}^n$ is called a vector of dimension $n$ or an *n*-vector. The number $n$ is called the
dimension of the vector space. Thus $\mathbb{R}^2$ is the space of all ordered pairs of real numbers, $\mathbb{R}^3$ the
space of all ordered triples, and so on.

Example 1.1.1.

- A 2-dimensional vector: $(3, -1) \in \mathbb{R}^2$.
- A 3-dimensional vector: $(2, 0, 5) \in \mathbb{R}^3$.
- A 1-dimensional vector: $(7) \in \mathbb{R}^1$, which corresponds to the scalar \$7$ itself.

Vectors are often written vertically in column form, which emphasizes their role in matrix multiplication:

$$
\mathbf{v} = \begin{bmatrix}
2 \\
0 \\
5 \end{bmatrix} \in \mathbb{R}^3.
$$

The vertical layout makes the structure clearer when we consider linear combinations or multiply matrices by vectors.

### Geometric Interpretation

In $\mathbb{R}^2$, a vector $(x_1, x_2)$ can be visualized as an arrow starting at the origin $(0,0)$ and ending at the
point $(x_1, x_2)$. Its length corresponds to the distance from the origin, and its orientation gives a direction in the
plane. In $\mathbb{R}^3$, the same picture extends into three dimensions: a vector is an arrow from the origin
to $(x_1, x_2, x_3)$. Beyond three dimensions, direct visualization is no longer possible, but the algebraic rules of
vectors remain identical. Even though we cannot draw a vector in $\mathbb{R}^{10}$, it behaves under addition, scaling,
and transformation exactly as a 2- or 3-dimensional vector does. This abstract point of view is what allows linear
algebra to apply to data science, physics, and machine learning, where data often lives in very high-dimensional spaces.
Thus a vector may be regarded in three complementary ways:

1. As a point in space, described by its coordinates.
2. As a displacement or arrow, described by a direction and a length.
3. As an abstract element of a vector space, whose properties follow algebraic rules independent of geometry.

### Notation

- Vectors are written in boldface lowercase letters: $\mathbf{v}, \mathbf{w}, \mathbf{x}$.
- The *i*-th entry of a vector $\mathbf{v}$ is written $v_i$, where indices begin at 1.
- The set of all *n*-dimensional vectors over $\mathbb{R}$ is denoted $\mathbb{R}^n$.
- Column vectors will be the default form unless otherwise stated.

### Why begin here?

Scalars and vectors form the atoms of linear algebra. Every structure we will build-vector spaces, linear
transformations, matrices, eigenvalues-relies on the basic notions of number and ordered collection of numbers. Once
vectors are understood, we can define operations such as addition and scalar multiplication, then generalize to
subspaces, bases, and coordinate systems. Eventually, this framework grows into the full theory of linear algebra, with
powerful applications to geometry, computation, and data.

### Exercises 1.1

1. Write three different vectors in $\mathbb{R}^2$ and sketch them as arrows from the origin. Identify their coordinates
   explicitly.
2. Give an example of a vector in $\mathbb{R}^4$. Can you visualize it directly? Explain why high-dimensional
   visualization is challenging.
3. Let $\mathbf{v} = (4, -3, 2)$. Write $\mathbf{v}$ in column form and state $v_1, v_2, v_3$.
4. In what sense is the set $\mathbb{R}^1$ both a line and a vector space? Illustrate with examples.
5. Consider the vector $\mathbf{u} = (1,1,\dots,1) \in \mathbb{R}^n$. What is special about this vector when $n$ is
   large? What might it represent in applications?

## 1.2 Vector Addition and Scalar Multiplication

Vectors in linear algebra are not static objects; their power comes from the operations we can perform on them. Two
fundamental operations define the structure of vector spaces: addition and scalar multiplication. These operations
satisfy simple but far-reaching rules that underpin the entire subject.

### Vector Addition

Given two vectors of the same dimension, their sum is obtained by adding