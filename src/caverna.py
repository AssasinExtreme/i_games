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

    def cria_caverna(self):
        """Cria a caverna e suas partes."""
        self.main.style.backgroundSize = 'cover'
        self.main.style.backgroundImage = 'url(%s)' % CAVEX
        self.main.style.width = 1000
        self.main.style.height = 800

        tunel = self .html.DIV()
        tunel.setAttribute ('style', 'height:700; width: 33.33%; float;')
        self.main <= tunel
        tunel = self .html.DIV()
        tunel.setAttribute ('style', 'height:700; width: 33.33%; float;')
        self.main <= tunel
        tunel = self .html.DIV()
        tunel.setAttribute ('style', 'height:700; width: 33.33%; float;')
        self.main <= tunel
        return self

def main(gui):
    print('Caverna 0.1.0')
    caverna = Caverna(gui).cria_caverna()
