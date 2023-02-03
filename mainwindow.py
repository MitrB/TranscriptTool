# This Python file uses the following encoding: utf-8
import sys
import whisper
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

LANGUAGE_OPTIONS = ["English", "Francais", "Nederlands"]
PRECISION_OPTIONS = ["very High", "high", "medium", "low", "very low"]

language_map = {"English": "en", "Francais": "fr", "Nederlands": "nl"}
precision_map = {	PRECISION_OPTIONS[0]: "large", 	\
                        PRECISION_OPTIONS[1]: "medium", \
                        PRECISION_OPTIONS[2]: "small", 	\
                        PRECISION_OPTIONS[3]: "base", 	\
                        PRECISION_OPTIONS[4]: "tiny"	\
                        }


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_path = None

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                      "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.file_path = file_name
            self.ui.path_label.setText(self.file_path)

    def transcribe_file(self):
        self.ui.status_label.setText("Transcribing, please wait.")
        chosen_language = self.ui.option_language.currentText()
        precision = self.ui.option_precision.currentText()


        chosen_language = language_map[chosen_language]
        precision = precision_map[precision]

        model = whisper.load_model(precision)
        transcribed_text = model.transcribe(self.file_path, language = chosen_language)
        output_file = self.file_path.split('/')[-1].split('.')[0] + "_transcribed.txt"
        self.ui.status_label.setText(f"Writing to {output_file}, please wait.")
        with open(f"{output_file}", "w+") as file:
            file.write(transcribed_text["text"])
            file.write('\n')
        self.ui.status_label.setText(f"Done. Transcription written to: {output_file}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
