import socket

# Endereço IP e porta do servidor

HOST = '127.0.0.1'

PORT = 8080

# Criação do socket TCP/IP

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço IP e porta

servidor.bind((HOST, PORT))

# Ouve por conexões entrantes

servidor.listen()

print('Servidor aguardando conexões...')

# Aceita uma conexão

conexao, endereco = servidor.accept()

print('Conexão estabelecida com', endereco)

# Recebe dados do cliente

dados = conexao.recv(1024)

# Decodifica os dados recebidos

dados_decodificados = dados.decode()

print('Dados recebidos do cliente:', dados_decodificados)

# Envia uma resposta ao cliente

resposta = 'Olá, cliente!'

conexao.send(resposta.encode())

# Fecha a conexão

conexao.close()
