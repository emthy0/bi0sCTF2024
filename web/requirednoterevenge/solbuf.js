const protobuf = require('protobufjs');

// Define the Protocol Buffers content
const protoDefinition = `
syntax = "proto3";
message Settings {
  // Add your settings fields here
  int32 userId = 1;
  string userName = 2;
  repeated string email = 3;
}`;

// Load the Protocol Buffers definition
const root = protobuf.parse(protoDefinition).root;
const Settings = root.lookupType("Settings");

// Create an instance of the message
const settingsMessage = {
  userId: 123,
  userName: "John",
  email: ["john@example.com", "john.doe@example.com"]
};

// Serialize the message to binary format
const buffer = Settings.encode(settingsMessage).finish();

// Write the serialized content to a file
const fs = require('fs');

fs.writeFileSync('./settings.proto', buffer, 'utf-8');
