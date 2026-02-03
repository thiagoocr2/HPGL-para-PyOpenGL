from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --- Passo 01: Configurações de Arquivo ---
caminho_arquivo = '/Users/thiago/Downloads/bottom_rafael_espelhada.txt'

segmentos = [] # Lista de listas para separar os traços (PU/PD)
caminho_atual = []

# --- Passo 02: Lógica de Leitura (Igual ao seu, mas separando traços) ---
def carregar_dados():
    global segmentos, caminho_atual
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("PU"):
                    if caminho_atual:
                        segmentos.append(caminho_atual)
                    caminho_atual = []
                elif linha.startswith("PA"):
                    coords = linha.replace("PA", "").replace(";", "").strip()
                    if coords:
                        x, y = map(float, coords.split(","))
                        caminho_atual.append((x, y))
            if caminho_atual:
                segmentos.append(caminho_atual)
    except FileNotFoundError:
        print("Arquivo não encontrado!")

# --- Passo 03: Funções do OpenGL (Estilo C) ---
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) # Fundo preto
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # Define a área de visualização (Janela de coordenadas)
    # Aqui você ajusta o "zoom". Se o desenho sumir, aumente esses valores.
    # gluOrtho2D(min_x, max_x, min_y, max_y)
    gluOrtho2D(0, 5000, 0, 5000) 

def desenhar():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) # Cor branca para as linhas
    
    for traço in segmentos:
        if len(traço) > 1:
            glBegin(GL_LINE_STRIP)
            for x, y in traço:
                glVertex2f(x, y)
            glEnd()
    
    glFlush() # Garante a execução dos comandos

# --- Passo 04: Main (Ciclo de vida do GLUT) ---
def main():
    carregar_dados()
    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Visualizador HPGL - PyOpenGL")
    
    init()
    glutDisplayFunc(desenhar)
    glutMainLoop()

if __name__ == "__main__":
    main()