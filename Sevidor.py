import socket

import select

# Configurações do servidor

HOST = 'localhost'  # Endereço IP do servidor

PORT = 2009  # Porta para escutar as conexões

# Cria um socket TCP/IP

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define as opções do socket para permitir a reutilização do endereço do servidor

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Liga o socket ao endereço e porta especificados

server_socket.bind((HOST, PORT))

# Coloca o socket em modo de escuta

server_socket.listen(10)

# Lista de sockets de entrada (incluindo o socket servidor)

sockets = [server_socket]

print("Servidor iniciado em {}:{}".format(HOST, PORT))

while True:

    # Aguarda até que haja um socket pronto para leitura, gravação ou erro

    # O segundo argumento é uma lista de sockets para monitorar para leitura

    # O terceiro argumento é uma lista de sockets para monitorar para gravação

    # O quarto argumento é uma lista de sockets para monitorar para erros

    readable, _, _ = select.select(sockets, [], [])

    for sock in readable:

        if sock == server_socket:

            # Novas conexões de entrada

            client_socket, client_address = server_socket.accept()

            sockets.append(client_socket)

            print("Nova conexão estabelecida: {}".format(client_address))

        else:

            # Dados recebidos de um cliente

            data = sock.recv(1024)

            if data:

                # Encaminha a mensagem recebida para todos os clientes conectados (exceto o remetente original)

                for client in sockets:

                    if client != server_socket and client != sock:

                        client.send(data)

            else:

                # Cliente desconectado

                print("Cliente desconectado: {}".format(sock.getpeername()))

                sock.close()

                sockets.remove(sock)
