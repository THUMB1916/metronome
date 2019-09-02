import wave
import pygame
import os


class Metronome:
    def __init__(self):
        self.tempo = 120
        self.customized = False

        # fields for standard beats
        self.time_signature = 4
        self.division = 1
        self.first_beat_accent = True

        # fields for customized beats
        self.beat_definition = []

        self.total_time = 60
        self.filename_first_beep = ''
        self.filename_beep = ''
        self.filename_weak_beep = ''
        self.filename_output = ''
        self.sound = None

    def begin(self):
        self.generate_sound()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(self.filename_output)
        self.sound.play(-1)

    def stop(self):
        self.sound.stop()
        os.remove(self.filename_output)

    def generate_sound(self):
        # open input sound files
        f = wave.open(self.filename_beep)
        f_first_beat = wave.open(self.filename_first_beep)
        f_weak = wave.open(self.filename_weak_beep)

        # check the properties
        if f.getparams()[:3] != f_first_beat.getparams()[:3] or f.getparams()[:3] != f_weak.getparams()[:3]:
            return False

        # get the properties
        framerate = f.getframerate()
        nchannels = f.getnchannels()
        sampwidth = f.getsampwidth()

        # open output sound file
        f_out = wave.open(self.filename_output, 'wb')
        f_out.setframerate(framerate)
        f_out.setnchannels(nchannels)
        f_out.setsampwidth(sampwidth)

        nframes_total = int(self.total_time * framerate)
        # output frames
        if self.customized:
            while f_out.getnframes() < nframes_total:
                for beat in self.beat_definition:
                    # calculate relavant frame counts
                    time_per_sub_beat = 60 / (self.tempo * len(beat))
                    nframes_per_sub_beat = int(time_per_sub_beat * framerate)
                    nbytes_per_sub_beat = nframes_per_sub_beat * sampwidth * nchannels

                    time_of_beep = f.getnframes() / framerate
                    time_of_blank = time_per_sub_beat - time_of_beep
                    nframes_of_blank = int(time_of_blank * framerate)
                    nbytes_of_blank = nframes_of_blank * sampwidth * nchannels

                    time_of_beep_first_beat = f_first_beat.getnframes() / framerate
                    time_of_blank_first_beat = time_per_sub_beat - time_of_beep_first_beat
                    nframes_of_blank_first_beat = int(
                        time_of_blank_first_beat * framerate)
                    nbytes_of_blank_first_beat = nframes_of_blank_first_beat * sampwidth * nchannels

                    time_of_beep_weak = f_weak.getnframes() / framerate
                    time_of_blank_weak = time_per_sub_beat - time_of_beep_weak
                    nframes_of_blank_weak = int(time_of_blank_weak * framerate)
                    nbytes_of_blank_weak = nframes_of_blank_weak * sampwidth * nchannels

                    for beep in beat:
                        if beep == 1:
                            self.output_beeps(
                                f_weak, f_out, nbytes_of_blank_weak)
                        elif beep == 2:
                            self.output_beeps(f, f_out, nbytes_of_blank)
                        elif beep == 3:
                            self.output_beeps(
                                f_first_beat, f_out, nbytes_of_blank_first_beat)
                        else:
                            f_out.writeframes(
                                bytes([0 for _ in range(nbytes_per_sub_beat)]))
        else:
            # calculate relavant frame counts
            time_per_sub_beat = 60 / (self.tempo * self.division)
            nframes_per_sub_beat = int(time_per_sub_beat * framerate)
            nbytes_per_sub_beat = nframes_per_sub_beat * sampwidth * nchannels

            time_of_beep = f.getnframes() / framerate
            time_of_blank = time_per_sub_beat - time_of_beep
            nframes_of_blank = int(time_of_blank * framerate)
            nbytes_of_blank = nframes_of_blank * sampwidth * nchannels

            time_of_beep_first_beat = f_first_beat.getnframes() / framerate
            time_of_blank_first_beat = time_per_sub_beat - time_of_beep_first_beat
            nframes_of_blank_first_beat = int(
                time_of_blank_first_beat * framerate)
            nbytes_of_blank_first_beat = nframes_of_blank_first_beat * sampwidth * nchannels

            time_of_beep_weak = f_weak.getnframes() / framerate
            time_of_blank_weak = time_per_sub_beat - time_of_beep_weak
            nframes_of_blank_weak = int(time_of_blank_weak * framerate)
            nbytes_of_blank_weak = nframes_of_blank_weak * sampwidth * nchannels

            while f_out.getnframes() < nframes_total:
                # output first beat
                if self.first_beat_accent:
                    self.output_beeps(f_first_beat, f_out,
                                      nbytes_of_blank_first_beat)
                else:
                    self.output_beeps(f, f_out, nbytes_of_blank)

                # output weak sub beats
                self.output_beeps(
                    f_weak, f_out, nbytes_of_blank_weak, self.division - 1)

                # output normal beats
                for _ in range(self.time_signature - 1):
                    self.output_beeps(f, f_out, nbytes_of_blank)
                    self.output_beeps(
                        f_weak, f_out, nbytes_of_blank_weak, self.division - 1)

        f_out.close()

    def output_beeps(self, f_in, f_out, nbytes_of_blank, n=1):
        for _ in range(n):
            f_out.writeframes(f_in.readframes(f_in.getnframes()))
            f_out.writeframes(bytes([0 for _ in range(nbytes_of_blank)]))
            f_in.rewind()
