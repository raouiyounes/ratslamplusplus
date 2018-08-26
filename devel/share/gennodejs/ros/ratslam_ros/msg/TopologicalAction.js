// Auto-generated. Do not edit!

// (in-package ratslam_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class TopologicalAction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.action = null;
      this.src_id = null;
      this.dest_id = null;
      this.relative_rad = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('action')) {
        this.action = initObj.action
      }
      else {
        this.action = 0;
      }
      if (initObj.hasOwnProperty('src_id')) {
        this.src_id = initObj.src_id
      }
      else {
        this.src_id = 0;
      }
      if (initObj.hasOwnProperty('dest_id')) {
        this.dest_id = initObj.dest_id
      }
      else {
        this.dest_id = 0;
      }
      if (initObj.hasOwnProperty('relative_rad')) {
        this.relative_rad = initObj.relative_rad
      }
      else {
        this.relative_rad = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TopologicalAction
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [action]
    bufferOffset = _serializer.uint32(obj.action, buffer, bufferOffset);
    // Serialize message field [src_id]
    bufferOffset = _serializer.uint32(obj.src_id, buffer, bufferOffset);
    // Serialize message field [dest_id]
    bufferOffset = _serializer.uint32(obj.dest_id, buffer, bufferOffset);
    // Serialize message field [relative_rad]
    bufferOffset = _serializer.float64(obj.relative_rad, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TopologicalAction
    let len;
    let data = new TopologicalAction(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [action]
    data.action = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [src_id]
    data.src_id = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [dest_id]
    data.dest_id = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [relative_rad]
    data.relative_rad = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ratslam_ros/TopologicalAction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '365d6e23e0fb90a477e21472cd2edf80';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # actions
    uint32 CREATE_NODE=1
    uint32 CREATE_EDGE=2
    uint32 SET_NODE=3
    
    Header header
    
    uint32 action
    
    uint32 src_id
    uint32 dest_id
    
    float64 relative_rad
    
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TopologicalAction(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.action !== undefined) {
      resolved.action = msg.action;
    }
    else {
      resolved.action = 0
    }

    if (msg.src_id !== undefined) {
      resolved.src_id = msg.src_id;
    }
    else {
      resolved.src_id = 0
    }

    if (msg.dest_id !== undefined) {
      resolved.dest_id = msg.dest_id;
    }
    else {
      resolved.dest_id = 0
    }

    if (msg.relative_rad !== undefined) {
      resolved.relative_rad = msg.relative_rad;
    }
    else {
      resolved.relative_rad = 0.0
    }

    return resolved;
    }
};

// Constants for message
TopologicalAction.Constants = {
  CREATE_NODE: 1,
  CREATE_EDGE: 2,
  SET_NODE: 3,
}

module.exports = TopologicalAction;
