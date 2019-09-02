import json
import os
import sys
import time

import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

import metronome_window
import rhythm_test
from metronome import Metronome


class MetronomeUi(metronome_window.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_80bpm.clicked.connect(self.set_80bpm)
        self.button_100bpm.clicked.connect(self.set_100bpm)
        self.button_120bpm.clicked.connect(self.set_120bpm)
        self.button_inc_bpm.clicked.connect(self.increase_bpm)
        self.button_dec_bpm.clicked.connect(self.decrease_bpm)
        self.slider_bpm.sliderMoved.connect(self.slider_moved)
        self.radio_standard.toggled.connect(self.standard_beat_toggled)
        self.radio_customized.toggled.connect(self.customized_beat_toggled)
        self.button_play.clicked.connect(self.play)
        self.button_test.clicked.connect(self.test)

        self.slider_bpm.setValue(int(self.label_bpm.text()))
        self.radio_standard.toggle()
        self.combo_signature.addItems(
            ['2拍子', '3拍子', '4拍子', '5拍子', '6拍子', '7拍子', '8拍子'])
        self.combo_division.addItems(
            ['1连音', '2连音', '3连音', '4连音', '5连音', '6连音', '7连音', '8连音'])
        self.combo_sound.addItems(os.listdir('res/sound packs'))

        self.metronome = Metronome()
        self.metronome.filename_output = 'output.wav'

        if os.path.isfile('config.json'):
            with open('config.json') as f:
                config = json.load(f)
                self.label_bpm.setText(config.get('tempo'))
                self.radio_customized.setChecked(config.get('customized'))
                self.combo_signature.setCurrentText(
                    config.get('time_signature'))
                self.combo_division.setCurrentText(config.get('division'))
                self.combo_sound.setCurrentText(config.get('sound_pack'))
                self.check_accent.setChecked(config.get('first_beat_accent'))
                self.edit_beat_definition.setText(
                    config.get('beat_definition'))

                self.slider_bpm.setValue(int(self.label_bpm.text()))

        self.rhythm_test_window = None

        self.show()

    def set_80bpm(self):
        self.label_bpm.setText(str(80))
        self.slider_bpm.setValue(int(self.label_bpm.text()))

    def set_100bpm(self):
        self.label_bpm.setText(str(100))
        self.slider_bpm.setValue(int(self.label_bpm.text()))

    def set_120bpm(self):
        self.label_bpm.setText(str(120))
        self.slider_bpm.setValue(int(self.label_bpm.text()))

    def increase_bpm(self):
        if int(self.label_bpm.text()) < 300:
            self.label_bpm.setText(str(int(self.label_bpm.text()) + 1))
            self.slider_bpm.setValue(int(self.label_bpm.text()))

    def decrease_bpm(self):
        if int(self.label_bpm.text()) > 1:
            self.label_bpm.setText(str(int(self.label_bpm.text()) - 1))
            self.slider_bpm.setValue(int(self.label_bpm.text()))

    def slider_moved(self):
        self.label_bpm.setText(str(self.slider_bpm.value()))

    def standard_beat_toggled(self):
        self.combo_division.setEnabled(True)
        self.combo_signature.setEnabled(True)
        self.check_accent.setEnabled(True)
        self.edit_beat_definition.setEnabled(False)

    def customized_beat_toggled(self):
        self.combo_division.setEnabled(False)
        self.combo_signature.setEnabled(False)
        self.check_accent.setEnabled(False)
        self.edit_beat_definition.setEnabled(True)

    def play(self):
        self.metronome.tempo = int(self.label_bpm.text())
        self.metronome.customized = self.radio_customized.isChecked()
        self.metronome.time_signature = int(
            self.combo_signature.currentText()[0])
        self.metronome.division = int(self.combo_division.currentText()[0])
        self.metronome.first_beat_accent = self.check_accent.isChecked()
        self.metronome.beat_definition = []
        for beat in self.edit_beat_definition.text().split('/'):
            self.metronome.beat_definition.append(
                [int(beep) for beep in beat.split()])
        self.metronome.filename_first_beep = 'res/sound packs/' + \
            self.combo_sound.currentText() + '/beep_first_beat.wav'
        self.metronome.filename_beep = 'res/sound packs/' + \
            self.combo_sound.currentText() + '/beep.wav'
        self.metronome.filename_weak_beep = 'res/sound packs/' + \
            self.combo_sound.currentText() + '/beep_weak.wav'
        self.metronome.begin()
        self.button_play.clicked.disconnect(self.play)
        self.button_play.clicked.connect(self.stop)
        self.button_play.setText('停止播放')

        self.button_80bpm.setEnabled(False)
        self.button_100bpm.setEnabled(False)
        self.button_120bpm.setEnabled(False)
        self.button_inc_bpm.setEnabled(False)
        self.button_dec_bpm.setEnabled(False)
        self.slider_bpm.setEnabled(False)
        self.radio_standard.setEnabled(False)
        self.radio_customized.setEnabled(False)
        self.edit_beat_definition.setEnabled(False)
        self.combo_division.setEnabled(False)
        self.combo_signature.setEnabled(False)
        self.combo_sound.setEnabled(False)
        self.check_accent.setEnabled(False)

    def stop(self):
        self.metronome.stop()
        self.button_play.clicked.disconnect(self.stop)
        self.button_play.clicked.connect(self.play)
        self.button_play.setText('播放节拍')

        self.button_80bpm.setEnabled(True)
        self.button_100bpm.setEnabled(True)
        self.button_120bpm.setEnabled(True)
        self.button_inc_bpm.setEnabled(True)
        self.button_dec_bpm.setEnabled(True)
        self.slider_bpm.setEnabled(True)
        self.radio_standard.setEnabled(True)
        self.radio_customized.setEnabled(True)
        self.combo_sound.setEnabled(True)

        if self.radio_standard.isChecked():
            self.standard_beat_toggled()
        else:
            self.customized_beat_toggled()

    def test(self):
        self.rhythm_test_window = RhythmTestUi()

    def closeEvent(self, event):
        config = {}
        config['tempo'] = self.label_bpm.text()
        config['customized'] = self.radio_customized.isChecked()
        config['time_signature'] = self.combo_signature.currentText()
        config['division'] = self.combo_division.currentText()
        config['sound_pack'] = self.combo_sound.currentText()
        config['first_beat_accent'] = self.check_accent.isChecked()
        config['beat_definition'] = self.edit_beat_definition.text()
        with open('config.json', 'w') as f:
            json.dump(config, f)


class RhythmTestUi(rhythm_test.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_rhythm_test_stop.clicked.connect(self.stop_test)

        self.Timer = QTimer()
        self.Timer.timeout.connect(self.timeout)

        self.init_vars()
        self.show()

    def init_vars(self):
        self.start_flag = True
        self.click_time = []
        self.label_timer.setText('0.00s')
        self.label_result.setText('')

    def keyPressEvent(self, event):
        if event.text() == 'g' and self.start_flag:
            if not self.Timer.isActive():
                self.begin_test()
            else:
                self.click_time.append(time.time())

    def begin_test(self):
        self.button_rhythm_test_stop.setEnabled(True)
        self.click_time.append(time.time())
        self.Timer.start(50)

    def stop_test(self):
        self.init_vars()
        self.button_rhythm_test_stop.setText('停止测试')
        self.button_rhythm_test_stop.setEnabled(False)
        self.Timer.stop()

    def timeout(self):
        if (time.time() - self.click_time[0]) >= 20.0:
            self.Timer.stop()
            self.label_timer.setText('{:.2f}s'.format(20.0))
            result = np.array([self.click_time[i] - self.click_time[i - 1]
                               for i in range(1, len(self.click_time))])
            self.label_result.setText('平均值：{}拍\n标准差：{:.3f}s'.format(
                int(round(60 / np.mean(result))), np.std(result)))
            self.button_rhythm_test_stop.setText('重新开始')
            self.start_flag = False
        else:
            self.label_timer.setText('{:.2f}s'.format(
                time.time() - self.click_time[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MetronomeUi()
    sys.exit(app.exec_())
