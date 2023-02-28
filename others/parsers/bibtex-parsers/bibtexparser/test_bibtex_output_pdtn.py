#!/Users/zhiyang/anaconda3/bin/python


"""
	Slightly modified from the example in [Boulogne2023a].

	https://bibtexparser.readthedocs.io/en/master/tutorial.html#call-the-writer

	References:
	+ [Boulogne2022]
		- Francois Boulogne, Michael Weiss, and sciunto, "bibtexparser 1.4.0," Python Software Foundation, Beaverton, OR, September 23, 2022. Available online from *PyPI -- The Python Package Index: pew 1.4.0* at: https://pypi.org/project/bibtexparser/; February 25, 2023 was the last accessed date.
	+ [Boulogne2023a]
		- Fran{\c{c}}ois Boulogne, Olivier Mangin, Lucas Verney, and other contributors, "Tutorial," Read the Docs, Inc., Portland, OR, January 3, 2023. Available online from *Read the Docs: Welcome to BibtexParser's documentation!: Tutorial* as Version 1.4.0 at: https://bibtexparser.readthedocs.io/en/master/tutorial.html; February 25, 2023 was the last accessed date.
"""


from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

db = BibDatabase()
db.entries = [
    {'journal': 'Nice Journal',
     'comments': 'A comment',
     'pages': '12--23',
     'month': 'jan',
     'abstract': 'This is an abstract. This line should be long enough to test\nmultilines...',
     'title': 'An amazing title',
     'year': '2013',
     'volume': '12',
     'ID': 'Cesar2013',
     'author': 'Jean César',
     'keyword': 'keyword1, keyword2',
     'ENTRYTYPE': 'article'}]

writer = BibTexWriter()
writer.indent = '    '     # indent entries with 4 spaces instead of one
writer.comma_first = True  # place the comma at the beginning of the line
with open('./output-files/bibtex.bib', 'w') as bibfile:
    bibfile.write(writer.write(db))