const net = require('net');

// Porta em que o servidor irá ouvir as conexões

const PORT = 8080;

// Criação do servidor

const servidor = net.createServer((socket) => {

  console.log('Cliente conectado');

  // Evento de recebimento de dados do cliente

  socket.on('data', (dados) => {

    console.log('Dados recebidos do cliente:', dados.toString());

    // Envia uma resposta ao cliente

    const resposta = 'Olá, cliente!';

    socket.write(resposta);

  });

  // Evento de fechamento da conexão

  socket.on('close', () => {

    console.log('Cliente desconectado');

  });

});

// Inicia o servidor e faz ele ouvir na porta especificada

servidor.listen(PORT, () => {

  console.log('Servidor aguardando conexões...');

});
