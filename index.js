const content = require('fs').readFileSync(__dirname + '/test.html', 'utf8');
const {spawn} = require('child_process');
var dataToSend;
 // spawn new child process to call the python script
 const python = spawn('python', ['-u', 'Untitled-1.py']);
 // collect data from script
 
// python.stdout.on('data', function (data) {
//   console.log('Pipe data from python script ...');
   
//   dataToSend = data.toString();
// });
const httpServer = require('http').createServer((req, res) => {
  // serve the index.html file
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('Content-Length', Buffer.byteLength(content));
  res.end(content);
});

const io = require('socket.io')(httpServer);

io.on('connection', socket => {

    setInterval(() => {
      socket.emit('a', dataToSend);
      python.stdout.on('data', function (data) {
        
         
        dataToSend = data.toString();
      });
    }, 100);
  });

httpServer.listen(3000, () => {
  console.log('go to http://localhost:3000');
});