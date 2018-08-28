import datetime
import os

from . import AdcpJson as JSON
from . import subsystem_view
from . import subsystem_vm
from rti_python.ADCP import AdcpCommands as Commands
from rti_python.ADCP.Predictor import DataStorage as DS
from rti_python.ADCP import Subsystem as SS
from . import predictor_view


class PredictorVM(predictor_view.Ui_RoweTechPredictor):
    """
    Prediction model.
    """

    def __init__(self, parent):
        predictor_view.Ui_RoweTechPredictor.__init__(self)
        self.setupUi(parent)
        self.parent = parent

        # Calculated results
        self.calc_power = 0.0
        self.calc_data = 0.0
        self.calc_num_batt = 0.0

        self.revLabel.setText("© RoweTech Inc. Rev 1.8")

        # Connect the buttons
        self.addSubsystemButton.clicked.connect(self.add_subsystem)
        self.addSubsystemButton.setStyleSheet("background: #c8e6c9")
        self.predictionGroupBox.setStyleSheet("QGroupBox { background: #e3f2fd }\n QGroupBox::title { background-color: transparent; }")

        self.tabSubsystem.setTabsClosable(True)
        self.tabSubsystem.clear()
        self.tabSubsystem.tabCloseRequested.connect(self.tab_close_requested)
        #self.calculateButton.clicked.connect(self.calculate)
        self.saveCommandsButton.clicked.connect(self.save_to_file)

        # Create the list of subsystems
        self.init_list()

        # Set the tooltips from the JSON file
        self.set_tooltips()

        # Recalculate when value changes
        self.deploymentDurationSpinBox.valueChanged.connect(self.valueChanged)
        self.ceiDoubleSpinBox.valueChanged.connect(self.valueChanged)
        self.cwsSpinBox.valueChanged.connect(self.valueChanged)
        self.cerecordCheckBox.stateChanged.connect(self.valueChanged)
        self.dataFormatComboBox.currentIndexChanged.connect(self.valueChanged)
        self.coordinateTransformComboBox.currentIndexChanged.connect(self.valueChanged)

        # Initialize to RTB
        self.dataFormatComboBox.setCurrentText("RTB")
        self.coordinateTransformComboBox.setDisabled(True)

        # Set status bar
        self.parent.statusBar().showMessage('Add a subsystem to begin configuring...')

        # Command file
        self.cepo_list = []
        self.command_file = []

        # Run initial Calculate
        self.calculate()

    def init_list(self):
        # Add item to combobox.  Set the userData to subsystem code
        self.subsystemComboBox.addItem("2 - 1200kHz", "2")
        self.subsystemComboBox.addItem("3 - 600kHz", "3")
        self.subsystemComboBox.addItem("4 - 300kHz", "4")
        self.subsystemComboBox.addItem("6 - 1200kHz 45 degree offset", "6")
        self.subsystemComboBox.addItem("7 - 600kHz 45 degree offset", "7")
        self.subsystemComboBox.addItem("8 - 300kHz 45 degree offset", "8")
        self.subsystemComboBox.addItem("A - 1200kHz Vertical", "A")
        self.subsystemComboBox.addItem("B - 600kHz Vertical", "B")
        self.subsystemComboBox.addItem("C - 300kHz Vertical", "C")
        self.subsystemComboBox.addItem("D - 150kHz Vertical", "D")
        self.subsystemComboBox.addItem("E - 75kHz Vertical", "E")

        self.dataFormatComboBox.addItem("RTB", "RTB")
        self.dataFormatComboBox.addItem("PD0", "PD0")

        self.coordinateTransformComboBox.addItem("Beam", "Beam")
        self.coordinateTransformComboBox.addItem("Instrument", "Instrument")
        self.coordinateTransformComboBox.addItem("Earth", "Earth")
        self.coordinateTransformComboBox.addItem("Ship", "Ship")

    def set_tooltips(self):
        """
        Set the tooltip for all the values.  The tooltip will be found
        in a JSON file.  This file can be changed for other languages.
        :return:
        """
        # Get the JSON file
        cmds = JSON.get_json()
        if cmds is None:
            self.commandFileTextBrowser.append('Error loading the configuration file')
            return
        else:
            self.commandFileTextBrowser.append('File found')

        self.ceiDoubleSpinBox.setToolTip(Commands.get_tooltip(cmds["CEI"]["desc"]))
        self.cwsSpinBox.setToolTip(Commands.get_tooltip(cmds["CWS"]["desc"]))
        self.cwtSpinBox.setToolTip(Commands.get_tooltip(cmds["CWT"]["desc"]))
        self.ctdSpinBox.setToolTip(Commands.get_tooltip(cmds["CTD"]["desc"]))
        self.dataFormatComboBox.setToolTip(Commands.get_tooltip(cmds["CEOUTPUT"]["desc"]))
        self.speedOfSoundSpinBox.setToolTip(Commands.get_tooltip(cmds["CWSS"]["desc"]))
        self.cerecordCheckBox.setToolTip(Commands.get_tooltip(cmds["CERECORD"]["desc"]))
        self.deploymentDurationSpinBox.setToolTip("Number of days the ADCP will be deployed.")
        self.predictionGroupBox.setToolTip("Prediction results from all the subsystem configurations combined.")
        self.commandFileGroupBox.setToolTip("Command file generated from all the subsystem configurations.")
        self.subsystemConfigGroupBox.setToolTip("Select a subsystem to create a configuration.")
        self.saveCommandsButton.setToolTip("Save the commands to a text file.\nThe file will be saved to location of the application.\nThe file name will be the date and time.")
        #self.dataFormatComboBox.setToolTip("Select the data format.  RTB = Rowe Tech Binary.  PD0 is an industry standard format used on TRDI systems.")
        self.coordinateTransformComboBox.setToolTip("Select the coordinate Transform for PD0.  Beam = Raw Data, Instrument = X,Y,Z,Err, Earth=East,North,Vert,Err")

    def add_subsystem(self):
        """
        Add a tab for the given subsystem.
        :return:
        """
        ss = self.subsystemComboBox.itemData(self.subsystemComboBox.currentIndex())

        # Create the subsystem view
        # Add it to the Tab
        ssUI = subsystem_view.Ui_Subsystem()
        ssVM = subsystem_vm.SubsystemVM(self.tabSubsystem, self, ss)
        ss_label = "[" + str(ss) + "] - " + SS.ss_label(ss)
        self.tabSubsystem.addTab(ssVM, ss_label)

        # Add subsystem to CEPO
        self.cepo_list.append(ss)

        # Recalculate
        self.calculate()

        self.parent.statusBar().showMessage(ss_label + ' added to configuration.')

    def tab_close_requested(self, index):
        """
        Remove the tab.
        :param index: Index of the tab.
        :return:
        """
        self.tabSubsystem.removeTab(index)

        # Remove from the CEPO list
        del self.cepo_list[index]

        if self.tabSubsystem.count() == 0:
            # Set status bar
            self.parent.statusBar().showMessage('Add a subsystem to begin configuring...')

        # Recalculate
        self.calculate()

    def valueChanged(self, value):
        """
        Use this to handle a value changed.
        :param value: New value.
        :return:
        """
        # Disable coordinate transform if RTB is selected
        if self.dataFormatComboBox.currentText() == "RTB":
            self.coordinateTransformComboBox.setDisabled(True)
        else:
            self.coordinateTransformComboBox.setDisabled(False)

        for tab in range(self.tabSubsystem.count()):
            if self.dataFormatComboBox.currentText() == "RTB":
                self.tabSubsystem.widget(tab).cedBeamVelCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedInstrVelCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedEarthVelCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedAmpCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedCorrCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedBeamGoodPingCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedEarthGoodPingCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedEnsCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedAncCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedBtCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedNmeaCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedWpEngCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedBtEngCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedSysSettingCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedRangeTrackingCheckBox.setDisabled(False)
            else:
                self.tabSubsystem.widget(tab).cedBeamVelCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedBeamVelCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedInstrVelCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedEarthVelCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedAmpCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedCorrCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedBeamGoodPingCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedEarthGoodPingCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedEnsCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedAncCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedBtCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedNmeaCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedWpEngCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedBtEngCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedSysSettingCheckBox.setDisabled(True)
                self.tabSubsystem.widget(tab).cedRangeTrackingCheckBox.setDisabled(True)


        # Calculate prediction
        self.calculate()

    def calculate(self):
        """
        Calculate the new prediction results.
        :return:
        """
        # Clear the results
        self.calc_power = 0.0
        self.calc_data = 0.0
        self.calc_num_batt = 0.0

        for tab in range(self.tabSubsystem.count()):
            self.tabSubsystem.widget(tab).calculate()
            # print(self.tabSubsystem.widget(tab).cwpblDoubleSpinBox.value())

            # Accumlate the values
            self.calc_data += self.tabSubsystem.widget(tab).calc_data
            self.calc_num_batt += self.tabSubsystem.widget(tab).calc_num_batt
            self.calc_power += self.tabSubsystem.widget(tab).calc_power


        # Update the display
        self.powerLabel.setText(str(round(self.calc_power, 2)) + " watt*hr")
        self.powerLabel.setStyleSheet("font-weight: bold; color: blue")
        self.numBatteriesLabel.setText(str(round(self.calc_num_batt, 2)) + " batteries")
        self.numBatteriesLabel.setStyleSheet("font-weight: bold; color: blue")
        self.dataUsageLabel.setText(str(DS.bytes_2_human_readable(self.calc_data)))
        self.dataUsageLabel.setStyleSheet("font-weight: bold; color: blue")

        # Update the command file
        self.update_command_file()

    def update_command_file(self):
        self.commandFileTextBrowser.clear()

        self.commandFileTextBrowser.append("CDEFAULT")

        # CEPO List
        cepo = "CEPO "
        for ss in self.cepo_list:
            cepo += ss
        self.commandFileTextBrowser.append(cepo)

        if self.dataFormatComboBox.currentText() == "RTB":
            self.commandFileTextBrowser.append("CEOUTPUT 1")
        else:
            if self.coordinateTransformComboBox.currentText() == "Beam":
                self.commandFileTextBrowser.append("CEOUTPUT 100,0 ")
            elif self.coordinateTransformComboBox.currentText() == "Instrument":
                self.commandFileTextBrowser.append("CEOUTPUT 100,1 ")
            elif self.coordinateTransformComboBox.currentText() == "Earth":
                self.commandFileTextBrowser.append("CEOUTPUT 100,2 ")
            elif self.coordinateTransformComboBox.currentText() == "Ship":
                self.commandFileTextBrowser.append("CEOUTPUT 100,3 ")


        self.commandFileTextBrowser.append("CEI " + Commands.sec_to_hmss(self.ceiDoubleSpinBox.value()))
        self.commandFileTextBrowser.append("CWS " + str(self.cwsSpinBox.value()))
        self.commandFileTextBrowser.append("CWSS " + str(self.speedOfSoundSpinBox.value()))

        if self.cerecordCheckBox.isChecked():
            self.commandFileTextBrowser.append("CERECORD " + "1")
        else:
            self.commandFileTextBrowser.append("CERECORD " + "0")

        for tab in range(self.tabSubsystem.count()):
            ss_cmd_list = self.tabSubsystem.widget(tab).get_cmd_list()
            for ss_cmd in ss_cmd_list:
                self.commandFileTextBrowser.append(ss_cmd.to_str(tab))

        self.commandFileTextBrowser.append("CSAVE")
        self.commandFileTextBrowser.append("START")

    def save_to_file(self):

        # Create a new file name based off date and time
        file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S_RTI_CFG.txt")
        file_path = os.path.expanduser("~/Desktop/"+file_name)

        file = open(file_path, 'w')
        file.write(self.commandFileTextBrowser.toPlainText())
        file.close()

        self.parent.statusBar().showMessage('File saved to ' + file_path)

