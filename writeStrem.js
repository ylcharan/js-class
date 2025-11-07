const fs = require("fs");

const writeStream = fs.createWriteStream("output.txt");

writeStream.write("Hello Node.js Streams!\n");
writeStream.write("Write more data...");
writeStream.end("Done Writing.");

writeStream.on("finish", () => {
  console.log("All data written successfully");
});

writeStream.on("error", (err) => {
  console.error("Error: ", err);
});
