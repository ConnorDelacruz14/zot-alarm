import { Alert, Image, Pressable, StyleSheet, Text, View } from "react-native";
import React, { Component } from "react";

class Item extends Component {
  render() {
    return (
      <View style={this.props.style}>
        <Text style={{ textAlign: "center" }}>{this.props.title}</Text>
      </View>
    );
  }
}

class SmallItem extends Item {
  render() {
    return <Item title={this.props.title} style={this.props.style}></Item>;
  }
}

export default function Homepage({ navigation }) {
  return (
    <View style={styles.app_container}>
      <Item title="Today's Most Missed Classes" style={styles.item}></Item>
      <Item title="Your Missed Classes" style={styles.item}></Item>
      <View style={{ display: "flex", flexDirection: "row" }}>
        <SmallItem
          title="Total Tuition Lost"
          style={styles.small_item}
        ></SmallItem>
        <SmallItem title="Your Schedule" style={styles.small_item}></SmallItem>
      </View>
      <Text style={styles.attendance_rate}>97% Attendance Rate</Text>
      <Taskbar></Taskbar>
    </View>
  );
}

const Taskbar = () => {
  return (
    <View style={styles.taskbar_container}>
      <Image source={require("./assets/alarm-clock.png")} style={styles.icon} />
      <Image source={require("./assets/friends.png")} style={styles.icon} />
      <Image source={require("./assets/graphs.png")} style={styles.icon} />
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
    fontSize: 50,
    fontWeight: "bold",
    color: "green",
    textAlign: "center",
    width: 300,
    paddingTop: 30,
  },

  taskbar_container: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "flex-end",
    height: 100,
    padding: 30,
    backgroundColor: "#F5F5F5",
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
