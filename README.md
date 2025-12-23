# Group Project B3 report repository
Topic: Bubble Extraction and Dialog Translation for Japanese Manga

Members: Nguyen Lam Tung, Nguyen Vu Hong Ngoc, Le Chi Thanh Lam, Hoang Khanh Dong, Pham Quang Vinh, Pham Quang Minh

Instructions
1. Set up (For Linux users)

- Download LaTeX packages

```
sudo apt install texlive-latex-recommended
sudo apt install texlive-publishers
```

- Download LaTeX extension on VSC: LaTeX Workshop
- Compile LaTeX file by these commands:
```
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

2. Notes for members

Each member works on his/her branch, create tex files in "sections", "subsections", "subsubsections" directories to include them in the main.tex file:

```
\input{file}
```
DO NOT USE \include BECAUSE IT PUT OUR CONTENTS INTO A CLEAR PAGE 

Example tree directory for a personal branch: 

```
├── README.md
├── img
│   └── usth.jpg
├── main.aux
├── main.bbl
├── main.blg
├── main.log
├── main.out
├── main.pdf
├── main.tex
├── main.toc
├── references.bib
└── sections
    ├── introduction.tex
    ├── literature-review.tex
    ├── motivation.tex
    ├── subsections
    │   └── dataset.tex
    └── subsubsections
        └── data-preparation-bubble-seg.tex
```
