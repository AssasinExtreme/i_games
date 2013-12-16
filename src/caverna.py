"""
############################################################
Caverna - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/11/04
:Status: This is a "work in progress"
:Revision: 0.1.3
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

Caverna é um jogo de aventuras em uma caverna.
"""
CAVEX = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernax.jpg"
CAVEZ = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernaz.jpg"
CAMARA = [0, 1, 2, 3]
TUNEIS = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (1, 3)]


class Caverna:
    """Uma caverna com cameras tuneis e habitantes. :ref:`caverna`
"""
    def __init__(self, gui):
        """Initializes builder and gui. """
        self.doc = gui.DOC
        self.html = gui.HTML
        self.camera = {}
        self.tunel = {}
        self.heroi = None
        self.main = self.doc['main']
        self.camara = None
        self.sala = None
        self.esconde = self.html.DIV()

    def movimenta(self, sala):
        self.esconde <= self.sala.div
        self.main <= sala.div
        self.sala = sala

    def cria_caverna(self):
        """Cria a caverna e suas partes."""
        self.camara = {
            'camara_%d' % a:
            Camara(self.html, "camara_%d" % a, self).cria_camara() for a in CAMARA
        }
        # criando uma colecao de tuneis
        self.sala = self.camara['camara_0']
        self.main <= self.sala

        self.tunel = {
            'tunel_%d_%d' % a:
            Tunel(self.html, "tunel_%d_%d" % a, self.camara, self.camara['camara_0'].passagem, self).cria_tunel()
            for a in TUNEIS
        }
        return self


class Camara:
    """Uma camara de caverna com tuneis e habitantes. :ref:'camara'
"""
    def __init__(self, html, nome, lugar):
        """Inicia a camara. """
        self.html, self.nome, self.lugar = html, nome, lugar
        self.passagem = self.div = None
        self.tunel = ()

    def cria_camara(self):
        """Cria a camara e suas partes."""
        self.div = self.html. DIV(Id=self.nome)
        self.passagem = self.html.DIV(Id='passa_'+self.nome)
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEX
        self.div.style.width = 1000
        self.div.style.height = 800
        self.div.text = "Caverna do Vinicius"
        self.div <= self.passagem
        self.lugar.esconde <= self.div
        return self


class Tunel:
    """Um tunel da caverna que liga camaras. :ref:'tunel'
"""
    def __init__(self, html, nome, lugar, saida, caverna):
        """Inicia o tunel. """
        self.html, self.nome, self.caverna = html, nome, caverna
        self.lugar, self.saida = lugar, saida
        self.entrada_camara = self.entrada = self.passagem = self.div = None
        self.camara = ()

    def movimenta(self, ev):
        print('movimenta', ev.target.Id, self.div)
        self.caverna.movimenta(self)

    def sai_tunel(self, ev):
        print(ev.target.Id, self.lugar)
        self.caverna.movimenta(self.lugar)

    def cria_saida(self):
        """Cria uma saida deste tunel"""
        estilo = dict(
            width="50%", height=300, Float='left')
        self.entrada_camara = self.html.DIV(
            Id='entra_'+self.nome, style=estilo
        )
        self.entrada_camara.onclick = self.sai_tunel
        self.passagem <= self.entrada_camara

    def cria_tunel(self):
        """Cria o tunel e suas partes."""
        self.div = self.html. DIV(Id=self.nome)
        self.passagem = self.html.DIV(Id='passa_'+self.nome)
        estilo = dict(
            width="33.33%", height=300, Float='left')
        self.entrada = self.html.DIV(
            Id='entra_'+self.nome, style=estilo
        )
        self.entrada.onclick = self.movimenta
        self.saida <= self.entrada
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEZ
        self.div.style.width = 1000
        self.div.style.height = 800
        self.div.text = "Caverna d Vinicius"
        self.div <= self.passagem
        self.cria_saida()
        return self


def main(gui):
    print('Caverna 0.1.0')
    Caverna(gui).cria_caverna()