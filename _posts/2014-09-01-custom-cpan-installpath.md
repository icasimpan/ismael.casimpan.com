---
published: false
---

## Custom CPAN Install Path

Do something like 
```
cpan> o conf mbuildpl_arg "--install_base /proj/rose/"
cpan> o conf makepl_arg "PREFIX=/proj/rose/"
cpan> install HTML::Template
```
See perlmonk: [Set Install path in CPAN](http://www.perlmonks.org/?node_id=630026)
