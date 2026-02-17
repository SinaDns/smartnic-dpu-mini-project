.PHONY: all report slides clean

all: report slides

report:
	cd docs/report && pdflatex report.tex && pdflatex report.tex

slides:
	cd docs/slides && pdflatex presentation.tex && pdflatex presentation.tex

clean:
	find . -type f -name "*.aux" -delete
	find . -type f -name "*.log" -delete
	find . -type f -name "*.out" -delete
	find . -type f -name "*.toc" -delete
	find . -type f -name "*.nav" -delete
	find . -type f -name "*.snm" -delete
	find . -type f -name "*.vrb" -delete
