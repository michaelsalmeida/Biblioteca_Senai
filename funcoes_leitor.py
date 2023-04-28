from funcoes_internas import *

def obter_matricula():
    import cv2
    from pyzbar.pyzbar import decode

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cv2.namedWindow('Barcode reader', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Barcode reader', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    verificacao = [] # lista que receberá os números lidos pelo código de barras.

    while True:
        # Leia um frame da câmera
        ret, frame = cap.read()

        # Detecte códigos de barras no frame
        barcodes = decode(frame)

        # # Exiba o número do código de barras na tela
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            if barcode_data != None:
                verificacao.append(barcode_data)

        # Verifica se os valores lidos estão consistentes.
        if len(verificacao) == 5:
            if verificacao[0] == verificacao[1] == verificacao[2] == verificacao[3] == verificacao[4]:

                if len(str(barcode_data)) == 8:
                    cap.release()
                    cv2.destroyAllWindows() # condicional que verifica se o valor lido é correspondente ao padrão de matricula.
                    return int(barcode_data)
                else:
                    print('Código de barras inválido. Tente novamente.')
                    verificacao = []

            else:
                verificacao = []
                print('Erro ao ler o codigo de barras, pode não estao legivel o suficiente. Por favor, tente novamente.')

        # Exiba o frame com o número do código de barras
        cv2.imshow('Barcode reader', frame)

        # Pare o loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exitt()
            break

        elif cv2.waitKey(1) & 0xFF == ord('ç'):
            break

