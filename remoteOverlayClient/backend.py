import pyNetworking as nw

@nw.recvFunction(str)
def recvDebug(message):
    print(message)

@nw.sendFunction(str, bytes)
def sendFile(path):
    fileName = path.split("/")[-1]
    file = open(path, "rb")
    content = file.read()
    file.close()
    return fileName, content

@nw.writeable(str)
class Texture:
    def write(filename):
        return (filename,)

@nw.sendFunction(nw.Connection, Texture)
def sendReloadTexture(filename):
    return (filename,)

@nw.writeable(str)
class Shader:
    def write(filename):
        return (filename,)

@nw.sendFunction(nw.Connection, Shader)
def sendReloadShader(filename):
    return (filename,)

@nw.withId(Shader, [float], [(str, Texture)])
class ClientMesh:
    def __init__(self, shader, data = None, uniforms = None, textures = None):
        self.shader = shader
        self.data = data or []
        self.textures = textures or {}
        self.uniforms = uniforms or {}
        self.onServer = False

    def sendInit(self):
        self.onServer = True
        return self.shader, self.data, list(self.textures.items())

    @nw.sendFunction(nw.Self, Shader, [float], [(str, Texture)])
    def sendUpdate(self):
        return self, self.shader, self.data, list(self.textures)

    @nw.sendFunction(nw.Self, Shader)
    def sendSelectShader(self, shader):
        return self, shader

    @nw.sendFunction(nw.Self, str, Texture)
    def sendUniformTexture(self, name, texture):
        return self, name, texture

    @nw.sendFunction(nw.Self, str, float)
    def sendUniform1f(self, name, *xs):
        return self, name, *xs

    @nw.sendFunction(nw.Self, str, float, float)
    def sendUniform2f(self, name, *xs):
        return self, name, *xs

    @nw.sendFunction(nw.Self, str, float, float, float)
    def sendUniform3f(self, name, *xs):
        return self, name, *xs

    @nw.sendFunction(nw.Self, str, float, float, float, float)
    def sendUniform4f(self, name, *xs):
        return self, name, *xs

    @nw.sendFunction(nw.Self, str, int)
    def sendUniform1i(self, name, *xs):
        return self, name, *xs

    @nw.sendFunction(nw.Self, str, int, int)
    def sendUniform2i(self, name, *xs):
        return self, name, *xs

    @nw.sendFunction(nw.Self, str, int, int, int)
    def sendUniform3i(self, name, *xs):
        return self, name, *xs

    @nw.sendFunction(nw.Self, str, int, int, int, int)
    def sendUniform4i(self, name, *xs):
        return self, name, *xs

