const net = require('net');
const WebSocket = require('ws');

// TCP server for incoming Pd messages (from Pd's netsend)
const pdServer = net.createServer();
let pdSocket = null;

pdServer.on('connection', (socket) => {
  console.log('Pure Data connected via TCP (netsend)');
  pdSocket = socket;

  socket.on('data', (data) => {
    console.log('From Pd:', data.toString());
    wss.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(data.toString());
      }
    });
  });

  socket.on('end', () => {
    console.log('Pure Data disconnected');
    pdSocket = null;
  });
});

pdServer.listen(9000, () => console.log('Listening for Pd (netsend) on TCP port 9000'));

// TCP client to send messages back to Pd (netreceive on port 9001)
const pdOut = new net.Socket();
pdOut.connect(9001, 'localhost', () => {
  console.log('Connected to Pd receive socket (netreceive 9001)');
});

// WebSocket server for browser
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('Browser connected via WebSocket');

  ws.on('message', (msg) => {
    console.log('From Browser:', msg);
    if (pdSocket) pdSocket.write(msg + '\n'); // to netsend side
    pdOut.write('fromBrowser ' + msg + '\n'); // to netreceive side
  });
});
