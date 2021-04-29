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
	python3 Math_Lib_tests.py
	python3 calc_tests.py

exe:
	pyinstaller --noconfirm --onefile --windowed --icon "logo.ico" --add-data "calc.py;." --add-data "calculator.py;." --add-data "calcules_Ui.py;." --add-data "Math_lib.py;." --add-data "logo.ico;." --add-data "../User manual.pdf;." --hidden-import "PyQt5" "main.py"

doc:
	doxygen Doxyfile

pack:
-mkdir ..\..\src
	-robocopy /MIR ..\src ..\..\src
	-copy ..\User manual.pdf ..\..
	-copy ..\hodnoceni.txt ..\..
	-echo %time% %date% > ..\..\odevzdani.txt
	-powershell /C Compress-Archive -Path "..\..\src", "..\..\"User Manual.pdf", "..\..\hodnoceni.txt", "..\..\odevzdani.txt" -DestinationPath ..\..\xkoren10_xhloze02_xtissm00.zip -CompressionLevel Optimal -Force
	-rmdir /s /q %cd%\..\..\src
	-del /q %cd%\..\..\User Manual.pdf
	-del /q %cd%\..\..\hodnoceni.txt
	-del /q %cd%\..\..\odevzdani.txt

clean:
	rm -rf ../plan/ ../profiling/ ../GUI ../install

help:
	-@echo "----------Makefile for Calcules by PyJaMa's------------"
	-@echo ""
	-@echo "Please check, if you have Python and PyQt5 installed."
	-@echo "     (you can use make requirements to do so)"
	-@echo ""
	-@echo "Commands:"
	-@echo "make requirements == checks required programs"
	-@echo "make test == runs Math_Lib_tests.py and calc_tests.py"
	-@echo "make doc == generates HTML documentation"
	-@echo "make / make all / make run == runs main.py"
	-@echo "make profile == runs profiling.py"
	-@echo "make pack == packs all needed files .zip file"
	-@echo "make clean == deletes .zip file"

