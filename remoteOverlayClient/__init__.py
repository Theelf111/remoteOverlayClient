from . import backend
import time

#server = nw.connect(input("ip: "), 25565, "PASSWORD")

server = None
def listen():
    global server
    if server:
        server.close()
    for mesh in Mesh.all.values():
        mesh.onServer = False
    backend.nw.listener(25565, "PASSWORD", 1)
    server = backend.nw.newClients.pop(0)

def pushFile(path):
    backend.sendFile(server, path)
    server.send()

def reloadShader(filename):
    backend.sendReloadShader(server, filename)
    server.send()

class Mesh(backend.ClientMesh):
    def update(self):
        if not self.onServer:
            self.sendInit(server)
        else:
            self.sendUpdate(server)
        for name in self.uniforms:
            value = self.uniforms[name]
            count = len(value)
            valueType = type(value[0])
            if count in range(1, 5) and valueType in (float, int):
                Mesh.__getattribute__(self, "sendUniform" + str(count) + ("f" if valueType == float else "i"))(server, name, *value)
            else:
                print(f"Uniform \"{name}\" with value {value} has invalid type ({count}, {valueType})")
        server.send()

    def setText(self, pos, text, color0 = (0.0, 0, 0, 1), color1 = (1.0, 1, 1, 1)):
        self.data = ()
        x = 0
        y = 0
        for i in range(len(text)):
            if text[i] == "\n":
                x = 0
                y += 1
                continue
            self.data += (pos[0] + x * 9, pos[1] + y * 20, ord(text[i]) - ord(" ") if ord(text[i]) in range(ord(" "), ord("ÿ") + 1) else ord(" "))
            x += 1
        self.uniforms["col0"] = color0
        self.uniforms["col1"] = color1

    def selectShader(self, shader):
        self.shader = shader
        self.sendSelectShader(server, shader)
        server.send()

    def uniformTexture(self, name, texture):
        self.textures[name] = texture
        self.sendUniformTexture(server, name, texture)
        server.send()

    def uniform1f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

    def uniform2f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

    def uniform3f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

    def uniform4f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

    def uniform1i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

    def uniform2i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

    def uniform3i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

    def uniform4i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)
        server.send()

def textMesh(pos, text, color0 = (0.0, 0, 0, 1), color1 = (1.0, 1, 1, 1)):
    mesh = Mesh("builtins:text", None,
                {"charSize" : (9.0, 20)},
                {"tex" : "builtins:font"})
    mesh.setText(pos, text, color0, color1)
    return mesh

listen()
