import { Image, View, ScrollView } from "react-native";
import React from "react";

export default function Graphs() {
  return (
    <View>
      <ScrollView>
        <Image
          source={require("../assets/chart2.png")}
          style={{ width: 410 }}
        ></Image>
      </ScrollView>
    </View>
  );
}
