import { ImageBackground } from "react-native";
import React from "react";

export default function Alarms() {
  return (
    <ImageBackground
      source={{
        uri: "https://www.applesutra.com/wp-content/uploads/2021/11/1-473x1024.jpeg",
      }}
      resizeMode="cover"
      style={{
        flex: 1,
        justifyContent: "center",
      }}
    ></ImageBackground>
  );
}
