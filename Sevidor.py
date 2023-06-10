import socket

import threading

# Endereço IP e porta do servidor

HOST = '127.0.0.1'

PORT = 8080

# Função que será executada em cada thread

def handle_client(conexao, endereco):

    print('Conexão estabelecida com', endereco)

    while True:

        # Recebe dados do cliente

        dados = conexao.recv(1024)

        if not dados:

            break

        # Decodifica os dados recebidos

        dados_decodificados = dados.decode()

        print('Dados recebidos do cliente:', dados_decodificados)

        # Envia uma resposta ao cliente

        resposta = 'Olá, cliente!'

        conexao.send(resposta.encode())

    # Fecha a conexão

    conexao.close()

    print('Conexão encerrada com', endereco)

# Criação do socket TCP/IP

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço IP e porta

servidor.bind((HOST, PORT))

# Ouve por conexões entrantes

servidor.listen()

print('Servidor aguardando conexões...')

while True:

    # Aceita uma conexão

    conexao, endereco = servidor.accept()

    # Cria uma nova thread para lidar com a conexão

    thread = threading.Thread(target=handle_client, args=(conexao, endereco))

    thread.start()
