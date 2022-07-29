## -*- encoding: utf-8 -*-
"""
This file (./sol/lp_doctest.sage) was *autogenerated* from ./sol/lp.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./sol/lp_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./sol/lp.tex, line 1::

  sage: sage.numerical.backends.generic_backend.default_solver = "Glpk"

Sage example in ./sol/lp.tex, line 28::

  sage: l = [28, 10, -89, 69, 42, -37, 76, 78, -40, 92, -93, 45]
  sage: p = MixedIntegerLinearProgram()
  sage: b = p.new_variable(binary = True)
  sage: p.add_constraint(p.sum([ v*b[v] for v in l ]) == 0)
  sage: p.add_constraint(p.sum([ b[v] for v in l ]) >= 1)
  sage: p.solve()
  0.0
  sage: b = p.get_values(b, convert=ZZ, tolerance=1e-3)
  sage: len([v for v in b if b[v] == 1])
  5
  sage: sum([v for v in b if b[v] == 1])
  0

Sage example in ./sol/lp.tex, line 64::

  sage: g = graphs.PetersenGraph()
  sage: p = MixedIntegerLinearProgram(maximization = False)
  sage: b = p.new_variable(binary = True)
  sage: for v in g:
  ....:     p.add_constraint( p.sum([b[u] for u in g.neighbors(v)])
  ....:                       + b[v] >= 1)
  sage: p.set_objective( p.sum([ b[v] for v in g ]) )
  sage: p.solve()
  3.0
  sage: b = p.get_values(b, convert=ZZ, tolerance=1e-3)
  sage: dom = [v for v in b if b[v] == 1]
  sage: len(dom)
  3
  sage: all((v in dom or any(g.has_edge(x,v) for x in dom)) for v in g)
  True

"""
