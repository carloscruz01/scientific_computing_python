def criation_file():
    open(mode="x", file='texto')
    open("texto")
def abertura_arquivo():
    var = open("texto", "r", closefd=True)
    print(var.read())
def abertura_arquivo2():
    def criation_file():
        open(mode="x", file="Text2")
    text2 = open("text2", "r")
    print(text2.read())
    #criation_file()
abertura_arquivo2()
    
