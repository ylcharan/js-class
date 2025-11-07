import http from "http";
import fs from "fs";
// http
//   .createServer((req, res) => {
//     // res.setHeader("Content-Type", "text/html");
//     res.writeHead(200, { "Content-type": "text/html" });
//     res.write("<i>Hello World</i>");
//     console.log("req");
//     res.end("hello world");

//     if (res.writable == true) {
//       console.log("Writable status is: ", res.writable);
//     }
//     if (res.writableEnded == true) {
//       console.log("writable status is: ", res.writableEnded);
//     }
//   })
//   .listen(9090);

const server = http.createServer((req, res) => {
  if (req.url == "/") {
    fs.readFile("./index.html", "utf-8", (err, data) => {
      if (err) {
        res.write("error displaying page");
        res.end();
      } else {
        res.setHeader("Content-type", "text/html");
        res.write(data);
        res.end();
      }
    });
  }
});

server.listen(9090);
