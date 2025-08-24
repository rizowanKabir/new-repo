import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QCheckBox, QFrame,
                             QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # --- CRUCIAL STEP ---
        # Replace "YOUR_API_KEY_HERE" with your actual OpenWeatherMap API key.
        self.api_key = "97b6ebc103843f0f88a45652202e9cee"

        self.weather_data = {}

        self.initUI()
        self.apply_styles()

        # Check if the API key has been set.
        if self.api_key == "YOUR_API_KEY_HERE" or not self.api_key:
            self.show_api_key_error()

    def initUI(self):
        """Initializes the User Interface."""
        self.setWindowTitle("Weather App")
        self.setGeometry(300, 300, 500, 550)

        # --- Widgets ---
        self.city_label = QLabel("Enter City Name:")
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("e.g., London")
        self.get_weather_button = QPushButton("Get Weather", self)
        self.unit_toggle = QCheckBox("Show in Fahrenheit", self)

        # Separator Line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        # --- Result Widgets ---
        self.status_label = QLabel("Enter a city to get started.", self)
        self.temperature_label = QLabel("--", self)
        self.emoji_label = QLabel("", self)
        self.description_label = QLabel("", self)
        self.details_label = QLabel("", self)

        # --- Layouts ---
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        result_header_layout = QHBoxLayout()

        input_layout.addWidget(self.city_label)
        input_layout.addWidget(self.city_input)

        result_header_layout.addStretch()  # Add spacer to push content to the right
        result_header_layout.addWidget(self.temperature_label)
        result_header_layout.addWidget(self.emoji_label)
        result_header_layout.addStretch()  # Add spacer to center content

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.get_weather_button)
        main_layout.addWidget(self.unit_toggle)
        main_layout.addWidget(line)
        main_layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
        main_layout.addLayout(result_header_layout)
        main_layout.addWidget(self.description_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.details_label, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

        # --- Connections ---
        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)
        self.unit_toggle.toggled.connect(self.update_weather_display)

    def apply_styles(self):
        """Applies stylesheet to the widgets."""
        self.setStyleSheet("""
            QWidget { background-color: #f0f8ff; }
            QLabel { font-family: 'Segoe UI', Calibri; font-size: 16px; color: #333; }
            QLineEdit { font-size: 18px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
            QPushButton {
                font-size: 18px; font-weight: bold; padding: 10px;
                background-color: #4682b4; color: white; border: none; border-radius: 5px;
            }
            QPushButton:hover { background-color: #5a9bd4; }
            QPushButton:disabled { background-color: #a9a9a9; }
            #TemperatureLabel { font-size: 80px; font-weight: bold; color: #2c3e50; }
            #EmojiLabel { font-size: 70px; }
            #DescriptionLabel { font-size: 24px; font-style: italic; color: #555; }
            #DetailsLabel { font-size: 16px; color: #555; }
            #StatusLabel { font-size: 16px; color: #d35400; font-weight: bold; }
        """)
        self.temperature_label.setObjectName("TemperatureLabel")
        self.emoji_label.setObjectName("EmojiLabel")
        self.description_label.setObjectName("DescriptionLabel")
        self.details_label.setObjectName("DetailsLabel")
        self.status_label.setObjectName("StatusLabel")
        self.emoji_label.setFont(QFont("Segoe UI Emoji", 40))

    def get_weather(self):
        city = self.city_input.text()
        if not city:
            self.display_error("Please enter a city name.")
            return

        # Provide UI feedback
        self.get_weather_button.setDisabled(True)
        self.status_label.setText("Loading...")
        QApplication.processEvents()  # Force UI update

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
            self.weather_data = response.json()
            self.status_label.setText("")  # Clear status on success
            self.update_weather_display()

        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                self.display_error(f"City not found: '{city}'")
            elif response.status_code == 401:
                self.display_error("Invalid API Key. Please check your key.")
            else:
                self.display_error(f"HTTP Error: {http_err}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: Check your internet.")
        except requests.exceptions.Timeout:
            self.display_error("Request Timed Out.")
        except requests.exceptions.RequestException as err:
            self.display_error(f"An error occurred: {err}")
        finally:
            # IMPORTANT: Always re-enable the button
            self.get_weather_button.setDisabled(False)

    def update_weather_display(self):
        """Updates the UI labels with the stored weather data."""
        if not self.weather_data:
            return

        temp_k = self.weather_data["main"]["temp"]
        temp_c = temp_k - 273.15
        temp_f = temp_c * 9 / 5 + 32

        feels_like_k = self.weather_data["main"]["feels_like"]
        feels_like_c = feels_like_k - 273.15
        feels_like_f = feels_like_c * 9 / 5 + 32

        description = self.weather_data["weather"][0]["description"].title()
        weather_id = self.weather_data["weather"][0]["id"]
        humidity = self.weather_data["main"]["humidity"]
        wind_speed_ms = self.weather_data["wind"]["speed"]
        wind_speed_kmh = wind_speed_ms * 3.6

        # Set display based on unit toggle
        if self.unit_toggle.isChecked():  # Fahrenheit
            temp_str = f"{temp_f:.0f}°F"
            feels_like_str = f"{feels_like_f:.0f}°F"
        else:  # Celsius
            temp_str = f"{temp_c:.0f}°C"
            feels_like_str = f"{feels_like_c:.0f}°C"

        self.temperature_label.setText(temp_str)
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(description)
        self.details_label.setText(
            f"Feels Like: {feels_like_str}  |  "
            f"Humidity: {humidity}%  |  "
            f"Wind: {wind_speed_kmh:.1f} km/h"
        )

    def display_error(self, message: str):
        """Shows an error message in the status label and clears old data."""
        self.status_label.setText(message)
        self.temperature_label.setText("--")
        self.emoji_label.setText("")
        self.description_label.setText("")
        self.details_label.setText("")

    def show_api_key_error(self):
        """Displays a pop-up message box if the API key is not set."""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("API Key Not Found!")
        msg_box.setInformativeText(
            'Please open the script file and replace "YOUR_API_KEY_HERE" '
            'with your actual OpenWeatherMap API key.'
        )
        msg_box.setWindowTitle("Configuration Error")
        msg_box.exec_()
        self.get_weather_button.setDisabled(True)
        self.city_input.setDisabled(True)

    @staticmethod
    def get_weather_emoji(weather_id: int) -> str:
        """Returns an emoji based on the OpenWeatherMap condition ID."""
        if 200 <= weather_id < 300:
            return "⛈️"  # Thunderstorm
        elif 300 <= weather_id < 400:
            return "🌦️"  # Drizzle
        elif 500 <= weather_id < 600:
            return "🌧️"  # Rain
        elif 600 <= weather_id < 700:
            return "❄️"  # Snow
        elif 700 <= weather_id < 800:
            return "🌫️"  # Atmosphere (fog, mist)
        elif weather_id == 800:
            return "☀️"  # Clear
        elif 801 <= weather_id < 805:
            return "☁️"  # Clouds
        else:
            return "🤷"


def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()