from pytube import YouTube, Playlist
import ffmpeg
import os

class Mytube():
    
    def __init__(self):
        self._diretorioVideo = os.getcwd()
        self._diretorioAudio = os.getcwd()
        self._diretorioFinal = self.verificaDiretorioFinal()
        self._yt = None 
        self._tituloFormato = ''

    @property
    def diretorioVideo(self):
        return self._diretorioVideo
    
    @diretorioVideo.setter
    def diretorioVideo(self, diretorio):
        self._diretorioVideo = diretorio
    
    @property
    def diretorioAudio(self):
        return self._diretorioAudio
    
    @diretorioAudio.setter
    def diretorioAudio(self, diretorio):
        self._diretorioAudio = diretorio
    
    @property
    def diretorioFinal(self):
        return self._diretorioFinal
    
    @diretorioFinal.setter
    def diretorioFinal(self, diretorio):
        self._diretorioFinal = diretorio

    @property
    def yt(self):
        return self._yt
    
    @yt.setter
    def yt(self, link):
        self._yt = link

    @property
    def tituloFormato(self):
        return self._tituloFormato
    
    @tituloFormato.setter
    def tituloFormato(self, titulo):
        self._tituloFormato = titulo

    def informacoesVideo(self, link):
        self.yt = YouTube(link)
        self.tituloFormato = self.yt.title + ".mp4"
        if self.yt.length >= 3600:
            hr = self.yt.length // 3600
            min = (self.yt.length - hr * 3600) // 60
            seg = self.yt.length - (min * 60 + hr * 3600)
        else:
            hr = 00
            min = self.yt.length // 60
            seg = self.yt.length - min * 60 
        return (f"\nTítulo do video: {self.yt.title}\n"
                f"Duração do vídeo: {hr}:{min}:{seg}")

    def qualidadesVideo(self):
        qualidades = ("\nQualidades disponíveis para download:")
        if self.yt.streams.filter(res="1080p"):
            qualidades += "\n1080p        "
        if self.yt.streams.filter(res="720p"):
            qualidades += "720p"
        if self.yt.streams.filter(res="480p"):
            qualidades += "\n480p        "
        if self.yt.streams.filter(res="360p"):
            qualidades += "360p"
        if self.yt.streams.filter(res="240p"):
            qualidades += "\n240p        "
        if self.yt.streams.filter(res="144p"):
            qualidades += "144p"
        return qualidades

    def verificaDiretorioFinal(self):  
        return "/home/will/Downloads/MYtube/VideosFinais/"
        #Fazer a verificação se tem arquivo do diretorio 
        #if os.path.exists("teste.txt"): # verifica se o arquivo existe
            #os.remove("teste.txt")
        pass
        
    def baixar1080(self):
        try:
            self.yt.streams.filter(res="1080p").first().download(filename = "video.mp4")
            audio = self.yt.streams.filter(only_audio=True)
            audio[0].download(filename = "audio.mp4")
            video_stream = ffmpeg.input('{}/video.mp4'.fomat(self.diretorioVideo))
            audio_stream = ffmpeg.input('{}/audio.mp4'.frmat(self.diretorioAudio))
            ffmpeg.output(audio_stream, video_stream, "{}/{}".format(self.diretorioFinal, self.tituloFormato)).run()
            os.remove("video.mp4")
            os.remove("audio.mp4")
            pass
        except:
            print("Por causa de um erro causado pelo nome do vídeo, o mesmo será baixado em 720p.")
            self.baixar720()

    def baixar720(self):
        self.yt.streams.filter(res="720p").first().download(self.diretorioFinal)

    def baixar480(self):
        try:
            self.yt.streams.filter(res="480p").first().download(filename = "video.mp4")
            audio = self.yt.streams.filter(only_audio=True)
            audio[0].download(filename = "audio.mp4")
            video_stream = ffmpeg.input('{}/video.mp4'.format(self.diretorioVideo))
            audio_stream = ffmpeg.input('{}/audio.mp4'.format(self.diretorioAudio))
            ffmpeg.output(audio_stream, video_stream, "{}/{}".format(self.diretorioFinal, self.tituloFormato)).run()
            os.remove("video.mp4")
            os.remove("audio.mp4")
        except:
            print("Por causa de um erro causado pelo nome do vídeo, o mesmo será baixado em 360p.")
            self.baixar360()

    def baixar360(self):
        self.yt.streams.filter(res="360p").first().download(self.diretorioFinal)

    def baixar240(self):
        try:
            self.yt.streams.filter(res="240p").first().download(filename = "video.mp4")
            audio = self.yt.streams.filter(only_audio=True)
            audio[0].download(filename = "audio.mp4")
            video_stream = ffmpeg.input('{}/video.mp4'.format(self.diretorioVideo))
            audio_stream = ffmpeg.input('{}/audio.mp4'.format(self.diretorioAudio))
            ffmpeg.output(audio_stream, video_stream, "{}/{}".format(self.diretorioFinal, self.tituloFormato)).run()
            os.remove("video.mp4")
            os.remove("audio.mp4")
        except:
            print("Por causa de um erro causado pelo nome do vídeo, o mesmo será baixado em 360p.")
            self.baixar360()

    def baixar144(self):
        try:
            self.yt.streams.filter(res="144p").first().download(filename = "video.mp4")
            audio = self.yt.streams.filter(only_audio=True)
            audio[0].download(filename = "audio.mp4")
            video_stream = ffmpeg.input('{}/video.mp4'.format(self.diretorioVideo))
            audio_stream = ffmpeg.input('{}/audio.mp4'.format(self.diretorioAudio))
            ffmpeg.output(audio_stream, video_stream, "{}/{}".format(self.diretorioFinal, self.tituloFormato)).run()
            os.remove("video.mp4")
            os.remove("audio.mp4")
        except:
            print("Por causa de um erro causado pelo nome do vídeo, o mesmo será baixado em 360p.")
            self.baixar360()