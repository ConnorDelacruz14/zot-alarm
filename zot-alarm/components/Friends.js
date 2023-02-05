import { View, Text, Alert } from "react-native";
import React from "react";
import { Item } from "./Homepage";

export default function Friends() {
  let no_friends = true;
  Alert.alert("You have no friends! Add some later");
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
