# HPGL-para-PyOpenGL
## 🎯 Objetivo
Desenvolver uma ferramenta de pré-visualização de arquivos HPGL utilizando Python e PyOpenGL, facilitando a verificação de erros antes da execução física em máquinas do tipo penplotter.

O arquivo HPGL era usado originalmente para impressoras do tipo penplotter. Na FGA (atual FCTE - UnB) uma dessas foi modificada para o desenvolvimento de placas de circuito impresso (pcb). Elas eram lentas, demoradas e por isso faz-se necessário a pré visualização do arquivo a ser impresso.
A pré visualização servirá tanto para garantir que o arquivo a ser enviado está certo como para verificar, caso aconteça, se o erro foi no arquivo ou na execução.
O arquivo de pré visualização chama-se open_hpgl.py e precisa da inserção do endereço do arquivo HPGL nas linhas de código. Além disso, é necessário a instalação da biblioteca PyOpenGL para que ele funcione corretamente. Após a execução ele vai interpretar o código HPGL e gerar um arquivo gráfico representando o que será impresso.
