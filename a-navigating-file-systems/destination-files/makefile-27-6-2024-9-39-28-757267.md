test:
	./b-file-writer.py
	cat -n test-output-file.md




sysarg:
	@echo "= Run the sys.argv processing script without input arguments."
	./z_sys_arg_for_loop.py
	@echo = Run the program with unary input argument.
	./z_sys_arg_for_loop.py -h
	@echo "= Run the sys.argv processing script with 2-tuple/paired input arguments."
	./z_sys_arg_for_loop.py -h -k ./input-files/bibtex_keys.csv
	./z_sys_arg_for_loop.py -h -m ./input-files/keyphrases_as_metadata.csv
	./z_sys_arg_for_loop.py -h -k ./input-files/bibtex_keys.csv -m ./input-files/keyphrases_as_metadata.csv
	@echo "= Process the same set of options together without the help manual."
	./z_sys_arg_for_loop.py -k ./input-files/bibtex_keys.csv -m ./input-files/keyphrases_as_metadata.csv
	./z_sys_arg_for_loop.py -a "John L. Hennessy and David A. Patterson"
	./z_sys_arg_for_loop.py -a "Zhiyang Ong"
	./z_sys_arg_for_loop.py -z "Ong"
	./z_sys_arg_for_loop.py -h -z "Ong" -h -h -h
	./z_sys_arg_for_loop.py -h -z "Ong" -h -h
	./z_sys_arg_for_loop.py -b "Design Automation Conference"
	./z_sys_arg_for_loop.py -j "\{ACM\} Computing Surveys"
	./z_sys_arg_for_loop.py -s "The Kluwer International Series in Engineering and Computer Science"
	./z_sys_arg_for_loop.py -u "Massachusetts Institute of Technology"
