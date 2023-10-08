# Bibidy
A simple command line tool for basic manipulations of bib files

## install

```bash
pip install git+https://github.com/michelecafagna26/bibidy.git#egg=bibidy
```

## Command line usage

Merge a list of bibtex files removing duplicates.
```bash
bibidy merge mybib1.bib,mybib2.bib,mybib2.bib --out merged.bib
```

Return the shared references in the provided list of bibtext files.
```bash
bibidy intersect mybib1.bib,mybib2.bib,mybib2.bib --out intersection.bib
```
