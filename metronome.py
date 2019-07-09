import wave
import pygame
import os


class Metronome:
    def __init__(self):
        self.beat = 120
        self.time_signature = 4
        self.division = 1
        self.total_time = 60
        self.filename_first_beep = ''
        self.filename_beep = ''
        self.filename_weak_beep = ''
        self.filename_output = ''
        self.first_beat_accent = True
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
        output = wave.open(self.filename_output, 'wb')
        output.setframerate(framerate)
        output.setnchannels(nchannels)
        output.setsampwidth(sampwidth)

        # calculate relavant frame counts
        time_per_sub_beat = 60 / (self.beat * self.division)
        time_of_beep = f.getnframes() / framerate
        time_of_blank = time_per_sub_beat - time_of_beep
        nframes_of_blank = int(time_of_blank * framerate)
        nframes_total = int(self.total_time * framerate)

        time_of_beep_first_beat = f_first_beat.getnframes() / framerate
        time_of_blank_first_beat = time_per_sub_beat - time_of_beep_first_beat
        nframes_of_blank_first_beat = int(time_of_blank_first_beat * framerate)

        time_of_beep_weak = f_weak.getnframes() / framerate
        time_of_blank_weak = time_per_sub_beat - time_of_beep_weak
        nframes_of_blank_weak = int(time_of_blank_weak * framerate)

        # output frames
        frame_count = 0
        while frame_count < nframes_total:
            # output first beat
            if self.first_beat_accent:
                output.writeframes(f_first_beat.readframes(f_first_beat.getnframes()))
                output.writeframes(bytes([0 for _ in range(nframes_of_blank_first_beat * sampwidth * nchannels)]))
                f_first_beat.rewind()
                frame_count += f_first_beat.getnframes() + nframes_of_blank_first_beat
            else: 
                output.writeframes(f.readframes(f.getnframes()))
                output.writeframes(bytes([0 for _ in range(nframes_of_blank * sampwidth * nchannels)]))
                f.rewind()
                frame_count += f.getnframes() + nframes_of_blank

            # output weak beats
            for _ in range(self.division - 1):
                output.writeframes(f_weak.readframes(f_weak.getnframes()))
                output.writeframes(bytes([0 for _ in range(nframes_of_blank_weak * sampwidth * nchannels)]))
                f_weak.rewind()
                frame_count += f_weak.getnframes() + nframes_of_blank_weak

            # output normal beats
            for _ in range(self.time_signature - 1):
                output.writeframes(f.readframes(f.getnframes()))
                output.writeframes(bytes([0 for _ in range(nframes_of_blank * sampwidth * nchannels)]))
                f.rewind()
                frame_count += f.getnframes() + nframes_of_blank

                # output weak beats
                for _ in range(self.division - 1):
                    output.writeframes(f_weak.readframes(f_weak.getnframes()))
                    output.writeframes(bytes([0 for _ in range(nframes_of_blank_weak * sampwidth * nchannels)]))
                    f_weak.rewind()
                    frame_count += f_weak.getnframes() + nframes_of_blank_weak

        output.close()


if __name__ == '__main__':
    metronome = Metronome()
    metronome.begin()
    import time
    time.sleep(2)
    metronome.stop()
    time.sleep(2)
    metronome.begin()
    time.sleep(10)
