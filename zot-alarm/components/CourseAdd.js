import { StatusBar } from "expo-status-bar";
import { useState } from "react";
import {
  Image,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
  Alert,
} from "react-native";

export default function CourseAdd({ navigation }) {
  const [className, setClassName] = useState("");
  const [classNumber, setClassNumber] = useState("");
  const [classRoom, setClassRoom] = useState("");
  const [classTime, setClassTime] = useState("");

  let class_info = {
    className: "",
    classNumber: "",
    classRoom: "",
    classTime: "",
  };

  return (
    <View style={styles.container}>
      <Image style={styles.logo} source={require("../assets/logo.png")}></Image>
      <Text style={styles.title_text}>Zot Alarm!</Text>
      <View>
        <TextInput
          placeholder=" Class Name: "
          style={styles.input}
          value={className}
          onChangeText={(text) => setClassName(text)}
        ></TextInput>
        <TextInput
          placeholder=" Class Number: "
          style={styles.input}
          value={classNumber}
          onChangeText={(text) => setClassNumber(text)}
        ></TextInput>
        <TextInput
          placeholder=" Class Room: "
          style={styles.input}
          value={classRoom}
          onChangeText={(text) => setClassRoom(text)}
        ></TextInput>
        <TextInput
          placeholder=" Class Time: "
          style={styles.input}
          value={classTime}
          onChangeText={(text) => setClassTime(text)}
        ></TextInput>
      </View>
      <Pressable
        title="submit-btn"
        style={styles.submit_btn}
        onPress={() => {
          if (
            className != "" &&
            classNumber != "" &&
            classRoom != "" &&
            classTime != ""
          ) {
            class_info.className = className;
            class_info.classNumber = classNumber;
            class_info.classRoom = classRoom;
            class_info.classTime = classTime;
            navigation.navigate("Homepage");
            Alert.alert("Class has been added successfully!");
          } else {
            Alert.alert("Please fill out all the fields.");
          }
        }}
      >
        <Text style={styles.submit_text}>Submit</Text>
      </Pressable>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  logo: {
    marginTop: -240,
  },

  container: {
    fontWeight: "bold",
    text: 60,
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
