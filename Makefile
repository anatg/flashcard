make:
	python flashcards.py $(ARG)
clean:
	rm *~
test:
	python test.py