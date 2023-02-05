import { ImageBackground } from "react-native";
import React from "react";

export default function Alarms() {
  return (
    <ImageBackground
      source={{
        uri: "https://github.com/ConnorDelacruz14/zot-alarm/blob/main/zot-alarm/components/alarm.png",
      }}
      resizeMode="cover"
      style={{ flex: 1, justifyContent: "center" }}
    ></ImageBackground>
  );
}
