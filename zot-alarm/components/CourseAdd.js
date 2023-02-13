import React, { Component } from "react";
import {
  Image,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
  Alert,
  StatusBar,
} from "react-native";

export default class CourseAdd extends Component {
  constructor(props) {
    super(props);

    this.state = {
      departmentName: "",
      courseCode: "",
      courseNumber: "",
      class_list: [],
    };

    this.classInfo = {
      departmentName: "",
      courseNumber: "",
      courseCode: "",
    };
  }

  render() {
    return (
      <View style={styles.container}>
        <Image
          style={styles.logo}
          source={require("../assets/logo.png")}
        ></Image>
        <Text style={styles.title_text}>To get started, add your classes.</Text>
        <View>
          <TextInput
            placeholder="Department Name: ex. I&C SCI"
            style={styles.input}
            value={this.state.departmentName}
            onChangeText={(text) => this.setState({ departmentName: text })}
          ></TextInput>
          <TextInput
            placeholder="Course Number: ex. 45C"
            style={styles.input}
            value={this.state.courseNumber}
            onChangeText={(text) => this.setState({ courseNumber: text })}
          ></TextInput>
          <TextInput
            placeholder="Section Code: ex. 35630"
            style={styles.input}
            value={this.state.courseCode}
            onChangeText={(text) => this.setState({ courseCode: text })}
          ></TextInput>
        </View>
        <Pressable
          title="add-new-class-btn"
          style={styles.add_new_class_btn}
          onPress={() => {
            this.classInfo.departmentName = this.state.departmentName;
            this.classInfo.courseCode = this.state.courseCode;
            this.classInfo.courseNumber = this.state.courseNumber;
            this.setState({
              class_list: [...this.state.class_list, this.classInfo],
              departmentName: "",
              courseNumber: "",
              courseCode: "",
            });
          }}
        >
          <Text style={styles.add_new_class_text}>
            Submit and add new class
          </Text>
        </Pressable>
        <Pressable
          title="submit-btn"
          style={styles.submit_btn}
          onPress={() => {
            if (this.state.class_list.length !== 0) {
              this.props.navigation.navigate("Homepage", {
                class_list: this.state.class_list,
                login_info: this.props.route.params.login_info,
              });
            } else {
              Alert.alert("Please submit at least one class.");
            }
          }}
        >
          <Text style={styles.submit_text}>Continue</Text>
        </Pressable>
        <StatusBar style="auto" />
      </View>
    );
  }
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
