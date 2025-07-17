---
# =============================================================================
# COMMON METADATA
# =============================================================================
title: "Real and Complex Mathematical Analysis"
author: "Arithmoi Foundation"
date: "May 23, 2025"
description: "A comprehensive guide to real and complex mathematical analysis, covering foundations, sequences, series, continuity, differentiation, integration, and complex function theory."

# =============================================================================
# PDF-SPECIFIC METADATA (mdtexpdf only)
# =============================================================================
# Document structure
format: "book"
section: "foundations"

# Section numbering
no_numbers: true

# Headers and footers
header_footer_policy: "all"
footer: " 2025 Arithmoi Foundation | arithmoi.org. All rights reserved."
pageof: true
date_footer: "DD/MM/YY"
---

# Real and Complex Mathematical Analysis

# Part 1: Real Analysis

## Chapter 1: Foundations of Real Numbers

### 1.1 The Real Number System

The **real numbers**, denoted by $\mathbb{R}$ (pronounced "R, the set of real numbers"), are a fundamental building block of mathematical analysis. Real numbers include:

- The rational numbers $\mathbb{Q}$ (pronounced "Q, the set of rationals"): numbers that can be written as fractions, $\frac{p}{q}$, where $p$ and $q$ are integers and $q \neq 0$.
- The irrational numbers: numbers that cannot be written as fractions, such as $\sqrt{2}$ and $\pi$ (pronounced "pi").

**Properties of $\mathbb{R}$:**

- **Field properties**: Real numbers can be added, subtracted, multiplied, and divided (except by zero), and these operations satisfy the usual field axioms.
- **Order properties**: The real numbers have a total order; for any $a, b \in \mathbb{R}$, we can say $a < b$, $a = b$, or $a > b$.
- **Completeness**: Every non-empty set of real numbers that is bounded above has a least upper bound (supremum).

### 1.2 The Completeness Axiom

The **completeness axiom** is a defining property of the real numbers. It is what distinguishes $\mathbb{R}$ from $\mathbb{Q}$.

**Completeness Axiom Statement:**

For every non-empty subset $S \subseteq \mathbb{R}$ that is bounded above, there exists a least upper bound (supremum) $s_0 \in \mathbb{R}$ such that:

$$
\forall x \in S, \quad x \leq s_0
$$

and

$$
\forall \epsilon > 0, \quad \exists x_0 \in S \text{ such that } s_0 - \epsilon < x_0 \leq s_0
$$

Here, $\epsilon$ (pronounced "epsilon") is any positive real number, representing an arbitrarily small quantity.

- **Supremum** (least upper bound): The smallest real number that is greater than or equal to every element of $S$.

### 1.3 Order Properties of $\mathbb{R}$

The real numbers are an **ordered field**, which means:

- For any $a, b, c \in \mathbb{R}$:
  - If $a < b$, then $a + c < b + c$
  - If $a < b$ and $c > 0$, then $ac < bc$
  - For any $a \in \mathbb{R}$, exactly one of $a = 0$, $a > 0$, or $a < 0$ is true (trichotomy law)

These properties allow us to compare and manipulate inequalities involving real numbers.

### 1.4 The Archimedean Property and Density of $\mathbb{Q}$

#### Archimedean Property

The **Archimedean property** states that:

For any real number $x$, there exists a natural number $n \in \mathbb{N}$ such that 

$$
n > x
$$

where $\mathbb{N}$ (pronounced "N, the set of natural numbers") is the set $\{1, 2, 3, \dots\}$.

#### Density of $\mathbb{Q}$

The **rational numbers** are **dense** in $\mathbb{R}$. This means:

Between any two real numbers $a$ and $b$ with $a < b$, there exists a rational number $q$ such that

$$
a < q < b
$$

This property is essential for constructing sequences and for approximation arguments in analysis.

### 1.5 Supremum and Infimum (Least Upper and Greatest Lower Bounds)

Given a subset $S \subseteq \mathbb{R}$:

- An **upper bound** for $S$ is any $u \in \mathbb{R}$ such that $x \leq u$ for all $x \in S$.
- The **supremum** (least upper bound), denoted $\sup S$, is the smallest upper bound of $S$.

Similarly:

- A **lower bound** for $S$ is any $l \in \mathbb{R}$ such that $x \geq l$ for all $x \in S$.
- The **infimum** (greatest lower bound), denoted $\inf S$, is the largest lower bound of $S$.

**Formal Definitions:**

Let $S$ be a non-empty subset of $\mathbb{R}$.

- $u$ is an **upper bound** of $S$ if $\forall x \in S, \ x \leq u$.
- $s_0$ is the **supremum** of $S$ if:
  - $s_0$ is an upper bound of $S$
  - For any $\epsilon > 0$, there exists $x_0 \in S$ such that $s_0 - \epsilon < x_0$

The **infimum** is defined analogously.

### 1.6 The Extended Real Number System

The **extended real number system** augments $\mathbb{R}$ with two symbols, $+\infty$ and $-\infty$ (pronounced "plus infinity" and "minus infinity"), to handle limits and unbounded sets.

- The set is denoted $\overline{\mathbb{R}} = \mathbb{R} \cup \{+\infty, -\infty\}$
- For any real $x$:
  - $x < +\infty$
  - $x > -\infty$

**Applications:**

- Useful when working with limits, especially in improper integrals and measures.



#### Exercises

1. Prove that between any two distinct real numbers, there is an irrational number.
2. Show that the set $S = \{x \in \mathbb{Q} : x^2 < 2\}$ is bounded above in $\mathbb{Q}$, but its supremum does not belong to $\mathbb{Q}$.
3. Give an example of a non-empty set $S \subseteq \mathbb{R}$ that is bounded below but does not attain its infimum.

## Chapter 2: Sequences and Series

### 2.1 Sequences of Real Numbers

A **sequence** is a function from the natural numbers $\mathbb{N} = \{1, 2, 3, \ldots\}$ into the real numbers $\mathbb{R}$. We typically write a sequence as $(x_n)_{n=1}^{\infty}$ or simply $(x_n)$, where $n$ is the index.

- $x_n$ (pronounced "x sub n") is the $n$-th term of the sequence.

Example: The sequence $x_n = \frac{1}{n}$ is the sequence $(1, \frac{1}{2}, \frac{1}{3}, \ldots)$.

### 2.2 Convergence and Divergence of Sequences

A sequence $(x_n)$ **converges** to a real number $L$ if, for every $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that

$$
|x_n - L| < \epsilon \quad \text{whenever} \quad n \geq N
$$

Here, $|x_n - L|$ means the absolute value of $x_n - L$. If such an $L$ exists, we write

$$
\lim_{n \to \infty} x_n = L
$$

If no such $L$ exists, the sequence is said to **diverge**.

#### Explanation of Symbols

- $\epsilon$ ("epsilon"): an arbitrarily small positive real number.
- $N$: a natural number indicating how far out in the sequence we must go for the terms to get close to $L$.

### 2.3 Limit Superior and Limit Inferior

For a sequence $(x_n)$, the **limit superior** and **limit inferior** are defined as follows:

- The **limit superior** (lim sup), denoted $\limsup_{n \to \infty} x_n$, is the smallest real number $L$ such that, for every $\epsilon > 0$, $x_n < L + \epsilon$ eventually (for all large $n$), and infinitely often $x_n > L - \epsilon$.

- The **limit inferior** (lim inf), denoted $\liminf_{n \to \infty} x_n$, is the largest real number $l$ such that, for every $\epsilon > 0$, $x_n > l - \epsilon$ eventually, and infinitely often $x_n < l + \epsilon$.

Formally, for sequence $(x_n)$,

$$
\limsup_{n \to \infty} x_n = \lim_{n \to \infty} \sup \{ x_k : k \geq n \}
$$

$$
\liminf_{n \to \infty} x_n = \lim_{n \to \infty} \inf \{ x_k : k \geq n \}
$$

- $\sup$ ("supremum") and $\inf$ ("infimum") are as defined previously.

### 2.4 Monotone Sequences and the Monotone Convergence Theorem

A sequence $(x_n)$ is **monotone increasing** if $x_{n+1} \geq x_n$ for all $n$, and **monotone decreasing** if $x_{n+1} \leq x_n$ for all $n$.

**The Monotone Convergence Theorem** states:

- Every bounded monotone sequence converges.

That is, if $(x_n)$ is monotone and there exist real numbers $m, M$ such that

$$
m \leq x_n \leq M
$$

for all $n$, then $(x_n)$ converges to a real number $L$.

### 2.5 Subsequences and the Bolzano–Weierstrass Theorem

A **subsequence** of $(x_n)$ is a sequence $(x_{n_k})$ where $n_1 < n_2 < n_3 < \cdots$ is a strictly increasing sequence of natural numbers.

**Bolzano–Weierstrass Theorem:**

- Every bounded sequence in $\mathbb{R}$ has a convergent subsequence.

This theorem is fundamental for compactness and limit arguments.

### 2.6 Cauchy Sequences and Completeness

A sequence $(x_n)$ is a **Cauchy sequence** if, for every $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that

$$
|x_n - x_m| < \epsilon \quad \text{whenever} \quad n, m \geq N
$$

**Completeness of $\mathbb{R}$:**  
Every Cauchy sequence in $\mathbb{R}$ converges to a real number.

This property is what makes $\mathbb{R}$ a "complete" metric space.

### 2.7 Infinite Series: Definitions and Convergence

An **infinite series** is the formal sum

$$
\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots
$$

The **partial sum** $S_N$ is

$$
S_N = \sum_{n=1}^{N} a_n
$$

The series **converges** if the sequence $(S_N)$ converges (as $N \to \infty$).

### 2.8 Tests for Series Convergence

There are several standard tests:

- **Comparison Test:** If $0 \leq a_n \leq b_n$ and $\sum b_n$ converges, then $\sum a_n$ converges.
- **Ratio Test:** If

  $$
  L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|
  $$

  and $L < 1$, then the series converges absolutely. If $L > 1$, the series diverges.

- **Root Test:** If

  $$
  L = \limsup_{n \to \infty} \sqrt[n]{|a_n|}
  $$

  and $L < 1$, the series converges absolutely.

- **Integral Test:** For positive, decreasing $a_n = f(n)$, if $\int_1^\infty f(x) dx$ converges, then $\sum a_n$ converges.

### 2.9 Absolute and Conditional Convergence

A series $\sum a_n$ is **absolutely convergent** if $\sum |a_n|$ converges.

- If a series is absolutely convergent, it is convergent.

A series is **conditionally convergent** if $\sum a_n$ converges but $\sum |a_n|$ diverges.

Example: The alternating harmonic series

$$
\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}
$$

converges, but the harmonic series

$$
\sum_{n=1}^{\infty} \frac{1}{n}
$$

diverges.

### 2.10 Rearrangements of Series

For absolutely convergent series, any rearrangement of the terms converges to the same sum.

For conditionally convergent series, **Riemann's Rearrangement Theorem** states that the terms can be rearranged to converge to any real number (or to diverge).

#### Exercises

1. Prove that every convergent sequence is a Cauchy sequence.
2. Give an example of a sequence that has subsequences converging to different limits.
3. Determine whether the series $\sum_{n=1}^{\infty} \frac{1}{n^2}$ converges or diverges.
4. Show that the sequence $x_n = (-1)^n$ does not converge, but has subsequences that do.

## Chapter 3: Topology of the Real Line

### 3.1 Open and Closed Sets in $\mathbb{R}$

An **open set** $U \subseteq \mathbb{R}$ is a set such that for every point $x \in U$, there exists a real number $\epsilon > 0$ (pronounced "epsilon") such that the open interval $(x - \epsilon, x + \epsilon)$ is entirely contained in $U$:

$$
\forall x \in U, \ \exists \epsilon > 0 \ \text{such that} \ (x - \epsilon, x + \epsilon) \subseteq U
$$

The interval $(a, b) = \{ x \in \mathbb{R} \mid a < x < b \}$ is an example of an open set.

A **closed set** $F \subseteq \mathbb{R}$ is a set whose complement $\mathbb{R} \setminus F$ is open. Equivalently, $F$ contains all its **limit points** (see 3.2).

The interval $[a, b] = \{ x \in \mathbb{R} \mid a \leq x \leq b \}$ is an example of a closed set.

### 3.2 Limit Points, Isolated Points, and Closure

A point $x \in \mathbb{R}$ is a **limit point** (or accumulation point) of a set $A \subseteq \mathbb{R}$ if every open interval around $x$ contains at least one point of $A$ different from $x$ itself:

$$
\forall \epsilon > 0, \ (A \cap (x - \epsilon, x + \epsilon) \setminus \{x\}) \neq \emptyset
$$

A point $x \in A$ is an **isolated point** of $A$ if there exists $\epsilon > 0$ such that $(x - \epsilon, x + \epsilon) \cap (A \setminus \{x\}) = \emptyset$.

The **closure** of a set $A$, denoted $\overline{A}$ (pronounced "A bar"), is the set of all points $x \in \mathbb{R}$ such that every open interval around $x$ contains a point of $A$. That is, $\overline{A}$ is the union of $A$ and all its limit points.

### 3.3 Compact Sets and the Heine–Borel Theorem

A set $K \subseteq \mathbb{R}$ is **compact** if every open cover of $K$ has a finite subcover. That is, given any family of open sets $\{U_\alpha\}_{\alpha \in I}$ such that

$$
K \subseteq \bigcup_{\alpha \in I} U_\alpha,
$$

there exists a finite subset $J \subseteq I$ such that

$$
K \subseteq \bigcup_{\alpha \in J} U_\alpha.
$$

**Heine–Borel Theorem:**  
A set $K \subseteq \mathbb{R}$ is compact **if and only if** it is closed and bounded.

- "Closed" means $K$ contains all its limit points.
- "Bounded" means there exists $M > 0$ such that $|x| \leq M$ for all $x \in K$.

### 3.4 Connected Sets and Intervals

A set $A \subseteq \mathbb{R}$ is **connected** if it cannot be written as the union of two non-empty, disjoint open subsets of $A$.

Equivalent characterization:  
A set $A \subseteq \mathbb{R}$ is connected **if and only if** it is an interval (possibly infinite in extent).

An **interval** is any set of the form

- $(a, b)$, $[a, b)$, $(a, b]$, $[a, b]$ (with $a < b$),
- $(-\infty, b)$, $(a, \infty)$, or $(-\infty, \infty)$.

### 3.5 The Cantor Set

The **Cantor set** is a classic example of a set that is uncountable, closed, has measure zero, and contains no intervals.

**Construction:**

1. Start with the closed interval $[0, 1]$.
2. Remove the open middle third $(\frac{1}{3}, \frac{2}{3})$.
3. Remove the middle third of each remaining segment.
4. Repeat ad infinitum.

The resulting set is the **Cantor set**, denoted $C$. It has the following properties:

- $C$ is closed (it contains all its limit points).
- $C$ is **nowhere dense** (it contains no intervals).
- $C$ is uncountable.

#### Exercises

1. Prove that the intersection of any collection of closed sets is closed.
2. Give an example of a set that is closed but not open, and a set that is open but not closed.
3. Show that every finite subset of $\mathbb{R}$ is closed.
4. Describe the set of all limit points of the set $A = \left\{ \frac{1}{n} : n \in \mathbb{N} \right\}$.

## Chapter 4: Continuity

### 4.1 Limits of Functions

Let $f: D \to \mathbb{R}$, where $D \subseteq \mathbb{R}$, and let $a$ be a limit point of $D$. We say that the **limit** of $f(x)$ as $x$ approaches $a$ is $L$, and write

$$
\lim_{x \to a} f(x) = L
$$

if, for every $\epsilon > 0$, there exists $\delta > 0$ such that

$$
0 < |x - a| < \delta \implies |f(x) - L| < \epsilon
$$

Here:
- $\epsilon$ ("epsilon") is an arbitrarily small positive real number.
- $\delta$ ("delta") is a positive real number depending on $\epsilon$.

This formalizes the idea that $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $a$ (but not equal to $a$).

### 4.2 Continuous Functions and Their Properties

A function $f: D \to \mathbb{R}$ is **continuous at a point** $a \in D$ if

$$
\lim_{x \to a} f(x) = f(a)
$$

That is, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
|x - a| < \delta \implies |f(x) - f(a)| < \epsilon
$$

A function is **continuous on $D$** if it is continuous at every point $a \in D$.

**Properties of continuous functions:**

- The sum, product, and quotient (where the denominator is nonzero) of continuous functions are continuous.
- The composition of continuous functions is continuous.

### 4.3 Types of Discontinuities

A function $f$ is **discontinuous** at $a$ if it is not continuous at $a$. Discontinuities are classified as:

- **Removable Discontinuity:** $\lim_{x \to a} f(x)$ exists, but $f(a)$ is not equal to this limit or is undefined.
- **Jump Discontinuity:** The left-hand and right-hand limits exist at $a$ but are not equal.
- **Essential (or Infinite) Discontinuity:** At least one of the one-sided limits does not exist or is infinite.

### 4.4 The Intermediate Value Theorem

**Theorem (Intermediate Value Theorem):**  
If $f$ is continuous on $[a, b]$ and $k$ is any number between $f(a)$ and $f(b)$, then there is a $c \in [a, b]$ such that

$$
f(c) = k
$$

This theorem formalizes the intuitive idea that continuous functions on an interval attain every value between their endpoints.

### 4.5 The Extreme Value Theorem

**Theorem (Extreme Value Theorem):**  
If $f$ is continuous on a closed interval $[a, b]$, then $f$ attains both a maximum and a minimum value on $[a, b]$. That is, there exist points $c, d \in [a, b]$ such that

$$
f(c) \leq f(x) \leq f(d) \quad \text{for all} \ x \in [a, b]
$$

### 4.6 Uniform Continuity

A function $f: D \to \mathbb{R}$ is **uniformly continuous** on $D$ if, for every $\epsilon > 0$, there exists $\delta > 0$ such that for all $x, y \in D$,

$$
|x - y| < \delta \implies |f(x) - f(y)| < \epsilon
$$

The key difference from pointwise continuity: $\delta$ depends only on $\epsilon$, not on the point in the domain.

**Theorem:**  
Every continuous function on a closed, bounded interval $[a, b]$ is uniformly continuous.

### 4.7 Continuity and Compactness

If $f: K \to \mathbb{R}$ is continuous and $K$ is compact, then $f(K)$ is also compact.

As a result:
- $f$ is bounded on $K$
- $f$ attains its maximum and minimum values on $K$

### 4.8 Continuity and Connectedness

If $f: A \to \mathbb{R}$ is continuous and $A$ is connected, then $f(A)$ is also connected. In $\mathbb{R}$, this means $f(A)$ is an interval whenever $A$ is an interval.

#### Exercises

1. Prove that the function $f(x) = x^2$ is continuous on $\mathbb{R}$.
2. Give an example of a function that is continuous everywhere except at a single point.
3. Let $f$ be continuous on $[0, 1]$ with $f(0) < 0$ and $f(1) > 0$. Show that there exists $c \in (0, 1)$ such that $f(c) = 0$.
4. Give an example of a function that is continuous but not uniformly continuous, and explain why.

## Chapter 5: Differentiation

### 5.1 The Derivative and Its Interpretation

Let $f: D \to \mathbb{R}$ with $D \subseteq \mathbb{R}$ and $a \in D$ be a limit point. The **derivative** of $f$ at $a$, denoted $f'(a)$ (read as "f prime of a"), is defined as:

$$
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
$$

provided this limit exists.

- $h$ is a real number approaching $0$.
- The derivative represents the instantaneous rate of change of $f$ at $a$ or the slope of the tangent line to the graph of $f$ at $x = a$.

### 5.2 Rules for Differentiation

Let $f$ and $g$ be differentiable at $a$ and $c$ a constant. Then:

- **Linearity:**
  $$
  (cf + g)'(a) = c f'(a) + g'(a)
  $$
- **Product Rule:**
  $$
  (f \cdot g)'(a) = f'(a)g(a) + f(a)g'(a)
  $$
- **Quotient Rule:** If $g(a) \neq 0$,
  $$
  \left(\frac{f}{g}\right)'(a) = \frac{f'(a)g(a) - f(a)g'(a)}{[g(a)]^2}
  $$
- **Chain Rule:** If $f$ is differentiable at $a$ and $g$ is differentiable at $f(a)$,
  $$
  (g \circ f)'(a) = g'(f(a)) \cdot f'(a)
  $$
  where $g \circ f$ is the composition $x \mapsto g(f(x))$.

### 5.3 Mean Value Theorems (Rolle, Lagrange)

**Rolle’s Theorem:**  
If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then there exists $c \in (a, b)$ such that

$$
f'(c) = 0
$$

**Mean Value Theorem (Lagrange’s Theorem):**  
If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then there exists $c \in (a, b)$ such that

$$
f'(c) = \frac{f(b) - f(a)}{b - a}
$$

This says that the instantaneous rate of change (derivative) equals the average rate of change at some point.

### 5.4 Taylor’s Theorem and Taylor Series

Let $f$ be $n+1$ times differentiable at $a$. The **Taylor polynomial** of degree $n$ about $a$ is:

$$
P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n
$$

The **remainder** $R_n(x)$ is given by:

$$
f(x) = P_n(x) + R_n(x)
$$

where

$$
R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

for some $\xi$ between $a$ and $x$.

- $f^{(k)}(a)$ denotes the $k$-th derivative of $f$ at $a$.
- $n!$ ("n factorial") is the product $1 \cdot 2 \cdots n$.

### 5.5 L’Hôpital’s Rule

Let $f$ and $g$ be differentiable on an open interval containing $a$, except possibly at $a$, and suppose

$$
\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0 \quad \text{or} \quad \pm\infty
$$

If $g'(x) \neq 0$ near $a$ and $\lim_{x \to a} \frac{f'(x)}{g'(x)}$ exists or is $\pm\infty$, then

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
$$

provided the right-hand limit exists.

### 5.6 Higher-Order Derivatives

The **second derivative** of $f$ at $a$ is the derivative of $f'$ at $a$, denoted $f''(a)$ or $\frac{d^2f}{dx^2}(a)$ ("d squared f by d x squared at a").

Higher-order derivatives are defined similarly:

$$
f^{(n)}(a) = \frac{d^n f}{dx^n}(a)
$$

where $f^{(n)}$ is the $n$-th derivative.

### 5.7 The Inverse Function Theorem (Single Variable)

**Theorem:**  
Let $f$ be continuously differentiable on an open interval $I$ and $f'(a) \neq 0$ at some $a \in I$. Then there exists an open interval $J$ containing $a$ such that $f$ is invertible on $J$, and the inverse function $f^{-1}$ is differentiable at $f(a)$, with

$$
(f^{-1})'(f(a)) = \frac{1}{f'(a)}
$$

### 5.8 The Implicit Function Theorem (Single Variable)

Suppose $F(x, y)$ is continuously differentiable and $F(a, b) = 0$, with $\frac{\partial F}{\partial y}(a, b) \neq 0$ (the partial derivative of $F$ with respect to $y$ at $(a, b)$ is not zero). Then, there exists a function $y = f(x)$ defined near $x = a$ such that $F(x, f(x)) = 0$ near $(a, b)$, and

$$
f'(x) = -\frac{\frac{\partial F}{\partial x}(x, f(x))}{\frac{\partial F}{\partial y}(x, f(x))}
$$

#### Exercises

1. Compute the derivative of $f(x) = \sin(x) e^{x}$.
2. Show that the function $f(x) = |x|$ is not differentiable at $x = 0$.
3. Use the Mean Value Theorem to show that if $f'(x) = 0$ everywhere on $[a, b]$, then $f$ is constant on $[a, b]$.
4. Find the Taylor polynomial of degree 3 for $f(x) = \ln(1+x)$ at $x=0$.
5. Give an example where L’Hôpital’s Rule applies and compute the limit.

## Chapter 6: Riemann Integration

### 6.1 Definition of the Riemann Integral

Let $f: [a, b] \to \mathbb{R}$ be a bounded function. To define the **Riemann integral** of $f$ on $[a, b]$:

- Divide $[a, b]$ into subintervals using a **partition** $P = \{x_0, x_1, \ldots, x_n\}$ with $a = x_0 < x_1 < \ldots < x_n = b$.
- For each subinterval $[x_{i-1}, x_i]$, choose a sample point $t_i \in [x_{i-1}, x_i]$.

The **Riemann sum** is

$$
S(P, f) = \sum_{i=1}^{n} f(t_i) (x_i - x_{i-1})
$$

The function $f$ is **Riemann integrable** on $[a, b]$ if there exists a real number $I$ such that for every $\epsilon > 0$, there exists $\delta > 0$ so that for every partition $P$ with mesh $|P| < \delta$, and for any choice of sample points, we have

$$
\left| S(P, f) - I \right| < \epsilon
$$

If so, $I$ is called the **Riemann integral** of $f$ from $a$ to $b$, written as

$$
\int_{a}^{b} f(x) \, dx
$$

### 6.2 Integrability Criteria

A bounded function $f: [a, b] \to \mathbb{R}$ is Riemann integrable if and only if the set of points where $f$ is discontinuous has measure zero (is "small" in a precise sense).

All continuous functions on $[a, b]$ are Riemann integrable.

### 6.3 Properties of the Riemann Integral

Let $f, g$ be Riemann integrable on $[a, b]$ and $c$ a real constant:

- **Linearity:**
  $$
  \int_{a}^{b} (cf(x) + g(x)) \, dx = c \int_{a}^{b} f(x) \, dx + \int_{a}^{b} g(x) \, dx
  $$
- **Additivity over Intervals:**
  $$
  \int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx
  $$
  for any $c \in [a, b]$.
- **Order Preservation:** If $f(x) \geq 0$ for all $x \in [a, b]$, then
  $$
  \int_{a}^{b} f(x) \, dx \geq 0
  $$
- **Absolute Value Inequality:**
  $$
  \left| \int_{a}^{b} f(x) \, dx \right| \leq \int_{a}^{b} |f(x)| \, dx
  $$

### 6.4 The Fundamental Theorem of Calculus

This theorem links differentiation and integration.

**Part 1:**  
If $f$ is Riemann integrable on $[a, b]$ and we define

$$
F(x) = \int_{a}^{x} f(t) \, dt
$$

then $F$ is continuous on $[a, b]$, and if $f$ is continuous at $x_0 \in [a, b]$, then $F$ is differentiable at $x_0$ and $F'(x_0) = f(x_0)$.

**Part 2:**  
If $F$ is differentiable on $[a, b]$ with $F' = f$ and $f$ is continuous, then

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$

### 6.5 Improper Integrals

If $f$ is defined on $[a, \infty)$ or has an infinite discontinuity at $b$, the **improper integral** is defined as a limit:

$$
\int_{a}^{\infty} f(x)\, dx = \lim_{b \to \infty} \int_{a}^{b} f(x)\, dx
$$

If $f$ has a singularity at $c \in [a, b]$:

$$
\int_{a}^{b} f(x)\, dx = \lim_{\epsilon \to 0^+} \left( \int_{a}^{c-\epsilon} f(x)\, dx + \int_{c+\epsilon}^{b} f(x)\, dx \right)
$$

### 6.6 Integration Techniques (Substitution, Integration by Parts)

- **Substitution Rule:**  
  If $u = g(x)$, $g$ differentiable, then

  $$
  \int_{a}^{b} f(g(x))g'(x)\, dx = \int_{g(a)}^{g(b)} f(u)\, du
  $$

- **Integration by Parts:**  
  If $u(x)$ and $v(x)$ are differentiable,

  $$
  \int_{a}^{b} u(x)v'(x)\, dx = [u(x)v(x)]_{a}^{b} - \int_{a}^{b} u'(x)v(x)\, dx
  $$

### 6.7 Functions Defined by Integrals

Functions can be defined as integrals with variable upper limit, such as

$$
F(x) = \int_{a}^{x} f(t)\, dt
$$

This is called the **integral function** associated with $f$.

#### Exercises

1. Prove that every continuous function on $[a, b]$ is Riemann integrable.
2. Compute $\int_{0}^{1} x^2 \, dx$.
3. Evaluate $\int_{1}^{\infty} \frac{1}{x^2} \, dx$ as an improper integral.
4. Use integration by parts to compute $\int_{0}^{1} x e^{x} \, dx$.
5. Show that the function $f(x) = \chi_{\mathbb{Q} \cap [0,1]}(x)$ (the characteristic function of the rationals in $[0,1]$) is not Riemann integrable.

## Chapter 7: Sequences and Series of Functions

### 7.1 Pointwise and Uniform Convergence

Let $(f_n)$ be a sequence of functions $f_n: D \to \mathbb{R}$. We say that $(f_n)$ **converges pointwise** to a function $f: D \to \mathbb{R}$ if for every $x \in D$,

$$
\lim_{n \to \infty} f_n(x) = f(x)
$$

That is, for each $x$, the sequence of numbers $f_n(x)$ converges to $f(x)$.

$(f_n)$ **converges uniformly** to $f$ on $D$ if for every $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that

$$
|f_n(x) - f(x)| < \epsilon \quad \text{for all } x \in D \text{ and all } n \geq N
$$

Uniform convergence means that all the functions $f_n$ get close to $f$ "at the same rate" across the entire domain.

### 7.2 Weierstrass M-Test

The **Weierstrass M-Test** provides a criterion for uniform convergence of series of functions.

Let $f_n: D \to \mathbb{R}$, and suppose there exist constants $M_n \geq 0$ such that

$$
|f_n(x)| \leq M_n \quad \text{for all } x \in D
$$

If

$$
\sum_{n=1}^{\infty} M_n < \infty
$$

then the series

$$
\sum_{n=1}^{\infty} f_n(x)
$$

converges uniformly and absolutely on $D$.

### 7.3 Continuity of the Limit Function

If each $f_n$ is continuous on $D$ and $(f_n)$ converges uniformly to $f$ on $D$, then $f$ is continuous on $D$.

This is not generally true for pointwise convergence.

### 7.4 Differentiation and Integration of Series

**Termwise Limit Theorems:**

- **Integration:**  
  If $f_n$ are continuous on $[a, b]$ and $(f_n)$ converges uniformly to $f$ on $[a, b]$, then

  $$
  \lim_{n \to \infty} \int_{a}^{b} f_n(x)\, dx = \int_{a}^{b} f(x)\, dx
  $$

- **Differentiation:**  
  If $f_n$ are differentiable on $[a, b]$, $f_n \to f$ pointwise, and $(f_n')$ converges uniformly to $g$ on $[a, b]$, then $f$ is differentiable and $f' = g$.

### 7.5 Power Series and Radius of Convergence

A **power series** centered at $a \in \mathbb{R}$ is

$$
\sum_{n=0}^{\infty} c_n (x - a)^n
$$

where $(c_n)$ is a sequence of real numbers.

The **radius of convergence** $R$ is given by the formula

$$
\frac{1}{R} = \limsup_{n \to \infty} |c_n|^{1/n}
$$

(pronounced "limit superior as $n$ goes to infinity of the $n$th root of the absolute value of $c_n$").

- The series converges absolutely for $|x - a| < R$.

### 7.6 Taylor and Fourier Series

- **Taylor Series:**  
  If $f$ is infinitely differentiable at $a$,

  $$
  f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n
  $$

  for $x$ in a neighborhood of $a$.

- **Fourier Series:**  
  For a function $f$ defined on $[-\pi, \pi]$ (and extended periodically), the Fourier series is

  $$
  \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
  $$

  where

  $$
  a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx)\, dx, \quad b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx)\, dx
  $$

#### Exercises

1. Give an example of a sequence of functions that converges pointwise but not uniformly.
2. Prove that the sum of a uniformly convergent sequence of continuous functions is continuous.
3. Find the radius of convergence of the power series $\sum_{n=1}^{\infty} \frac{x^n}{n}$.
4. Show that the sequence $f_n(x) = x^n$ converges pointwise on $[0, 1]$, and determine whether this convergence is uniform.

## Chapter 8: Metric Spaces

### 8.1 Definition and Examples of Metric Spaces

A **metric space** is a set $X$ together with a function $d: X \times X \to \mathbb{R}$, called a **metric** or **distance function**, such that for all $x, y, z \in X$:

1. **Non-negativity:** $d(x, y) \geq 0$.
2. **Identity of indiscernibles:** $d(x, y) = 0$ if and only if $x = y$.
3. **Symmetry:** $d(x, y) = d(y, x)$.
4. **Triangle Inequality:** $d(x, z) \leq d(x, y) + d(y, z)$.

**Examples:**

- The real numbers $\mathbb{R}$ with $d(x, y) = |x - y|$.
- Euclidean space $\mathbb{R}^n$ with $d(\mathbf{x}, \mathbf{y}) = \sqrt{(x_1 - y_1)^2 + \cdots + (x_n - y_n)^2}$.
- The set of continuous functions on $[a, b]$ with $d(f, g) = \sup_{x \in [a, b]} |f(x) - g(x)|$.

### 8.2 Open and Closed Sets in Metric Spaces

Let $(X, d)$ be a metric space.

- An **open ball** centered at $x_0 \in X$ with radius $r > 0$ is the set
  $$
  B(x_0, r) = \{ x \in X : d(x, x_0) < r \}
  $$
- A set $U \subseteq X$ is **open** if for every $x \in U$, there exists $r > 0$ such that $B(x, r) \subseteq U$.
- A set $F \subseteq X$ is **closed** if its complement $X \setminus F$ is open.

### 8.3 Convergence and Continuity in Metric Spaces

A sequence $(x_n)$ in $X$ **converges** to $x \in X$ if

$$
\lim_{n \to \infty} d(x_n, x) = 0
$$

A function $f: X \to Y$ between two metric spaces $(X, d_X)$ and $(Y, d_Y)$ is **continuous at $x_0 \in X$** if for every $\epsilon > 0$, there exists $\delta > 0$ such that

$$
d_X(x, x_0) < \delta \implies d_Y(f(x), f(x_0)) < \epsilon
$$

### 8.4 Completeness and Completion of Metric Spaces

A metric space $(X, d)$ is **complete** if every Cauchy sequence in $X$ converges to a point in $X$.

A **Cauchy sequence** $(x_n)$ in $X$ satisfies: for every $\epsilon > 0$, there exists $N$ such that for all $m, n \geq N$,

$$
d(x_n, x_m) < \epsilon
$$

**Completion:** Every metric space can be "enlarged" to a complete metric space containing it as a dense subset (its completion).

### 8.5 Compactness and Sequential Compactness

A subset $K \subseteq X$ is **compact** if every open cover of $K$ has a finite subcover.

A metric space is **sequentially compact** if every sequence in $K$ has a convergent subsequence whose limit is in $K$.

In metric spaces, compactness and sequential compactness are equivalent.

### 8.6 Connectedness in Metric Spaces

A metric space $X$ is **connected** if it cannot be written as the union of two non-empty, disjoint open sets.

In $\mathbb{R}$, connected subsets are intervals, but in general metric spaces, connectedness can be more subtle.

### 8.7 The Baire Category Theorem

**Baire Category Theorem:**  
In any complete metric space, the intersection of countably many dense open sets is dense.

This theorem has important consequences in analysis, especially in understanding the structure of function spaces.

#### Exercises

1. Show that the set of rational numbers $\mathbb{Q}$ with the usual metric is not complete.
2. Prove that any closed subset of a complete metric space is complete.
3. Give an example of a compact set in $\mathbb{R}^n$.
4. Show that in $\mathbb{R}$, every compact set is closed and bounded.
5. Verify that the space of continuous functions on $[0, 1]$ with the metric $d(f, g) = \sup_{x \in [0,1]} |f(x) - g(x)|$ is complete.

## Chapter 9: Functions of Several Variables

### 9.1 Euclidean Spaces $\mathbb{R}^n$

The set $\mathbb{R}^n$ (pronounced "R n") is the set of all $n$-tuples of real numbers:

$$
\mathbb{R}^n = \{ (x_1, x_2, \ldots, x_n) : x_i \in \mathbb{R} \ \text{for} \ i = 1, \ldots, n \}
$$

The **Euclidean norm** of $x = (x_1, \ldots, x_n)$ is

$$
\|x\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}
$$

The **Euclidean distance** between $x$ and $y$ is

$$
d(x, y) = \|x - y\| = \sqrt{(x_1 - y_1)^2 + \cdots + (x_n - y_n)^2}
$$

### 9.2 Limits and Continuity in $\mathbb{R}^n$

Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}^m$.

- The **limit** of $f(x)$ as $x \to a$ is $L$ if for every $\epsilon > 0$, there exists $\delta > 0$ such that

  $$
  \|x - a\| < \delta \implies \|f(x) - L\| < \epsilon
  $$

- $f$ is **continuous at $a$** if

  $$
  \lim_{x \to a} f(x) = f(a)
  $$

### 9.3 Partial Derivatives and Differentiability

Let $f: \mathbb{R}^n \to \mathbb{R}$.

The **partial derivative** of $f$ with respect to $x_i$ at $a$ is

$$
\frac{\partial f}{\partial x_i}(a) = \lim_{h \to 0} \frac{f(a_1, \ldots, a_i + h, \ldots, a_n) - f(a_1, \ldots, a_n)}{h}
$$

$f$ is **differentiable** at $a$ if there exists a linear map $L: \mathbb{R}^n \to \mathbb{R}$ such that

$$
\lim_{h \to 0} \frac{|f(a + h) - f(a) - L(h)|}{\|h\|} = 0
$$

### 9.4 The Gradient, Jacobian, and Hessian

- The **gradient** of $f: \mathbb{R}^n \to \mathbb{R}$ at $a$, denoted $\nabla f(a)$ (pronounced "del f at a"), is the vector of partial derivatives:

  $$
  \nabla f(a) = \left( \frac{\partial f}{\partial x_1}(a), \ldots, \frac{\partial f}{\partial x_n}(a) \right)
  $$

- The **Jacobian matrix** of $f: \mathbb{R}^n \to \mathbb{R}^m$ at $a$ is the $m \times n$ matrix of all first-order partial derivatives:

  $$
  J_f(a) = \left[ \frac{\partial f_i}{\partial x_j}(a) \right]_{i=1,\ldots,m; j=1,\ldots,n}
  $$

- The **Hessian matrix** of $f: \mathbb{R}^n \to \mathbb{R}$ at $a$ is the $n \times n$ matrix:

  $$
  H_f(a) = \left[ \frac{\partial^2 f}{\partial x_i \partial x_j}(a) \right]_{i,j=1}^{n}
  $$

### 9.5 The Chain Rule in Several Variables

Suppose $f: \mathbb{R}^n \to \mathbb{R}^m$ and $g: \mathbb{R}^k \to \mathbb{R}^n$ are differentiable. The **chain rule** states:

$$
D(f \circ g)(a) = Df(g(a)) \cdot Dg(a)
$$

where $Df$ and $Dg$ are the Jacobian matrices of $f$ and $g$.

### 9.6 The Inverse and Implicit Function Theorems

**Inverse Function Theorem:**  
If $f: \mathbb{R}^n \to \mathbb{R}^n$ is continuously differentiable near $a$ and the Jacobian determinant $\det Df(a) \neq 0$, then $f$ is invertible near $a$, and the inverse is continuously differentiable.

**Implicit Function Theorem:**  
Let $F: \mathbb{R}^{n+m} \to \mathbb{R}^m$ be continuously differentiable. If $F(a, b) = 0$ and the $m \times m$ matrix $\frac{\partial F}{\partial y}(a, b)$ is invertible, then there exists a differentiable function $y = f(x)$ near $a$ such that $F(x, f(x)) = 0$.

### 9.7 Extrema of Multivariable Functions (Lagrange Multipliers)

To find local extrema of $f: \mathbb{R}^n \to \mathbb{R}$ subject to a constraint $g(x) = 0$, set up the equations:

$$
\nabla f(x) = \lambda \nabla g(x)
$$

where $\lambda$ (pronounced "lambda") is the **Lagrange multiplier**.

### 9.8 Manifolds and Level Sets

A **level set** of $f: \mathbb{R}^n \to \mathbb{R}$ is the set $\{ x \in \mathbb{R}^n : f(x) = c \}$ for some $c \in \mathbb{R}$.

A **manifold** (informally) is a set that locally resembles $\mathbb{R}^k$ for some $k$.

#### Exercises

1. Compute the gradient and Hessian of $f(x, y) = x^2 + y^2$.
2. Find the critical points and classify the extrema of $f(x, y) = x^2 - y^2$.
3. Use Lagrange multipliers to find the extrema of $f(x, y) = x y$ subject to $x^2 + y^2 = 1$.
4. State and explain the chain rule for $f: \mathbb{R}^2 \to \mathbb{R}$ and $g: \mathbb{R} \to \mathbb{R}^2$.
5. Give an example of a level set in $\mathbb{R}^2$ and sketch it.

## Chapter 10: Lebesgue Measure and Integration (Introduction)

### 10.1 Sigma-Algebras and Measurable Sets

A **$\sigma$-algebra** (pronounced "sigma algebra") $\mathcal{F}$ on a set $X$ is a collection of subsets of $X$ satisfying:

- $X \in \mathcal{F}$
- If $A \in \mathcal{F}$, then $X \setminus A \in \mathcal{F}$ (closed under complements)
- If $A_1, A_2, \ldots \in \mathcal{F}$, then $\bigcup_{n=1}^{\infty} A_n \in \mathcal{F}$ (closed under countable unions)

A set $E \subseteq \mathbb{R}$ is **Lebesgue measurable** if it belongs to the $\sigma$-algebra generated by the open subsets of $\mathbb{R}$.

### 10.2 The Lebesgue Measure on $\mathbb{R}$

The **Lebesgue measure** $m(E)$ of a set $E \subseteq \mathbb{R}$ generalizes the idea of "length" to more complicated sets.

- For intervals, $m((a, b)) = b - a$
- The measure is countably additive: if $E = \bigcup_{n=1}^{\infty} E_n$ with $E_n$ disjoint and measurable, then

  $$
  m(E) = \sum_{n=1}^{\infty} m(E_n)
  $$

- There exist sets of Lebesgue measure zero (e.g., the Cantor set).

### 10.3 Measurable Functions

A function $f: \mathbb{R} \to \overline{\mathbb{R}}$ is **measurable** if for every $\alpha \in \mathbb{R}$, the set $\{ x \in \mathbb{R} : f(x) > \alpha \}$ is measurable.

- Measurable functions are the natural analogs of continuous functions in the context of measure theory.

### 10.4 The Lebesgue Integral

Let $f: [a, b] \to \mathbb{R}$ be measurable and non-negative. The **Lebesgue integral** of $f$ over $[a, b]$ is defined by approximating $f$ by simple functions (functions taking only finitely many values) and taking the supremum of their integrals.

For general (possibly negative) $f$, write $f = f^+ - f^-$, where $f^+ = \max\{f, 0\}$ and $f^- = \max\{-f, 0\}$.

If both $\int f^+\, dm$ and $\int f^-\, dm$ are finite, then $f$ is **Lebesgue integrable** and

$$
\int_{a}^{b} f\, dm = \int_{a}^{b} f^+\, dm - \int_{a}^{b} f^-\, dm
$$

- $dm$ denotes integration with respect to Lebesgue measure.

### 10.5 Comparison with the Riemann Integral

- Every Riemann integrable function is Lebesgue integrable, and the values of the integrals agree.
- There are Lebesgue integrable functions that are not Riemann integrable (e.g., the characteristic function of the rationals in $[0,1]$).

Lebesgue integration is better suited for handling limits and irregular sets.

### 10.6 Convergence Theorems (Monotone, Dominated)

- **Monotone Convergence Theorem:**  
  If $(f_n)$ is a sequence of non-negative measurable functions with $f_n \uparrow f$ (i.e., $f_n(x) \leq f_{n+1}(x)$ for all $x$ and $n$), then

  $$
  \lim_{n \to \infty} \int f_n\, dm = \int f\, dm
  $$

- **Dominated Convergence Theorem:**  
  If $(f_n)$ is a sequence of measurable functions converging pointwise to $f$, and there exists an integrable function $g$ such that $|f_n(x)| \leq g(x)$ for all $x$ and $n$, then

  $$
  \lim_{n \to \infty} \int f_n\, dm = \int f\, dm
  $$

These theorems allow the interchange of limits and integration under certain conditions.

### 10.7 Applications and Examples

- The Lebesgue integral can integrate functions with infinitely many discontinuities.
- Probability: the Lebesgue integral generalizes the concept of expectation.
- Fourier analysis: convergence of functions in $L^1$ and $L^2$ spaces.

#### Exercises

1. Show that the characteristic function of the rationals in $[0, 1]$ is measurable and has Lebesgue measure zero.
2. Give an example of a function that is Lebesgue integrable but not Riemann integrable.
3. State and prove the Monotone Convergence Theorem for non-negative functions.
4. Let $f_n(x) = x^n$ on $[0, 1]$. Compute $\lim_{n \to \infty} \int_{0}^{1} f_n(x)\, dx$ and compare with $\int_{0}^{1} \lim_{n \to \infty} f_n(x)\, dx$.
5. Prove that the Cantor set has measure zero.

## Chapter 11: Further Topics in Real Analysis

### 11.1 Differentiation and Integration Under the Integral Sign

**Leibniz’s Rule (Differentiation Under the Integral Sign):**  
Suppose $f(x, t)$ is continuous for $a \leq x \leq b$ and $t$ in an open interval $I$, and $\frac{\partial f}{\partial t}$ exists and is continuous. Then

$$
\frac{d}{dt} \int_{a}^{b} f(x, t)\, dx = \int_{a}^{b} \frac{\partial f}{\partial t}(x, t)\, dx
$$

This powerful technique is useful for parameter-dependent integrals.

### 11.2 Functions of Bounded Variation

A function $f: [a, b] \to \mathbb{R}$ is of **bounded variation** if

$$
V_a^b(f) = \sup_P \sum_{i=1}^{n} |f(x_i) - f(x_{i-1})| < \infty
$$

where the supremum is over all partitions $P: a = x_0 < x_1 < \cdots < x_n = b$.

- Functions of bounded variation can be written as the difference of two increasing functions.

### 11.3 The Riesz Representation Theorem (for $\mathbb{R}$)

For certain spaces of functions, every continuous linear functional can be represented as integration against a measure.

**Riesz Representation Theorem (for $C([a, b])$):**  
If $L$ is a continuous linear functional on the space of continuous functions $C([a, b])$, then there exists a function $\alpha$ of bounded variation such that

$$
L(f) = \int_{a}^{b} f(x)\, d\alpha(x)
$$

for all $f \in C([a, b])$.

### 11.4 Introduction to Functional Analysis

**Functional analysis** studies vector spaces of functions and linear operators acting on them, often equipped with a norm or inner product.

- **Normed vector spaces**, **Banach spaces** (complete normed spaces), and **Hilbert spaces** (complete inner product spaces) are central concepts.
- Examples include $L^p$ spaces, the space of continuous functions, and sequence spaces.

### 11.5 The Arzelà–Ascoli Theorem

The **Arzelà–Ascoli Theorem** gives criteria for precompactness (relatively compact subsets) in the space $C([a, b])$ of continuous functions.

**Theorem:**  
A set $\mathcal{F} \subseteq C([a, b])$ is relatively compact if and only if it is **equicontinuous** and **uniformly bounded**.

- **Equicontinuous:** For every $\epsilon > 0$, there exists $\delta > 0$ such that for all $f \in \mathcal{F}$ and $|x - y| < \delta$, $|f(x) - f(y)| < \epsilon$.
- **Uniformly bounded:** There exists $M > 0$ such that $|f(x)| \leq M$ for all $f \in \mathcal{F}$ and $x \in [a, b]$.

### 11.6 The Stone–Weierstrass Theorem

The **Stone–Weierstrass Theorem** generalizes the Weierstrass approximation theorem.

**Theorem:**  
Let $A$ be a subalgebra of $C([a, b])$ that contains the constant functions and separates points of $[a, b]$. Then $A$ is dense in $C([a, b])$ with respect to the uniform norm; that is, any continuous function can be uniformly approximated by elements of $A$.

#### Exercises

1. Use differentiation under the integral sign to evaluate $\int_{0}^{\infty} \frac{e^{-t}}{t + x}\, dt$ as a function of $x > 0$.
2. Show that every monotone function on $[a, b]$ is of bounded variation.
3. State and prove a version of the Arzelà–Ascoli Theorem for sequences of functions.
4. Give an example of a sequence of polynomials that converges uniformly to a continuous function on $[0, 1]$.
5. Explain why the set of polynomials is dense in $C([a, b])$ by the Stone–Weierstrass Theorem.

# Part 2: Complex Analysis

## Chapter 12: The Complex Number System

### 12.1 The Field of Complex Numbers $\mathbb{C}$

The set of **complex numbers** is denoted by $\mathbb{C}$ (pronounced "C, the set of complex numbers") and consists of all numbers of the form

$$
z = x + i y
$$

where $x, y \in \mathbb{R}$ and $i$ (pronounced "i") is the **imaginary unit** defined by

$$
i^2 = -1
$$

- $x$ is called the **real part** of $z$, denoted $\operatorname{Re}(z)$.
- $y$ is called the **imaginary part** of $z$, denoted $\operatorname{Im}(z)$.

**Basic Operations:**

- **Addition:** $(x_1 + i y_1) + (x_2 + i y_2) = (x_1 + x_2) + i (y_1 + y_2)$
- **Multiplication:** $(x_1 + i y_1)(x_2 + i y_2) = (x_1 x_2 - y_1 y_2) + i (x_1 y_2 + x_2 y_1)$
- **Conjugate:** For $z = x + i y$, the **complex conjugate** is $\overline{z} = x - i y$.
- **Modulus:** $|z| = \sqrt{x^2 + y^2}$

### 12.2 Algebraic and Geometric Representations

- **Algebraic (Cartesian) form:** $z = x + i y$
- **Geometric (Argand diagram):** Represents $z$ as a point $(x, y)$ in the plane.

The **modulus** $|z|$ is the distance from the origin to $(x, y)$.

The **argument** $\arg(z)$ (pronounced "arg z") is the angle $\theta$ between the positive real axis and the line joining the origin to $z$, measured in radians.

### 12.3 The Complex Plane and Polar Form

Every nonzero complex number $z$ can be written in **polar form**:

$$
z = r (\cos \theta + i \sin \theta)
$$

where $r = |z|$ is the modulus and $\theta = \arg(z)$.

Using **Euler’s formula** (Leonhard Euler, pronounced "oiler"):

$$
e^{i\theta} = \cos \theta + i \sin \theta
$$

so

$$
z = r e^{i\theta}
$$

### 12.4 Roots of Complex Numbers and the Fundamental Theorem of Algebra

**Roots:**

The $n$-th roots of $z = r e^{i\theta}$ are given by

$$
z_k = r^{1/n} e^{i \left(\frac{\theta + 2\pi k}{n}\right)},\quad k = 0, 1, \ldots, n-1
$$

- $r^{1/n}$ is the real $n$-th root of $r$.
- $2\pi$ (pronounced "two pi") is a full turn in radians.

**Fundamental Theorem of Algebra:**

Every non-constant polynomial $p(z)$ with complex coefficients has at least one root in $\mathbb{C}$, and in fact, exactly as many roots as its degree (counting multiplicities).

#### Exercises

1. Express $z = -1 + i$ in polar form.
2. Find all cube roots of $8$ in $\mathbb{C}$.
3. Prove that $|z_1 z_2| = |z_1| |z_2|$ and $\arg(z_1 z_2) = \arg(z_1) + \arg(z_2)$ (modulo $2\pi$).
4. Show that the equation $z^4 + 1 = 0$ has four distinct roots in $\mathbb{C}$ and find them.
5. State and explain Euler’s formula for complex exponentials.

## Chapter 13: Topology of the Complex Plane

### 13.1 Open, Closed, and Connected Sets in $\mathbb{C}$

The **complex plane** is the set $\mathbb{C}$, identified with the Cartesian plane $\mathbb{R}^2$.

- An **open ball** centered at $z_0 \in \mathbb{C}$ with radius $r > 0$ is
  $$
  B(z_0, r) = \{ z \in \mathbb{C} : |z - z_0| < r \}
  $$
- A set $U \subseteq \mathbb{C}$ is **open** if for every $z_0 \in U$, there exists $r > 0$ such that $B(z_0, r) \subseteq U$.
- A set $F \subseteq \mathbb{C}$ is **closed** if its complement $\mathbb{C} \setminus F$ is open.

A set $A \subseteq \mathbb{C}$ is **connected** if it cannot be written as the union of two non-empty, disjoint open subsets of $A$.

A **domain** is a non-empty open and connected subset of $\mathbb{C}$.

### 13.2 Sequences and Limits in $\mathbb{C}$

A sequence $(z_n)$ of complex numbers **converges** to $z \in \mathbb{C}$ if

$$
\lim_{n \to \infty} |z_n - z| = 0
$$

The usual $\epsilon$-$N$ definition applies: for every $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that $|z_n - z| < \epsilon$ for all $n \geq N$.

### 13.3 Compactness in $\mathbb{C}$

A set $K \subseteq \mathbb{C}$ is **compact** if every open cover of $K$ has a finite subcover.

**Heine–Borel Theorem (Complex Version):**  
A set $K \subseteq \mathbb{C}$ is compact if and only if it is closed and bounded.

### 13.4 Regions and Domains

- A **region** is a non-empty open, connected subset of $\mathbb{C}$ (sometimes also required to be simply connected).
- A **simply connected** domain is an open connected set with no "holes"; formally, any closed curve in the domain can be continuously contracted to a point without leaving the domain.

#### Exercises

1. Give an example of a set in $\mathbb{C}$ that is open but not closed, and one that is closed but not open.
2. Prove that the closed disk $\{ z \in \mathbb{C} : |z| \leq 1 \}$ is compact.
3. Determine whether the set $\{ z \in \mathbb{C} : 0 < |z| < 1 \}$ is connected, open, closed, or compact.
4. Explain why every finite set in $\mathbb{C}$ is closed and bounded, but not open.
5. Provide an example of a simply connected region in $\mathbb{C}$ and one that is not simply connected.

## Chapter 14: Complex Functions and Limits

### 14.1 Functions of a Complex Variable

A **complex function** is a rule $f: D \to \mathbb{C}$, where $D \subseteq \mathbb{C}$. For each $z \in D$, $f(z)$ is a complex number.

- We can write $z = x + i y$ and $f(z) = u(x, y) + i v(x, y)$, where $u$ and $v$ are real-valued functions representing the real and imaginary parts of $f$.

### 14.2 Limits and Continuity

Let $f: D \to \mathbb{C}$ and $z_0 \in D$ be a limit point.

We say

$$
\lim_{z \to z_0} f(z) = w
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
|z - z_0| < \delta \implies |f(z) - w| < \epsilon
$$

A function $f$ is **continuous at $z_0$** if

$$
\lim_{z \to z_0} f(z) = f(z_0)
$$

### 14.3 Differentiability and the Cauchy–Riemann Equations

A function $f: D \to \mathbb{C}$ is **differentiable** at $z_0$ if the following limit exists:

$$
f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}
$$

If $f$ is differentiable at every point in $D$, $f$ is said to be **holomorphic** or **analytic** on $D$.

**Cauchy–Riemann Equations:**  
If $f(z) = u(x, y) + i v(x, y)$ is differentiable at $z_0 = x_0 + i y_0$, then $u$ and $v$ have first partial derivatives at $(x_0, y_0)$ and

$$
\frac{\partial u}{\partial x}(x_0, y_0) = \frac{\partial v}{\partial y}(x_0, y_0)
$$

$$
\frac{\partial u}{\partial y}(x_0, y_0) = -\frac{\partial v}{\partial x}(x_0, y_0)
$$

These are necessary (and under mild conditions, sufficient) for $f$ to be complex differentiable at $z_0$.

### 14.4 Analytic Functions

A function $f$ is **analytic** at $z_0$ if it is differentiable in some neighborhood of $z_0$. Analyticity is a much stronger property in complex analysis than in real analysis:

- If $f$ is analytic on an open set, it is infinitely differentiable there.
- $f$ has a convergent power series expansion around every point of analyticity.

#### Exercises

1. Express $f(z) = z^2$ in terms of real and imaginary parts, and verify the Cauchy–Riemann equations.
2. Show that the function $f(z) = \overline{z}$ is not differentiable anywhere except possibly at one point.
3. Prove that if $f$ is analytic, then $f$ is infinitely differentiable.
4. Give an example of a function that is continuous everywhere but nowhere differentiable (as a real function), and compare with the situation for complex analytic functions.
5. Determine where $f(z) = |z|^2$ is differentiable as a function of a complex variable.

## Chapter 15: Elementary Functions

### 15.1 The Exponential Function

The complex exponential function is defined by the power series

$$
e^z = \sum_{n=0}^{\infty} \frac{z^n}{n!}
$$

for all $z \in \mathbb{C}$.

**Key properties:**

- $e^{z + w} = e^z e^w$ for all $z, w \in \mathbb{C}$
- $e^0 = 1$
- $e^{i\theta} = \cos \theta + i \sin \theta$ (Euler’s formula)

### 15.2 The Logarithm and Branches

The **complex logarithm** is the inverse of the exponential function.

For $z = r e^{i\theta}$ (with $r > 0$ and $\theta \in \mathbb{R}$):

$$
\log z = \ln r + i \theta
$$

Since $\theta$ is determined only up to multiples of $2\pi$, the logarithm is **multi-valued**. The **principal value** is defined by restricting $\theta$ to $(-\pi, \pi]$:

$$
\text{Log}\ z = \ln r + i \arg(z)
$$

where $\arg(z)$ denotes the principal argument.

- The logarithm is analytic except on the branch cut (typically the negative real axis and $0$).

### 15.3 Complex Powers and Roots

For $z \neq 0$ and $w \in \mathbb{C}$,

$$
z^w = e^{w \log z}
$$

This is multi-valued because $\log z$ is multi-valued. To define a single-valued branch, restrict $\log z$.

**Roots:**  
The $n$-th roots of $z$ are the values $w$ such that $w^n = z$:

$$
w_k = r^{1/n} e^{i\left( \frac{\theta + 2\pi k}{n} \right)},\quad k = 0, 1, \ldots, n-1
$$

### 15.4 Trigonometric and Hyperbolic Functions

**Trigonometric functions:**

- $\sin z = \frac{e^{iz} - e^{-iz}}{2i}$
- $\cos z = \frac{e^{iz} + e^{-iz}}{2}$

These are entire functions (analytic everywhere on $\mathbb{C}$).

**Hyperbolic functions:**

- $\sinh z = \frac{e^{z} - e^{-z}}{2}$
- $\cosh z = \frac{e^{z} + e^{-z}}{2}$

**Relations:**

- $\cos^2 z + \sin^2 z = 1$
- $\cosh^2 z - \sinh^2 z = 1$

#### Exercises

1. Show that $e^{z}$ is entire (analytic on all of $\mathbb{C}$).
2. Compute all values of $\log(-1)$ in $\mathbb{C}$.
3. Find all solutions $z$ to $z^3 = 1$ and plot them in the complex plane.
4. Show that $\sin(z)$ and $\cos(z)$ are periodic with period $2\pi$ in the complex plane.
5. Express $\sin(z)$ in terms of real and imaginary parts using $z = x + i y$.

## Chapter 16: Complex Integration

### 16.1 Contours and Paths in the Complex Plane

A **contour** (or **path**) in $\mathbb{C}$ is a continuous, piecewise smooth map $\gamma: [a, b] \to \mathbb{C}$.

- The image $\gamma([a, b])$ is called the **trace** of the contour.
- The path is **simple** if it does not cross itself (except possibly at endpoints).

**Examples:**
- A straight line from $z_0$ to $z_1$: $\gamma(t) = (1-t)z_0 + t z_1$, $t \in [0,1]$.
- A circle centered at $z_0$ of radius $r$: $\gamma(t) = z_0 + r e^{it}$, $t \in [0, 2\pi]$.

### 16.2 Complex Line Integrals

Given $f: D \to \mathbb{C}$ and a contour $\gamma: [a, b] \to D$, the **complex line integral** is

$$
\int_{\gamma} f(z)\, dz = \int_{a}^{b} f(\gamma(t)) \gamma'(t)\, dt
$$

This generalizes the idea of integration along a curve in the plane.

**Properties:**
- Linearity: $\int_{\gamma} (a f + b g)\, dz = a \int_{\gamma} f\, dz + b \int_{\gamma} g\, dz$
- Reversal of path: $\int_{-\gamma} f(z)\, dz = -\int_{\gamma} f(z)\, dz$

### 16.3 Cauchy–Goursat Theorem

**Cauchy–Goursat Theorem:**  
If $f$ is analytic inside and on a simple closed contour $C$, then

$$
\int_{C} f(z)\, dz = 0
$$

This is a central result of complex analysis: the integral of a holomorphic function over a closed curve in a domain where it is analytic is zero.

### 16.4 Cauchy Integral Formula

**Theorem (Cauchy Integral Formula):**  
If $f$ is analytic in an open set containing a simple closed positively oriented contour $C$ and its interior, and $z_0$ is a point inside $C$, then

$$
f(z_0) = \frac{1}{2\pi i} \int_{C} \frac{f(z)}{z - z_0}\, dz
$$

This formula allows us to recover the value of an analytic function from its values on a contour.

### 16.5 Morera’s Theorem

**Morera’s Theorem:**  
If $f$ is continuous on an open set $D \subseteq \mathbb{C}$ and $\int_{C} f(z)\, dz = 0$ for every closed contour $C$ in $D$, then $f$ is analytic on $D$.

This provides a converse to the Cauchy–Goursat theorem.

#### Exercises

1. Evaluate $\int_{|z|=1} z^n dz$ for $n \in \mathbb{Z}$, where the contour is the unit circle oriented counterclockwise.
2. Show that $\int_{C} (z - z_0)^{-1} dz = 2\pi i$ if $C$ is a positively oriented simple closed contour enclosing $z_0$.
3. Use the Cauchy Integral Formula to compute $f^{(n)}(z_0)$ in terms of a contour integral.
4. State and prove the linearity of the complex line integral.
5. Give an example of a function which is continuous but not analytic, and show that Morera's theorem does not apply.

## Chapter 17: Series and Residues

### 17.1 Power Series and Analyticity

A **power series** centered at $z_0 \in \mathbb{C}$:

$$
\sum_{n=0}^{\infty} a_n (z - z_0)^n
$$

converges absolutely for $|z - z_0| < R$, where $R$ is the **radius of convergence**:

$$
R = \frac{1}{\limsup_{n \to \infty} |a_n|^{1/n}}
$$

Within $|z - z_0| < R$, the sum defines an analytic function; the power series can be differentiated and integrated term-by-term.

### 17.2 Taylor and Laurent Series

**Taylor Series:**  
If $f$ is analytic at $z_0$,

$$
f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n
$$

**Laurent Series:**  
If $f$ is analytic in an annulus $r < |z - z_0| < R$,

$$
f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n
$$

where the sum runs over all integers, and negative powers may be present.

### 17.3 Isolated Singularities

Let $f$ be analytic in $0 < |z - z_0| < R$.

- $z_0$ is a **removable singularity** if $f$ can be analytically extended to $z_0$.
- $z_0$ is a **pole of order $m$** if $(z - z_0)^m f(z)$ is analytic and nonzero at $z_0$.
- $z_0$ is an **essential singularity** if neither of the above holds.

### 17.4 The Residue Theorem

**Residue:** The coefficient $a_{-1}$ in the Laurent expansion of $f$ about $z_0$ is called the **residue** of $f$ at $z_0$:

$$
\operatorname{Res}(f, z_0) = a_{-1}
$$

**Residue Theorem:**  
Let $f$ be analytic in a domain except for isolated singularities $z_1, \ldots, z_n$ inside a simple closed curve $C$, then

$$
\int_{C} f(z)\, dz = 2\pi i \sum_{k=1}^{n} \operatorname{Res}(f, z_k)
$$

### 17.5 Calculation of Residues

**For a simple pole at $z_0$** ($f$ analytic except simple pole):

$$
\operatorname{Res}(f, z_0) = \lim_{z \to z_0} (z - z_0) f(z)
$$

**For a pole of order $m$ at $z_0$:**

$$
\operatorname{Res}(f, z_0) = \frac{1}{(m-1)!} \lim_{z \to z_0} \frac{d^{m-1}}{dz^{m-1}} \left[ (z - z_0)^m f(z) \right]
$$

### 17.6 Applications: Evaluation of Real Integrals

Using the residue theorem, certain real integrals can be evaluated by considering related complex integrals.

**Example:**

$$
\int_{-\infty}^{\infty} \frac{dx}{x^2 + 1} = \pi
$$

can be evaluated using a semicircular contour and the residue at $i$.

#### Exercises

1. Find the radius of convergence of $\sum_{n=0}^{\infty} z^{n!}$.
2. Expand $f(z) = \frac{1}{z(z-1)}$ in a Laurent series valid for $0 < |z| < 1$.
3. Classify the singularities of $f(z) = e^{1/z}$ at $z=0$.
4. Compute the residue of $f(z) = \frac{1}{(z-2)^3}$ at $z=2$.
5. Use the residue theorem to evaluate $\int_{-\infty}^{\infty} \frac{dx}{x^2 + a^2}$, $a > 0$.

## Chapter 18: Conformal Mappings

### 18.1 Definition and Geometric Meaning

A function $f: D \to \mathbb{C}$ is called **conformal** at a point $z_0 \in D$ if it is analytic at $z_0$ and $f'(z_0) \neq 0$.

- Conformal mappings **preserve angles** and the orientation of curves at points where $f'(z_0) \neq 0$.
- More generally, a conformal map is a **locally angle-preserving** transformation.

### 18.2 Mobius (Linear Fractional) Transformations

A **Mobius transformation** (or linear fractional transformation) is a function of the form

$$
f(z) = \frac{az + b}{cz + d}
$$

where $a, b, c, d \in \mathbb{C}$ and $ad - bc \neq 0$.

**Properties:**
- Mobius transformations map circles and lines to circles and lines (in the extended complex plane $\mathbb{C} \cup \{\infty\}$).
- They are conformal except at points where the denominator vanishes.

### 18.3 The Riemann Mapping Theorem

**Riemann Mapping Theorem:**  
Every non-empty simply connected open subset of $\mathbb{C}$ (other than $\mathbb{C}$ itself) can be mapped **conformally** onto the open unit disk $\mathbb{D} = \{ z : |z| < 1 \}$.

- The mapping is unique up to Mobius transformations preserving the disk.

### 18.4 Schwarz Lemma

Let $f: \mathbb{D} \to \mathbb{D}$ be analytic with $f(0) = 0$.

- Then $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$.
- Also, $|f'(0)| \leq 1$.
- If equality holds at any nonzero point, then $f(z) = e^{i\theta} z$ for some real $\theta$.

### 18.5 Applications to Boundary Value Problems

Conformal mappings are used to solve problems such as:
- Laplace’s equation in various domains
- Mapping complicated regions to simpler ones (e.g., the unit disk)

#### Exercises

1. Show that $f(z) = \frac{1}{z}$ is a Mobius transformation and describe its geometric action.
2. Find a Mobius transformation that maps the upper half-plane to the unit disk.
3. Prove that every non-constant analytic function is conformal where $f'(z) \neq 0$.
4. State and explain the Schwarz Lemma.
5. Explain why the whole complex plane cannot be conformally mapped onto the unit disk.

## Chapter 19: Harmonic and Analytic Functions

### 19.1 Harmonic Functions

A **harmonic function** is a twice continuously differentiable function $u: D \to \mathbb{R}$, $D \subseteq \mathbb{C}$, that satisfies **Laplace’s equation**:

$$
\Delta u = u_{xx} + u_{yy} = 0
$$

where $u_{xx}$ and $u_{yy}$ are the second partial derivatives with respect to $x$ and $y$.

- Harmonic functions describe steady-state heat flow, electrostatics, and fluid flow.

### 19.2 Relationship Between Harmonic and Analytic Functions

If $f = u + i v$ is analytic on $D$, then both $u$ and $v$ are harmonic on $D$.

- $u$ and $v$ are called **harmonic conjugates**.
- Conversely, if $u$ is harmonic and $D$ is simply connected, there exists $v$ so that $f = u + i v$ is analytic.

### 19.3 The Poisson Integral Formula

The **Poisson integral formula** provides the solution to the Dirichlet problem for the unit disk.

Suppose $u$ is harmonic in the unit disk and continuous on its closure, with boundary values $f(\theta)$ on $|z|=1$. Then for $z = r e^{i\phi}$, $0 \leq r < 1$,

$$
u(r e^{i\phi}) = \frac{1}{2\pi} \int_{0}^{2\pi} \frac{1 - r^2}{1 - 2r \cos(\theta - \phi) + r^2} f(\theta) d\theta
$$

### 19.4 The Maximum Principle

**Maximum Principle:**  
If $u$ is harmonic and achieves its maximum (or minimum) inside a domain, then $u$ is constant.

- Thus, maxima and minima of harmonic functions occur on the boundary.

### 19.5 The Mean Value Property

If $u$ is harmonic in a domain containing the closed disk $|z - z_0| \leq r$, then

$$
u(z_0) = \frac{1}{2\pi} \int_{0}^{2\pi} u(z_0 + r e^{i\theta}) d\theta
$$

That is, the value at the center equals the average on any circle about $z_0$ contained in the domain.

#### Exercises

1. Show that the real and imaginary parts of any analytic function are harmonic.
2. Find a harmonic conjugate for $u(x, y) = x^2 - y^2$.
3. State and prove the mean value property for harmonic functions.
4. Use the Poisson integral formula to solve the Dirichlet problem for the unit disk with boundary data $f(\theta) = \cos \theta$.
5. Give an example of a harmonic function on the unit disk which is not the real part of any analytic function on all of $\mathbb{C}$.

## Chapter 20: Analytic Continuation and Riemann Surfaces

### 20.1 Analytic Continuation

If two analytic functions $f$ and $g$ are defined on domains $D_1$ and $D_2$ with $D_1 \cap D_2 \neq \emptyset$, and $f = g$ on $D_1 \cap D_2$, then $f$ and $g$ are said to be **analytic continuations** of one another.

- **Analytic continuation** is a process of extending the domain of a given analytic function beyond its original region of definition.
- If the continuation is possible along every path without ambiguity, the function is called **single-valued**; otherwise, it may be **multi-valued**.

### 20.2 Uniqueness of Analytic Continuation

**Identity Theorem:**  
If two analytic functions agree on a set with an accumulation point in a domain, then they agree everywhere on the connected component containing that set.

- Analytic continuation is unique if it exists.

### 20.3 Natural Boundaries

A **natural boundary** is a boundary beyond which analytic continuation is not possible. For example, the function

$$
f(z) = \sum_{n=0}^{\infty} z^{2^n}
$$

is analytic in $|z| < 1$, but cannot be continued beyond $|z| = 1$.

### 20.4 Multi-Valued Functions and Branch Points

Some functions, like $\log z$ or $z^{1/n}$, are **multi-valued** because their value depends on the path taken around certain points.

- A **branch point** is a point where the function cannot be made single-valued by any branch cut in the plane.

### 20.5 Riemann Surfaces

A **Riemann surface** is a connected 1-dimensional complex manifold that allows multi-valued functions to become single-valued when considered as functions on the surface.

- For example, the Riemann surface of $\sqrt{z}$ is a two-sheeted cover of the complex plane, branched at $z=0$ and $z=\infty$.

#### Exercises

1. Give an explicit example of analytic continuation for the function $f(z) = \sum_{n=0}^{\infty} z^n$.
2. Show that $f(z) = \log z$ cannot be defined as a single-valued analytic function on all of $\mathbb{C} \setminus \{0\}$.
3. Describe the Riemann surface for $w = \sqrt{z}$.
4. What is the natural boundary of $f(z) = \sum_{n=0}^{\infty} z^{2^n}$? Explain.
5. State and prove the Identity Theorem for analytic functions.

## Chapter 21: Applications of Complex Analysis

### 21.1 Evaluation of Real Integrals via Contour Integration

Complex analysis provides powerful techniques for evaluating real integrals. Many definite integrals that are difficult or impossible to compute with real methods can be evaluated using **contour integration** and the **residue theorem**.

**Example:**
Evaluate
$$
\int_{-\infty}^{\infty} \frac{\cos(ax)}{x^2 + b^2} dx, \quad a, b > 0
$$
using a contour in the upper half-plane and the residue theorem.

### 21.2 Infinite Series and Summation Formulas

Complex analytic methods can sum certain infinite series.

**Example:**
The sum
$$
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
$$
can be found using the residue theorem and properties of $\pi \cot \pi z$.

### 21.3 The Gamma and Zeta Functions

- **Gamma function:** $\Gamma(z) = \int_0^{\infty} t^{z-1} e^{-t} dt$ (analytic continuation of factorial)
- **Riemann zeta function:** $\zeta(s) = \sum_{n=1}^{\infty} n^{-s}$, analytic for $\operatorname{Re}(s) > 1$, can be analytically continued to most of $\mathbb{C}$ except $s=1$.

Both have deep connections to number theory, probability, and physics.

### 21.4 Applications to Physics and Engineering

Complex analysis is foundational in:
- **Electrostatics and Fluid Dynamics:** Solutions to Laplace’s and Poisson’s equations.
- **Signal Processing:** Fourier and Laplace transforms.
- **Quantum Mechanics:** Analytic properties of wave functions.
- **Conformal Mapping:** Used in aerodynamics, elasticity, and other fields.

### 21.5 Potential Theory and Fluid Flow

- **Potential theory** studies harmonic functions, describing gravitational, electrostatic, or fluid potentials.
- **Complex potentials** (analytic functions) describe two-dimensional incompressible, irrotational fluid flow.

#### Exercises

1. Use contour integration to compute $\int_{0}^{\infty} \frac{dx}{x^2 + 1}$.
2. Show how the sum $\sum_{n=1}^\infty \frac{1}{n^2}$ can be obtained using the residue theorem.
3. State the basic properties of the Gamma function and its relation to the factorial function.
4. Give an example of a conformal mapping used in solving a physics problem (e.g., mapping a slit domain to the unit disk).
5. Explain how analytic functions describe potential flows in two dimensions.

## Chapter 22: Further Topics in Complex Analysis

### 22.1 Normal Families and Montel’s Theorem

A **normal family** is a family $\mathcal{F}$ of analytic functions on a domain $D$ such that every sequence in $\mathcal{F}$ has a subsequence that converges uniformly on compact subsets of $D$ (the limit may be a function or identically $\infty$).

**Montel’s Theorem:**  
A family of analytic functions on a domain $D$ that is uniformly bounded on compact subsets of $D$ is a normal family.

- Normal families are fundamental in the study of value distribution and dynamics.

### 22.2 Picard’s Theorems

**Picard’s Little Theorem:**  
An entire (analytic on all of $\mathbb{C}$) non-constant function attains all complex values, with at most one exception.

**Picard’s Great Theorem:**  
If $f$ has an essential singularity at $z_0$, then in any neighborhood of $z_0$, $f$ takes on all possible complex values, with at most one exception, infinitely often.

### 22.3 The Argument Principle and Rouche’s Theorem

**Argument Principle:**  
Let $f$ be meromorphic inside and on a simple closed curve $C$ not passing through any zeros or poles of $f$. Then

$$
\frac{1}{2\pi i}\int_{C} \frac{f'(z)}{f(z)} dz = N - P
$$

where $N$ is the number of zeros and $P$ the number of poles inside $C$, counted with multiplicity.

**Rouche’s Theorem:**  
Let $f$ and $g$ be analytic inside and on a simple closed curve $C$, and suppose $|g(z)| < |f(z)|$ on $C$. Then $f$ and $f + g$ have the same number of zeros inside $C$.

### 22.4 Schwarz Reflection Principle

If $f$ is analytic in a domain $D$ and continuous up to a segment of the real axis, and $f$ is real-valued on that segment, then $f$ can be analytically continued across the segment by reflection:

$$
f(\overline{z}) = \overline{f(z)}
$$

for $z$ in $D$.

### 22.5 Introduction to Elliptic Functions

**Elliptic functions** are meromorphic functions that are doubly periodic (periodic in two directions in the complex plane).

- Examples: Weierstrass $\wp$-function, Jacobi elliptic functions.
- Elliptic functions are central in the theory of complex tori and have applications in number theory and physics.

#### Exercises

1. State and prove Montel’s Theorem for normal families.
2. Give an explicit example illustrating Picard’s Great Theorem.
3. Use Rouche’s Theorem to determine how many zeros $f(z) = z^5 + 2z + 1$ has inside $|z|=1$.
4. State and explain the Schwarz Reflection Principle.
5. Define an elliptic function and give an example of a non-constant elliptic function.

# Chapter 23: Appendices

## Appendix A: Notation and Symbols

| Symbol              | Meaning                                             |
|---------------------|-----------------------------------------------------|
| $\mathbb{R}$        | Real numbers                                        |
| $\mathbb{C}$        | Complex numbers                                     |
| $\mathbb{N}$        | Natural numbers                                     |
| $\mathbb{Z}$        | Integers                                            |
| $\mathbb{Q}$        | Rational numbers                                    |
| $z, w$              | Complex variables                                   |
| $i$                 | Imaginary unit, $i^2 = -1$                          |
| $|z|$               | Modulus (absolute value) of $z$                     |
| $\overline{z}$      | Complex conjugate of $z$                            |
| $\operatorname{Re}(z)$ | Real part of $z$                                 |
| $\operatorname{Im}(z)$ | Imaginary part of $z$                            |
| $\arg(z)$           | Argument (angle) of $z$                             |
| $\subseteq$         | Subset                                              |
| $\supseteq$         | Superset                                            |
| $\cap$              | Intersection                                        |
| $\cup$              | Union                                               |
| $\emptyset$         | Empty set                                           |
| $f: X \to Y$        | Function $f$ with domain $X$ and codomain $Y$       |
| $\lim$              | Limit                                               |
| $\sup$              | Supremum (least upper bound)                        |
| $\inf$              | Infimum (greatest lower bound)                      |
| $\int$              | Integral                                            |
| $\sum$              | Summation                                           |
| $\prod$             | Product                                             |
| $dx, dz$            | Differential with respect to $x$ or $z$             |
| $C([a,b])$          | Space of continuous functions on $[a,b]$            |
| $L^p, L^2$          | Spaces of $p$-integrable, square-integrable functions |
| $f'(z)$, $f^{(n)}(z)$ | Derivatives of $f$ at $z$                         |
| $\Delta u$          | Laplacian of $u$                                    |
| $\mathbb{D}$        | Open unit disk in $\mathbb{C}$, $\{z: |z| < 1\}$    |

## Appendix B: Logic and Set Theory Fundamentals

- **Implication ($\implies$):** $A \implies B$ means if $A$ is true, then $B$ is true.
- **Equivalence ($\iff$):** $A \iff B$ means $A$ is true if and only if $B$ is true.
- **Negation ($\neg$):** $\neg A$ means "not $A$".
- **For all ($\forall$):** $\forall x \in X, P(x)$ means $P(x)$ holds for every $x$ in $X$.
- **There exists ($\exists$):** $\exists x \in X, P(x)$ means there is at least one $x$ in $X$ for which $P(x)$ holds.
- **Set-builder notation:** $\{x \in X : P(x)\}$ is the set of all $x$ in $X$ such that $P(x)$ is true.
- **Cardinality:** $|A|$ is the number of elements in set $A$ (finite case) or its "size" (infinite case).
- **Function:** A rule assigning to each $x \in X$ a unique $y \in Y$.

## Appendix C: Proof Techniques

- **Direct Proof:** Start from assumptions, apply definitions and known results to reach the conclusion.
- **Contrapositive Proof:** To prove $A \implies B$, prove $\neg B \implies \neg A$.
- **Proof by Contradiction:** Assume the statement is false, derive a contradiction.
- **Proof by Induction:** Used for statements about integers:
    - **Base case:** Prove for first value (often $n=0$ or $n=1$).
    - **Inductive step:** Assume true for $n$, prove for $n+1$.
- **Proof by Cases:** Consider all possible cases that cover the possibilities.
- **Existence Proof:** Show at least one object with the desired property exists.
- **Uniqueness Proof:** Show that any two objects with the property must be equal.

## Appendix D: References and Suggested Reading

- W. Rudin, *Principles of Mathematical Analysis*
- W. Rudin, *Real and Complex Analysis*
- E.M. Stein & R. Shakarchi, *Fourier Analysis* and *Complex Analysis*
- E.T. Whittaker & G.N. Watson, *A Course of Modern Analysis*
- T.W. Körner, *A Companion to Analysis*
- J.B. Conway, *Functions of One Complex Variable*
- E. Kreyszig, *Advanced Engineering Mathematics* (applied perspective)
- T. Tao, *Analysis* I and II
- S. Axler, *Linear Algebra Done Right* (for functional analysis prerequisites)
- L. Ahlfors, *Complex Analysis*
- M. Spivak, *Calculus* (rigorous single-variable calculus)
- Open online resources:  
  - Terence Tao’s blog  
  - Paul’s Online Math Notes  
  - Math Stack Exchange