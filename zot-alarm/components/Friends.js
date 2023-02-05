import { View, Alert } from "react-native";
import React from "react";
import { Item } from "./Items";

export default function Friends() {
  let no_friends = true;
  if (no_friends) {
    Alert.alert("You have no friends! Add some later");
  }
  return (
    <View>
      <Item
        title="Your Friends"
        style={{
          width: 390,
          height: 109,
          borderWidth: 2,
          borderRadius: 20,
          margin: 20,
          alignContent: "center",
          textAlign: "center",
        }}
      ></Item>
    </View>
  );
}
