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

def reloadshader(filename):
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
            type = str(len(value))+str(type(value))[0]

        server.send()

    def selectShader(self, shader):
        self.shader = shader
        self.sendSelectShader(server, shader)

    def uniformTexture(self, name, texture):
        self.textures[name] = texture
        self.sendUniformTexture(server, name, texture)

    def uniform(self, t, name, *xs):
        Mesh.__getattribute__("uniform"+t)(self, name, *xs)

    def uniform1f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

    def uniform2f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

    def uniform3f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

    def uniform4f(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

    def uniform1i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

    def uniform2i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

    def uniform3i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

    def uniform4i(self, name, *xs):
        self.uniforms[name] = xs
        self.sendUniform1i(server, name, *xs)

listen()
