# Do Not Change FROM Use Lavan DockerFile
# MajesteUserBot - ŞakirBey1
FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/MacroKeke/MajesteUserBot /root/MajesteUserBot
WORKDIR /root/MajesteUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
