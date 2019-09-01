# tsvtools

Utilities for tab-separated files: viewing, filtering, reordering.

Usage:

```
tsv file.tsv
cat file.tsv | tsv
cat file.tsv.gz | tsv
cat variants.tsv | tsvtools filter -header BIOTYPE eq protein_coding
```
