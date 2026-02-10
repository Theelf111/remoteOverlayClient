import pyNetworking as nw

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

@nw.sendFunction(Texture)
def sendReloadTexture(filename):
    return (filename,)

@nw.writeable(str)
class Shader:
    def write(filename):
        return (filename,)

@nw.sendFunction(Shader)
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

@nw.sendFunction(Shader, [float], [(str, Texture)], methodOf = ClientMesh)
def sendUpdate(self):
    return self, self.shader, self.data, list(self.textures)

@nw.sendFunction(Shader, methodOf = ClientMesh)
def sendSelectShader(self, shader):
    return self, shader

@nw.sendFunction(str, Texture, methodOf = ClientMesh)
def sendUniformTexture(self, name, texture):
    return self, name, texture

@nw.sendFunction(str, float, methodOf = ClientMesh)
def sendUniform1f(self, name, *xs):
    return self, name, *xs

@nw.sendFunction(str, float, float, methodOf = ClientMesh)
def sendUniform2f(self, name, *xs):
    return self, name, *xs

@nw.sendFunction(str, float, float, float, methodOf = ClientMesh)
def sendUniform3f(self, name, *xs):
    return self, name, *xs

@nw.sendFunction(str, float, float, float, float, methodOf = ClientMesh)
def sendUniform4f(self, name, *xs):
    return self, name, *xs

@nw.sendFunction(str, int, methodOf = ClientMesh)
def sendUniform1i(self, name, *xs):
    return self, name, *xs

@nw.sendFunction(str, int, int, methodOf = ClientMesh)
def sendUniform2i(self, name, *xs):
    return self, name, *xs

@nw.sendFunction(str, int, int, int, methodOf = ClientMesh)
def sendUniform3i(self, name, *xs):
    return self, name, *xs

@nw.sendFunction(str, int, int, int, int, methodOf = ClientMesh)
def sendUniform4i(self, name, *xs):
    return self, name, *xs

