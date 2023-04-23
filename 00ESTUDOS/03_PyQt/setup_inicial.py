#!/usr/bin/env pydm
#./ ou pydm
from pydm import Display
from pydm.widgets import PyDMLineEdit, PyDMLabel
from qtpy.QtWidgets import QFormLayout

class setup_inicial(Display):

    def __init__(self, args, macros):
        
        print(args)
        print(macros)

        super().__init__(ui_filename="")

        layout = QFormLayout()
        for i in range (int(args[0])):
            label = PyDMLabel()
            edit = PyDMLineEdit()
            label.text = "oi"
            layout.addRow(PyDMLabel(), PyDMLineEdit())

        self.setLayout(layout)