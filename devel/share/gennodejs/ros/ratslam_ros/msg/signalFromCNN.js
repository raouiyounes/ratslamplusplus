// Auto-generated. Do not edit!

// (in-package ratslam_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class signalFromCNN {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.signalCNN = null;
    }
    else {
      if (initObj.hasOwnProperty('signalCNN')) {
        this.signalCNN = initObj.signalCNN
      }
      else {
        this.signalCNN = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type signalFromCNN
    // Serialize message field [signalCNN]
    bufferOffset = _serializer.float32(obj.signalCNN, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type signalFromCNN
    let len;
    let data = new signalFromCNN(null);
    // Deserialize message field [signalCNN]
    data.signalCNN = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ratslam_ros/signalFromCNN';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6affad96707d21429a6e875cadc1f691';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 signalCNN
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new signalFromCNN(null);
    if (msg.signalCNN !== undefined) {
      resolved.signalCNN = msg.signalCNN;
    }
    else {
      resolved.signalCNN = 0.0
    }

    return resolved;
    }
};

module.exports = signalFromCNN;
