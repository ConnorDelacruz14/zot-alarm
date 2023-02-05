import { Alert, Image, Pressable, StyleSheet, Text, View } from "react-native";
import React, { Component } from "react";
import Friends from "./Friends";
import Alarms from "./Alarms";
import Graphs from "./Graphs";

export class Item extends Component {
  render() {
    return (
      <Pressable style={this.props.style}>
        <Text style={{ textAlign: "center" }}>{this.props.title}</Text>
      </Pressable>
    );
  }
}

class SmallItem extends Item {
  render() {
    return <Item title={this.props.title} style={this.props.style}></Item>;
  }
}

export default function Homepage({ navigation }) {
  let attendance_rate = 95;
  let on_time_rate = 87;
  let tuition_lost = "487";
  let next_class = {};
  return (
    <View style={styles.app_container}>
      <Item title="Today's Most Missed Classes" style={styles.item}></Item>
      <Item title="Your Missed Classes" style={styles.item}></Item>
      <View style={{ display: "flex", flexDirection: "row" }}>
        <SmallItem
          title="Total Tuition Lost"
          style={styles.small_item}
        ></SmallItem>
        <SmallItem title="Next Class" style={styles.small_item}></SmallItem>
      </View>
      <View style={{ display: "flex", flexDirection: "row" }}>
        <Text style={styles.attendance_rate}>
          {attendance_rate}% Attendance Rate
        </Text>
        <Text style={styles.attendance_rate}>
          {on_time_rate}
          {"%                On-time Rate "}
        </Text>
      </View>
      <Taskbar navigation={navigation}></Taskbar>
    </View>
  );
}

const Taskbar = ({ navigation }) => {
  return (
    <View style={styles.taskbar_container}>
      <Pressable
        onPress={() => {
          navigation.navigate(Alarms);
        }}
      >
        <Image
          source={require("../assets/alarm-clock.png")}
          style={styles.icon}
        />
      </Pressable>
      <Pressable
        onPress={() => {
          navigation.navigate(Friends);
        }}
      >
        <Image source={require("../assets/friends.png")} style={styles.icon} />
      </Pressable>
      <Pressable
        onPress={() => {
          navigation.navigate(Graphs);
        }}
      >
        <Image source={require("../assets/graphs.png")} style={styles.icon} />
      </Pressable>
    </View>
  );
};

const styles = StyleSheet.create({
  app_container: {
    flex: 1,
    alignItems: "center",
  },

  item: {
    width: 390,
    height: 109,
    borderWidth: 2,
    borderRadius: 20,
    margin: 20,
    alignContent: "center",
    textAlign: "center",
  },

  small_item: {
    width: 190,
    height: 109,
    borderWidth: 2,
    borderRadius: 20,
    margin: 10,
    alignContent: "center",
    textAlign: "center",
  },

  attendance_rate: {
    fontSize: 20,
    fontWeight: "bold",
    color: "green",
    textAlign: "center",
    width: 150,
    paddingTop: 30,
  },

  taskbar_container: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "flex-end",
    height: 100,
    padding: 30,
    backgroundColor: "#D3D3D3",
    position: "absolute",
    bottom: 0,
    left: 0,
    right: 0,
  },
  icon: {
    width: 40,
    height: 40,
  },
});
