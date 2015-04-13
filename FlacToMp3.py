import os.path
from MP3Info import Mp3Info
from AudioUtil import AudioUtil
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
# Mutagen!!!

def main():
    print "Flac to mp3 converter."
    CheckForNecessaryApplications()
    GatherData()
    Convert()


def CheckForNecessaryApplications():
    allAppsAreInstalled = True
    print "Checking for applications:"
    if ApplicationsIsCallable("lame") is False:
        allAppsAreInstalled = False

    if ApplicationsIsCallable("flac") is False:
        allAppsAreInstalled = False

    if ApplicationsIsCallable("id3v2") is False:
        allAppsAreInstalled = False

    assert allAppsAreInstalled is True


def GatherData():
    Mp3Properties.SetArtFileName()
    assert Mp3Properties.CheckIfArtFileExist() is True


def ApplicationsIsCallable(applicationName):
    print "Checking if " + applicationName + " exist."
    for currentDirectory in os.environ['PATH'].split(':'):
        appNameWithPath = os.path.join(currentDirectory, applicationName)
        if os.path.exists(appNameWithPath):
            return True
    print "Please install " + applicationName + ", or add it to PATH."
    return False


def Convert():
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    dirs = os.listdir(currentDirectory)
    for currentFile in dirs:
        if ".flac" in currentFile:
            fileInfo=GetTagsFromFlac(currentFile)
            #FlacToWave(currentFile)
           # WaveToMp3(fileInfo)
            SetTags(fileInfo)


def GetTagsFromFlac(flacFileName):
    audioFile = FLAC(flacFileName)
    mp3FileInfo = Mp3Info()
    mp3FileInfo.SetArtist(audioFile.get("ARTIST"))
    mp3FileInfo.SetAlbumName(audioFile.get("ALBUM"))
    mp3FileInfo.SetYear(audioFile.get("DATE"))
    mp3FileInfo.SetTitle(audioFile.get("TITLE"))
    mp3FileInfo.SetGenre(audioFile.get("GENRE"))
    mp3FileInfo.SetTrackIndex(audioFile.get("TRACKNUMBER"))
    mp3FileName = ConstructFileName(mp3FileInfo)
    mp3FileInfo.SetFileName(mp3FileName)
    return mp3FileInfo

def ConstructFileName(mp3FileInfo):
    if mp3FileInfo.GetTrackIndex() > 9:
        return str(mp3FileInfo.GetTrackIndex()) + " " + mp3FileInfo.GetTitle() + ".mp3"
    else:
        return "0" + str(mp3FileInfo.GetTrackIndex()) + " " + mp3FileInfo.GetTitle() + ".mp3"


def FlacToWave(flacFileName):
    AudioUtil.FlacToWave(flacFileName,"temp.wav")

def WaveToMp3(mp3FileInfo):
    AudioUtil.WaveToMp3(
        Mp3Properties.s_mp3BitRate,
        Mp3Properties.s_mp3SampleRate,
        mp3FileInfo.GetFileName(),
        "temp.wav")

def SetTags(mp3FileInfo):
    mp3FileInfo.WriteTags()


class Mp3Properties:
    s_artFileName = ""
    s_mp3BitRate = 320
    s_mp3SampleRate = 44.1
    s_trackCount = 0

    @staticmethod
    def SetArtFileName(artFileName="Front.jpg"):
        Mp3Properties.s_artFileName = artFileName

    @staticmethod
    def CheckIfArtFileExist():
        return os.path.exists(Mp3Properties.s_artFileName)



if __name__ == "__main__":
    main()
