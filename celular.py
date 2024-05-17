class Celular ():
    bateria = 'Infitina'
    tela = '4x3'
    tem_camera = True
    tem_botao = True
    tem_antena = True
    cor = 'Cinza'
    modelo = 'Tijolao'

    def ligacao():
        print('Ligando...')

    def mensagem():
        print('Enviando mensagem...')

    def jogo_cobrinha():
        return('Snake Game')

print(Celular.bateria)
print(Celular.jogo_cobrinha())
