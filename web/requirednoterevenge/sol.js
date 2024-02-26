const express = require('express');
const fs = require('fs');
const protobuf = require('protobufjs');
const glob = require('glob');
const { healthCheck } = require('./bot');
const crypto=require('crypto');
data = [{"title":"string title = 1;string author = 3;}option(a).constructor.prototype.client = 1;message X {optional"},{"author":"optional"}]

let author = data.pop()['author'];

let title = data.pop()['title'];

let protoContents = fs.readFileSync('./settings.proto', 'utf-8').split('\n');

if (author) {
  if (typeof author !== 'string') {
    // return res.status(500).json({ Message: 'Internal server error' });
    return console.log("author not string")
  }
  if (author.length > 86) {
    return console.log("author length err")
  }
  if (!/^[A-Za-z0-9/."\\(){};=]+$/.test(author)) {
    return console.log("author regex err")
  }
  protoContents[5] = `  ${author} string author = 3 [default="user"];`;
}

if (title) {
  if (typeof title !== 'string') {
    return  console.log("title not string")
  }
  if (title.length > 86) {
    return console.log("title length err", title.length)
  }
  if (!/^[A-Za-z0-9/."\\(){};=]+$/.test(title)) {
    return console.log("title regex err")
  }
  protoContents[5] = `  ${author} string author = 3 [default="user"];`;
}