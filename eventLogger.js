const eventEmitter = require("events");
const emitter = new eventEmitter();
const fs = require("fs");

let count = {
  login: 0,
  logout: 0,
  purchase: 0,
  update: 0,
  delete: 0,
};
