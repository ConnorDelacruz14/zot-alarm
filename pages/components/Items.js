import { Pressable, Text } from "react-native";
import React, { Component } from "react";

export class Item extends Component {
  render() {
    return (
      <Pressable style={this.props.style}>
        <Text style={{ textAlign: "center" }}>{this.props.title}</Text>
      </Pressable>
    );
  }
}

export class SmallItem extends Item {
  render() {
    return <Item title={this.props.title} style={this.props.style}></Item>;
  }
}
