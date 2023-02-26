import { Pressable, Text, View } from "react-native";
import React, { Component } from "react";

export class Item extends Component {
  render() {
    return (
      <Pressable style={this.props.style}>
        <Text
          style={{
            textAlign: "center",
            paddingBottom: 30,
          }}
        >
          {this.props.title}
        </Text>
        <View style={{ flexDirection: "column" }}>
          <Text
            style={{
              textAlign: "center",
              fontSize: 30,
              color: this.props.text_color,
            }}
          >
            {this.props.text}
          </Text>
        </View>
      </Pressable>
    );
  }
}

export class SmallItem extends Item {
  render() {
    return (
      <Item
        title={this.props.title}
        style={this.props.style}
        text={this.props.text}
        text_color={this.props.text_color}
      ></Item>
    );
  }
}
