""" Configuração do pygame """

import sys
import pygame as pg


class Engine:
    """ Inicializa o pygame """

    def __init__(self, size: tuple[int, int]):
        pg.init()
        pg.display.set_caption("Fighter")

        self.__framerate = 60
        self.__screen = pg.display.set_mode(size, 0, 32)
        self.__clock = pg.time.Clock()

    def tick(self) -> float:
        """ Atualiza o clock e retorna o delta time """
        return self.__clock.tick(self.__framerate) * 0.001 * 60

    def draw(self, surface: pg.Surface):
        """ Desenha a superfície para a tela """
        self.__screen.blit(surface, (0, 0))


class InputManager:
    """
    Lida com os eventos

    O dicionário de mappings possui a estrutura {"tecla": "ação"}
    As teclas para capturar o click esquerdo e direito são (1, 3)
    """

    def __init__(self, mappings: dict[int, str]):
        self.__mappings = mappings
        self.__mouse = (0, 0)
        self.__pressed: set[str] = set()
        self.__just_pressed: set[str] = set()

    @property
    def pressed(self):
        """ Retorna as teclas pressionadas """
        return self.__pressed

    @property
    def just_pressed(self):
        """ Retorna as teclas pressionadas neste frame """
        return self.__just_pressed

    @property
    def mouse(self):
        """ Retorna a posição do código """
        return self.__mouse

    def update(self):
        """ Atualiza o estado dos inputs """
        self.__mouse = pg.mouse.get_pos()
        self.__just_pressed.clear()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type in (pg.KEYDOWN, pg.KEYUP):
                if event.key in self.__mappings:
                    action = self.__mappings[event.key]
                    if event.type == pg.KEYDOWN:
                        self.__pressed.add(action)
                        self.__just_pressed.add(action)
                    elif action in self.__pressed:
                        self.__pressed.remove(action)
            elif (
                event.type in (pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP)
                and event.button in self.__mappings
            ):
                action = self.__mappings[event.button]
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.__pressed.add(action)
                    self.__just_pressed.add(action)
                elif action in self.__pressed:
                    self.__pressed.remove(action)
