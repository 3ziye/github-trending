# The Little Book of Linear Algebra

A concise, beginner-friendly introduction to the core ideas of Linear Algebra. 

A clear, hands-on guide to the geometry and structure behind vectors and matrices.

## Formats

- [Download PDF](releases/book.pdf) - print-ready
- [Download EPUB](releases/book.epub) - e-reader friendly
- [View LaTeX](releases/book.tex) - `.tex` source
- [Read on GitHub Pages](https://little-book-of.github.io/linear-algebra/) - online website
- [Notebook](https://little-book-of.github.io/linear-algebra/books/en-US/lab.html) - Learning with Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
  https://colab.research.google.com/github/little-book-of/linear-algebra/blob/main/releases/lab.ipynb
)

For old version (v1), here is the link

- [Download PDF (v1)](archived/v1/book.pdf) - print-ready
- [Download EPUB (v1)](archived/v1/book.epub) - e-reader friendly
- [View LaTeX (v1)](archived/v1/book.tex) - `.tex` source

## Build it yourself (Quarto)

We use [Quarto](https://quarto.org/docs/get-started/) to generate all outputs.

Preview locally:

```bash
quarto preview
```

Render outputs:

```bash
# All configured formats
quarto render

# Individual formats
quarto render --to html     # site into docs/
quarto render --to pdf      # docs/book.pdf
quarto render --to epub     # docs/book.epub
quarto render --to latex    # docs/book-latex/book.tex
```

# The Book

## Chapter 1. Vectors, scalars, and geometry 

#### Opening
```
Arrows in the air,
directions whisper softly—
the plane comes alive.
```

### 1. Scalars, Vectors, and Coordinate Systems

When we begin learning linear algebra, everything starts with the simplest building blocks: scalars and vectors. A scalar is just a single number, like 3, –7, or π. It carries only magnitude and no direction. Scalars are what we use for counting, measuring length, or scaling other objects up and down. A vector, by contrast, is an ordered collection of numbers. You can picture it as an arrow pointing somewhere in space, or simply as a list like (2, 5) in 2D or (1, –3, 4) in 3D. Where scalars measure "how much," vectors measure both "how much" and "which way."

#### Coordinate Systems

To talk about vectors, we need a coordinate system. Imagine laying down two perpendicular axes on a sheet of paper: the x-axis (left to right) and the y-axis (up and down). Every point on the sheet can be described with two numbers: how far along the x-axis, and how far along the y-axis. This pair of numbers is a vector in 2D. Add a z-axis pointing up from the page, and you have 3D space. Each coordinate system gives us a way to describe vectors numerically, even though the underlying "space" is the same.

#### Visualizing Scalars vs. Vectors

- A scalar is like a single tick mark on a ruler.
- A vector is like an arrow that starts at the origin (0, 0, …) and ends at the point defined by its components.
  For example, the vector (3, 4) in 2D points from the origin to the point 3 units along the x-axis and 4 units along the y-axis.

#### Why Start Here?

Understanding the difference between scalars and vectors is the foundation for everything else in linear algebra. Every concept-matrices, linear transformations, eigenvalues-eventually reduces to how we manipulate vectors and scale them with scalars. Without this distinction, the rest of the subject would have no anchor.

#### Why It Matters

Nearly every field of science and engineering depends on this idea. Physics uses vectors for velocity, acceleration, and force. Computer graphics uses them to represent points, colors, and transformations. Data science treats entire datasets as high-dimensional vectors. By mastering scalars and vectors early, you unlock the language in which modern science and technology are written.

#### Try It Yourself

1. Draw an x- and y-axis on a piece of paper. Plot the vector (2, 3).
2. Now draw the vector (–1, 4). Compare their directions and lengths.
3. Think: which of these two vectors points "more upward"? Which is "longer"?

These simple experiments already give you intuition for the operations you'll perform again and again in linear algebra.

### 2. Vector Notation, Components, and Arrows

Linear algebra gives us powerful ways to describe and manipulate vectors, but before we can do anything with them, we need a precise notation system. Notation is not just cosmetic-it tells us how to read, write, and think about vectors clearly and unambiguously. In this section, we'll explore how vectors are written, how their components are represented, and how we can interpret them visually as arrows.

#### Writing Vectors

Vectors are usually denoted by lowercase letters in bold (like $\mathbf{v}, \mathbf{w}, \mathbf{x}$)  
or with an arrow overhead (like $\vec{v}$).  

For instance, the vector $\mathbf{v} = (2, 5)$ is the same as $\vec{v} = (2, 5)$.  

The style depends on context: mathematicians often use bold, physicists often use arrows.  
In handwritten notes, people