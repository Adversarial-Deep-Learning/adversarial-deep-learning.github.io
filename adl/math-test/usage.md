---
title: MathJax v3 usage
parent: MathJax Test
layout: default
grand_parent: Adversarial Deep Learning
math: mathjax3
---

# MathJax v3

Just the Docs sites can be customised to support [MathJax](https://www.mathjax.org),
as explained in the [configuration suggestions](config).
Pages with `math: mathjax3` in the front matter then render $$\mathrm{\LaTeX}$$ code in [kramdown math blocks](https://kramdown.gettalong.org/syntax.html#math-blocks) using MathJax v3.
For example:

$$
\begin{aligned}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{aligned}
$$

To see the $$\mathrm{\LaTeX}$$ source of the formula, right-click anywhere on it.
