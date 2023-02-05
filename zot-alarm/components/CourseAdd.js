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
  const [departmentName, setDepartmentName] = useState("");
  const [courseCode, setCourseCode] = useState("");
  const [courseNumber, setCourseNumber] = useState("");
  const [classList, setClassList] = useState([]);

  let class_info = {
    departmentName: "",
    courseNumber: "",
    courseCode: "",
  };

  return (
    <View style={styles.container}>
      <Image style={styles.logo} source={require("../assets/logo.png")}></Image>
      <Text style={styles.title_text}>To get started, add your classes.</Text>
      <View>
        <TextInput
          placeholder=" Department Name: ex. I&C SCI"
          style={styles.input}
          value={departmentName}
          onChangeText={(text) => setDepartmentName(text)}
        ></TextInput>
        <TextInput
          placeholder=" Course Number: ex. 45C"
          style={styles.input}
          value={courseNumber}
          onChangeText={(text) => setCourseNumber(text)}
        ></TextInput>
        <TextInput
          placeholder=" Section Code: ex. 35630"
          style={styles.input}
          value={courseCode}
          onChangeText={(text) => setCourseCode(text)}
        ></TextInput>
      </View>
      <Pressable
        title="add-new-class-btn"
        style={styles.add_new_class_btn}
        onPress={() => {
          setDepartmentName("");
          setCourseNumber("");
          setCourseCode("");
        }}
      >
        <Text style={styles.add_new_class_text}>Add New Class</Text>
      </Pressable>
      <Pressable
        title="submit-btn"
        style={styles.submit_btn}
        onPress={() => {
          if (
            (departmentName != "" && courseCode != "" && courseNumber != "") ||
            classList.length != 0
          ) {
            class_info.departmentName = departmentName;
            class_info.courseCode = courseCode;
            class_info.courseNumber = courseNumber;
            setClassList([...classList, class_info]);
            navigation.navigate("Homepage");
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
    alignSelf: "center",
    marginTop: -40,
  },

  container: {
    fontWeight: "bold",
    fontSize: 60,
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },

  title_text: {
    fontSize: 40,
    fontWeight: "bold",
    marginTop: 40,
    textAlign: "center",
  },

  input: {
    backgroundColor: "#D9D9D9",
    borderRadius: 10,
    padding: 10,
    width: 300,
    marginTop: 20,
  },

  submit_btn: {
    backgroundColor: "#333",
    padding: 10,
    borderRadius: 5,
    marginTop: 20,
  },

  submit_text: {
    color: "#fff",
    fontWeight: "bold",
    fontSize: 20,
    textAlign: "center",
  },
  add_new_class_btn: {
    backgroundColor: "#333",
    padding: 10,
    borderRadius: 5,
    marginTop: 20,
  },

  add_new_class_text: {
    color: "#fff",
    fontWeight: "bold",
    fontSize: 20,
    textAlign: "center",
  },
});
