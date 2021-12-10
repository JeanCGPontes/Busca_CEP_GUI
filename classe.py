import functions

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QApplication, QLineEdit, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

        #  Fonts
        self.Arial_Rounded_MT_Bold = functions.get_font("Arial Rounded MT Bold", 16)
        self.Bahnschrift_Light_SemiCondensed = functions.get_font("Bahnschrift Light SemiCondensed", 16)
        self.DejaVu_Sans_Condensed = functions.get_font("DejaVu Sans Condensed", 14)

        #  Window settings
        self.setGeometry(350, 225, 400, 440)
        self.setStyleSheet("QMainWindow { background-color: rgb(248, 248, 248) }")
        self.setWindowTitle("Busca CEP")
        self.setWindowIcon(QIcon("images/globe.ico"))

        #  Creation and configuration of the map image label
        self.map_image_label = QLabel(self)
        self.map_image_label.setGeometry(0, 0, 400, 100)
        self.map_image_label.setStyleSheet("""QLabel { border-color: rgb(0, 0, 0);
                                                       border-width: 1px;
                                                       border-style:solid }""")
        self.map_image_label.setPixmap(QPixmap("images/roadmap_view.png"))

        #  Creation and configuration of the text box that will receive the CEP
        self.cep_number = QLineEdit(self)
        self.cep_number.setGeometry(100, 80, 200, 40)
        self.cep_number.setStyleSheet("""QLineEdit { background-color: rgb(255, 255, 255);
                                          color: rgb(29, 29, 29);
                                          border-color: rgb(0, 0, 0);
                                          border-width: 1px;
                                          border-style: solid;
                                          border-radius: 4; }""")
        self.cep_number.setFont(self.Arial_Rounded_MT_Bold)
        self.cep_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cep_number.returnPressed.connect(self.update_labels)

        #  Frame creation and configuration
        self.information_frame = QFrame(self)
        self.information_frame.setGeometry(5, 130, 390, 245)
        self.information_frame.setStyleSheet("""QFrame { background-color: rgb(255, 255, 255);
                                                         border-color: rgb(0, 0, 0);
                                                         border-width: 1px;
                                                         border-style:solid;
                                                         border-radius: 4; }""")

        #  Creation and configuration of the button that will start the search
        self.search_button = QPushButton(self)
        self.search_button.setText("Search")
        self.search_button.setGeometry(150, 385, 100, 40)
        self.search_button.setStyleSheet("""QPushButton { background-color: rgba(65, 255, 51, 210);
                                                          border-color: rgb(0, 0, 0);
                                                          border-width: 1px;
                                                          border-style:solid;
                                                          border-radius: 4; }
                                      QPushButton:hover { background-color: rgb(170, 255, 127) }""")
        self.search_button.setFont(self.Bahnschrift_Light_SemiCondensed)

        #  Creation and configuration of labels that will be in the information frame
        default_style = ("""QLabel { background-color: rgb(255, 255, 255);
                                     border-color: rgb(0, 0, 0);
                                     border-width: 0px;
                                     border-style: solid;
                                     border-radius: 0; }""")
        self.street_label = functions.create_label(self.information_frame, 5, 5, 380, 55, default_style, self.DejaVu_Sans_Condensed, 5)
        self.district_label = functions.create_label(self.information_frame, 5, 65, 380, 55, default_style, self.DejaVu_Sans_Condensed, 5)
        self.city_label = functions.create_label(self.information_frame, 5, 125, 380, 55, default_style, self.DejaVu_Sans_Condensed, 5)
        self.state_label = functions.create_label(self.information_frame, 5, 185, 380, 55, default_style, self.DejaVu_Sans_Condensed, 5)

        self.street_label.setText("Rua: ")
        self.district_label.setText("Bairro: ")
        self.city_label.setText("Cidade: ")
        self.state_label.setText("Estado: ")

        #  Search button function setting
        self.search_button.clicked.connect(self.update_labels)

        #  Show window
        self.show()

    def get_cep_provided(self):

        """Module that takes the value provided by the user"""

        information_provided = self.cep_number.text()

        return information_provided

    @staticmethod
    def search_cep(cep):

        """Module that starts the search for information through the cep provided"""

        web_request_response = functions.get_web_request_response(cep)
        json = functions.get_json(web_request_response)
        street = functions.get_street(json)
        district = functions.get_district(json)
        city = functions.get_city(json)
        state = functions.get_state(json)
        acronym = functions.get_acronym(json)

        return street, district, city, state, acronym

    def update_labels(self):

        """Module that updates the information frame labels"""

        cep = self.get_cep_provided()
        street, district, city, state, acronym = self.search_cep(cep)
        self.street_label.setText(f"Rua: {street}")
        self.district_label.setText(f"Bairro: {district}")
        self.city_label.setText(f"Cidade: {city}")
        self.state_label.setText(f"Estado: {state} {acronym}")
