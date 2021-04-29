# Makefile
# IVS projekt 2 - Calcules
# Autor: Matej Koreň, xkoren10

all:
	python3 main.py

requirements:
	sudo apt-get install python3 python3-pip python3-pyqt5
	pip install pyinstaller

run:
	python3 main.py

profile:
	python3 profiling.py

test:
	python3 Math_lib_tests.py
	python3 calc_tests.py

exe:
	pyinstaller --noconfirm --onefile --windowed --icon "logo.ico" --add-data "calc.py;." --add-data "calculator.py;." --add-data "calcules_Ui.py;." --add-data "Math_lib.py;." --add-data "logo.ico;." --add-data "../User manual.pdf;." --hidden-import "PyQt5" "main.py"

doc:
	doxygen Doxyfile

pack:
	mkdir ../../pack
	cp "calc.py"  ../../pack
	cp "calculator.py"  ../../pack
	cp "main.py"  ../../pack
	cp "Math_lib.py"  ../../pack
	cp "calcules_Ui.py"  ../../pack
	cp ../"User manual.pdf" ../../pack
	cp ../"hodnoceni.txt" ../../pack
	echo `date +'%y.%m.%d %H:%M:%S'` > ../../pack/odevzdani.txt
	cd ../../pack ; zip -r xkoren10_xhloze02_xtissm00.zip *
	cp "../../pack/xkoren10_xhloze02_xtissm00.zip"  ../../
	rm -f "xkoren10_xhloze02_xtissm00.zip"
	rm -r ../../pack


clean:
	rm -rf ../../IVS-projekt

help:
	-@echo "----------Makefile for Calcules by PyJaMa's------------"
	-@echo ""
	-@echo "Please check, if you have Python and PyQt5 installed."
	-@echo "     (you can use make requirements to do so)"
	-@echo ""
	-@echo "Commands:"
	-@echo "make requirements == checks required programs"
	-@echo "make test == runs Math_lib_tests.py and calc_tests.py"
	-@echo "make doc == generates HTML documentation"
	-@echo "make / make all / make run == runs main.py"
	-@echo "make profile == runs profiling.py"
	-@echo "make pack == packs all files needed for wis .zip file"
	-@echo "make clean == deletes .zip file"

