import datetime
import os

from PyQt5 import QtWidgets
import qdarkstyle
from . import AdcpJson as JSON
from . import subsystem_view
from . import subsystem_vm
from rti_python.ADCP import AdcpCommands as Commands
from rti_python.ADCP.Predictor import DataStorage as DS
from rti_python.ADCP import Subsystem as SS
from rti_python.ADCP.Predictor import Power as Power
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

        self.revLabel.setText("© RoweTech Inc. Rev 1.13")

        # Command file
        self.cepo_list = []
        self.command_file = []

        # Connect the buttons
        self.addSubsystemButton.clicked.connect(self.add_subsystem)
        #self.addSubsystemButton.setStyleSheet("background: #41658a")
        #self.predictionGroupBox.setStyleSheet("QGroupBox { background: #639ecf }\n QGroupBox::title { background-color: transparent; }")

        #self.powerLabel.setStyleSheet("color: black")
        #self.numBatteriesLabel.setStyleSheet("color: black")
        #self.dataUsageLabel.setStyleSheet("color: black")
        #self.salinityLabel.setStyleSheet("color: black")
        #self.recordingLabel.setStyleSheet("color: black")

        self.tabSubsystem.setTabsClosable(True)
        self.tabSubsystem.clear()
        self.tabSubsystem.tabCloseRequested.connect(self.tab_close_requested)
        #self.calculateButton.clicked.connect(self.calculate)
        self.saveCommandsButton.clicked.connect(self.save_to_file)
        self.darkCheckBox.clicked.connect(self.change_theme)

        # Init progressbars
        #self.batteryProgressBar.setMinimum(0)
        #self.batteryProgressBar.setMaximum(1)
        #self.batteryProgressBar.setValue(1)
        #self.dataUsageProgressBar.setMinimum(0)
        #self.dataUsageProgressBar.setMaximum(1)
        #self.batteryProgressBar.setValue(1)

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
        self.batteryTypeComboBox.currentIndexChanged.connect(self.valueChanged)
        self.numBatteriesSpinBox.valueChanged.connect(self.valueChanged)
        self.storageSizeSpinBox.valueChanged.connect(self.valueChanged)

        # Initialize to RTB
        self.dataFormatComboBox.setCurrentText("RTB")
        self.coordinateTransformComboBox.setDisabled(True)
        self.cerecordCheckBox.setChecked(True)

        # Set status bar
        self.parent.statusBar().showMessage('Add a subsystem to begin configuring...')


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

        self.batteryTypeComboBox.addItem("Alkaline [440 W-Hr]", 440)
        self.batteryTypeComboBox.addItem("Lithium [2100 W-Hr]", 2100)

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
        self.dataFormatComboBox.setToolTip("Select the data format.  RTB = Rowe Tech Binary.  PD0 is an industry standard format used on TRDI systems.")
        self.coordinateTransformComboBox.setToolTip("Select the coordinate Transform for PD0.  Beam = Raw Data, Instrument = X,Y,Z,Err, Earth=East,North,Vert,Err")
        self.batteryTypeComboBox.setToolTip("Set the battery type to accurately calculate how many batteries will be used.  Default is an alkaline battery.")
        self.numBatteriesSpinBox.setToolTip("Set the number of batteries that will be used in the deployment to accurately calculate how many days the ADCP will last.")
        self.storageSizeSpinBox.setToolTip("Set size of the internal and external SD cards to accurately calculate the deployment length.  The default is 32GB.")

    def add_subsystem(self):
        """
        Add a tab for the given subsystem.
        :return:
        """
        ss = self.subsystemComboBox.itemData(self.subsystemComboBox.currentIndex())

        # Create the subsystem view
        # Add it to the Tab
        #ssUI = subsystem_view.Ui_Subsystem()
        ssVM = subsystem_vm.SubsystemVM(self.tabSubsystem, self, ss, None)
        ss_label = "[" + str(ss) + "] - " + SS.ss_label(ss)
        self.tabSubsystem.addTab(ssVM, ss_label)

        # Add subsystem to CEPO
        self.cepo_list.append(ss)

        # Update the Burst ID
        self.updateBurstID()

        # Recalculate
        self.calculate()

        self.parent.statusBar().showMessage(ss_label + ' added to configuration.')

    def clone_subsystem(self, ss_clone_vm):
        """
        Clone a tab for the given subsystem, based on the viewmodel given.
        :param ss_clone_vm Subsystem config ViewModel to clone.
        :return:
        """
        ss = ss_clone_vm.ss_code

        # Create the subsystem view
        # Add it to the Tab
        ssVM = subsystem_vm.SubsystemVM(self.tabSubsystem, self, ss, ss_clone_vm)
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
                #self.tabSubsystem.widget(tab).cedBeamVelCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedInstrVelCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedEarthVelCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedAmpCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedCorrCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedBeamGoodPingCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedEarthGoodPingCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedEnsCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedAncCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedBtCheckBox.setDisabled(False)
                #self.tabSubsystem.widget(tab).cedNmeaCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedWpEngCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedBtEngCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedSysSettingCheckBox.setDisabled(False)
                self.tabSubsystem.widget(tab).cedRangeTrackingCheckBox.setDisabled(False)
            else:
                #self.tabSubsystem.widget(tab).cedBeamVelCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedBeamVelCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedInstrVelCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedEarthVelCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedAmpCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedCorrCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedBeamGoodPingCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedEarthGoodPingCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedEnsCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedAncCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedBtCheckBox.setDisabled(True)
                #self.tabSubsystem.widget(tab).cedNmeaCheckBox.setDisabled(True)
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
        self.numBatteriesLabel.setText(str(round(self.calc_num_batt, 2)) + " batteries")
        self.dataUsageLabel.setText(str(DS.bytes_2_human_readable(self.calc_data)))

        # Calculate the power usage for progessbar
        battery_pwr = self.batteryTypeComboBox.itemData(self.batteryTypeComboBox.currentIndex())
        battery_usage_percent = Power.calculate_battery_usage(self.calc_power,
                                                              self.numBatteriesSpinBox.value(),
                                                              battery_pwr)
        if battery_usage_percent > 1:
            self.batteryProgressBar.setValue(100)
        else:
            self.batteryProgressBar.setValue(battery_usage_percent * 100.0)

        # Calculate the data usage for progressbar
        # Convert GB to bytes
        sd_card_mb = self.storageSizeSpinBox.value() * 1024.0
        if sd_card_mb == 0:
            sd_card_mb = 32 * 1024.0
            self.storageSizeSpinBox.setValue(32)
        data_usage_to_mb = self.calc_data / 1048576.0
        data_usage_percentage = (data_usage_to_mb / sd_card_mb) * 100.0

        if data_usage_percentage > 100:
            self.dataUsageProgressBar.setValue(100)
        else:
            self.dataUsageProgressBar.setValue(data_usage_percentage)

        # Salinity Label
        if self.cwsSpinBox.value() <= 5.0:
            self.salinityLabel.setText("Fresh Water")
            self.salinityLabel.setStyleSheet("color: blue;")
        else:
            self.salinityLabel.setText("Salt Water")
            self.salinityLabel.setStyleSheet("")

        # Recording Label
        if self.cerecordCheckBox.isChecked():
            self.recordingLabel.setText("Recording ON")
            self.recordingLabel.setStyleSheet("")
        else:
            self.recordingLabel.setText("Recording OFF")
            self.recordingLabel.setStyleSheet("color: red;")

        # Update the command file
        self.update_command_file()

    def updateStandardorBurstPinging(self, is_cbi_enabled: bool):
        for tab in range(self.tabSubsystem.count()):
            self.tabSubsystem.widget(tab).cbiEnabledCheckBox.setChecked(is_cbi_enabled)

    def updateBurstID(self):
        burst_id = 1
        interleave_count = 0

        # Update all the tabs
        for tab in range(self.tabSubsystem.count()):

            # Track the interleave count
            if self.tabSubsystem.widget(tab).cbiInterleaveSpinBox.value() > 0:
                interleave_count = self.tabSubsystem.widget(tab).cbiInterleaveSpinBox.value()

            # Set the Burst ID
            self.tabSubsystem.widget(tab).cbiBurstIdSpinBox.setValue(burst_id)

            if interleave_count <= 0:
                burst_id += 1
            else:
                interleave_count -= 1

    def update_command_file(self):
        """
        Update the command file.
        """
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
        """
        Save the configuration to a file.  Display on the statusbar
        the location and file name.
        :return:
        """
        # Create a new file name based off date and time
        file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S_RTI_CFG.txt")
        file_path = os.path.expanduser("~\\Desktop\\"+file_name)

        file = open(file_path, 'w')
        file.write(self.commandFileTextBrowser.toPlainText())
        file.close()

        self.parent.statusBar().showMessage('File saved to ' + file_path)

    def change_theme(self):
        """
        Change the theme color.
        :return:
        """
        # get the QApplication instance,  or crash if not set
        app = QtWidgets.QApplication.instance()
        if app is None:
            raise RuntimeError("No Qt Application found.")

        if self.darkCheckBox.isChecked():
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        else:
            app.setStyleSheet("")

