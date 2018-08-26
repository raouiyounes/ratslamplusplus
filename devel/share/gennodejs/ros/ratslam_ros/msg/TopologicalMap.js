// Auto-generated. Do not edit!

// (in-package ratslam_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let TopologicalNode = require('./TopologicalNode.js');
let TopologicalEdge = require('./TopologicalEdge.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class TopologicalMap {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.node_count = null;
      this.node = null;
      this.edge_count = null;
      this.edge = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('node_count')) {
        this.node_count = initObj.node_count
      }
      else {
        this.node_count = 0;
      }
      if (initObj.hasOwnProperty('node')) {
        this.node = initObj.node
      }
      else {
        this.node = [];
      }
      if (initObj.hasOwnProperty('edge_count')) {
        this.edge_count = initObj.edge_count
      }
      else {
        this.edge_count = 0;
      }
      if (initObj.hasOwnProperty('edge')) {
        this.edge = initObj.edge
      }
      else {
        this.edge = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TopologicalMap
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [node_count]
    bufferOffset = _serializer.uint32(obj.node_count, buffer, bufferOffset);
    // Serialize message field [node]
    // Serialize the length for message field [node]
    bufferOffset = _serializer.uint32(obj.node.length, buffer, bufferOffset);
    obj.node.forEach((val) => {
      bufferOffset = TopologicalNode.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [edge_count]
    bufferOffset = _serializer.uint32(obj.edge_count, buffer, bufferOffset);
    // Serialize message field [edge]
    // Serialize the length for message field [edge]
    bufferOffset = _serializer.uint32(obj.edge.length, buffer, bufferOffset);
    obj.edge.forEach((val) => {
      bufferOffset = TopologicalEdge.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TopologicalMap
    let len;
    let data = new TopologicalMap(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [node_count]
    data.node_count = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [node]
    // Deserialize array length for message field [node]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.node = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.node[i] = TopologicalNode.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [edge_count]
    data.edge_count = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [edge]
    // Deserialize array length for message field [edge]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.edge = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.edge[i] = TopologicalEdge.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 60 * object.node.length;
    length += 76 * object.edge.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ratslam_ros/TopologicalMap';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'deefb2c5a22caaa16af4e1b64a821bdc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    uint32 node_count
    TopologicalNode[] node
    uint32 edge_count
    TopologicalEdge[] edge
    
    	
    
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
    
    ================================================================================
    MSG: ratslam_ros/TopologicalNode
    uint32 id
    geometry_msgs/Pose pose
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    ================================================================================
    MSG: ratslam_ros/TopologicalEdge
    uint32 id
    uint32 source_id
    uint32 destination_id
    duration duration
    geometry_msgs/Transform transform
    ================================================================================
    MSG: geometry_msgs/Transform
    # This represents the transform between two coordinate frames in free space.
    
    Vector3 translation
    Quaternion rotation
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TopologicalMap(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.node_count !== undefined) {
      resolved.node_count = msg.node_count;
    }
    else {
      resolved.node_count = 0
    }

    if (msg.node !== undefined) {
      resolved.node = new Array(msg.node.length);
      for (let i = 0; i < resolved.node.length; ++i) {
        resolved.node[i] = TopologicalNode.Resolve(msg.node[i]);
      }
    }
    else {
      resolved.node = []
    }

    if (msg.edge_count !== undefined) {
      resolved.edge_count = msg.edge_count;
    }
    else {
      resolved.edge_count = 0
    }

    if (msg.edge !== undefined) {
      resolved.edge = new Array(msg.edge.length);
      for (let i = 0; i < resolved.edge.length; ++i) {
        resolved.edge[i] = TopologicalEdge.Resolve(msg.edge[i]);
      }
    }
    else {
      resolved.edge = []
    }

    return resolved;
    }
};

module.exports = TopologicalMap;
