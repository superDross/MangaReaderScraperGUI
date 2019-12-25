import logging
import sys

from PyQt5.QtWidgets import QApplication

from app.gui import AppGui

# PyQt5 is broken, requires to install PyQt5-sip then PyQt5
# however there is no way to specify install order in setup.py
# so this nasty hack will have to do now
# from PyQt5.QtWidgets import QApplication


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)


# TODO: fix broken gui
def gui() -> None:
    app = QApplication(sys.argv)
    window = AppGui()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    gui()
