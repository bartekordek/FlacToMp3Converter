from ShellHandler import ShellOp

class AudioUtil:
    @staticmethod
    def FlacToWave(flacFileName,waveFileName):
        ShellOp.ExecuteShellCommand("flac -f -d \"" + flacFileName + "\" -o " + waveFileName)

    @staticmethod
    def WaveToMp3(mp3BitRate,mp3SampleRate,mp3FileName,waveFileName):
        ShellOp.ExecuteShellCommand(
            "lame --noreplaygain -b " +
            str(mp3BitRate) +
            " -m s -q 0 -s " +
            str(mp3SampleRate) + " " +
            waveFileName +
            " \"" +
            mp3FileName +
            "\""
        )


