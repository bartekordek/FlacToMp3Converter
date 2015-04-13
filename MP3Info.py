from mutagen.easyid3 import EasyID3
from ShellHandler import ShellOp
import mutagen

class Mp3Info:
    tagList = s_GetTagList()
    def __init__(self):
        self.m_fileName = ""
        self.m_title = ""
        self.m_artist = ""
        self.m_albumName = ""
        self.m_genre = ""
        self.m_year = 0
        self.m_trackIndex = 0
        self.m_tracksCount = 0
        self.m_cdIndex = 0
        self.m_cdsCount = 0

    def SetFileName(self, fileName):
        self.m_fileName = fileName

    def GetFileName(self):
        return self.m_fileName

    def SetTitle(self, title):
        self.m_title = Mp3Info.m_DecodeToUtf8(title)

    def GetTitle(self):
        return self.m_title

    def SetArtist(self, artist):
        self.m_artist = Mp3Info.m_DecodeToUtf8(artist)

    def GetArtist(self):
        return self.m_artist

    def SetAlbumName(self, albumName):
        self.m_albumName = Mp3Info.m_DecodeToUtf8(albumName)

    def GetAlbumName(self):
        return self.m_albumName

    def SetGenre(self, genre):
        self.m_genre = Mp3Info.m_DecodeToUtf8(genre)

    def GetGenre(self):
        return self.m_genre

    def SetYear(self, year):
        self.m_year = int(Mp3Info.m_DecodeToUtf8(year))

    def GetYear(self):
        return self.m_year

    def SetTrackIndex(self, trackIndex):
        self.m_trackIndex = int(Mp3Info.m_DecodeToUtf8(trackIndex))

    def GetTrackIndex(self):
        return self.m_trackIndex

    def SetTracksCount(self, trackCount):
        self.m_tracksCount = int(Mp3Info.m_DecodeToUtf8(trackCount))

    def GetTracksCount(self):
        return self.m_tracksCount

    def SetCdIndex(self, cdIndex):
        self.m_cdIndex = int(Mp3Info.m_DecodeToUtf8(cdIndex))

    def GetCdIndex(self):
        return self.m_cdIndex

    def SetCdsCount(self, cdCount):
        self.m_cdsCount = int(Mp3Info.m_DecodeToUtf8(cdCount))

    def GetCdsCount(self):
        return self.m_cdsCount

    def WriteTags(self):
        tagCommand = "id3v2 "
        ShellOp.ExecuteShellCommand(tagCommand + )

    @staticmethod
    def m_DecodeToUtf8(mutagenList):
        return mutagenList.pop().encode('utf-8')

    @staticmethod
    def s_GetTagList():
        list.append("--song")
        list.append("--track")
        list.append("--artist")
        list.append("--album")
        list.append("--genre")
        list.append("--year")
        list.append("--TPOS")