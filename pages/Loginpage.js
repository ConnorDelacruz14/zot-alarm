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

export default function Loginpage({ navigation }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  let login_info = {
    email: "",
    password: "",
  };

  return (
    <View style={styles.container}>
      <Image style={styles.logo} source={require("../assets/logo.png")}></Image>
      <Text style={styles.title_text}>Zot Alarm!</Text>
      <View>
        <TextInput
          placeholder=" UCI Email: "
          style={styles.email_entry}
          value={email}
          onChangeText={(text) => setEmail(text)}
        ></TextInput>
        <TextInput
          placeholder=" Password: "
          style={styles.password_entry}
          value={password}
          secureTextEntry={true}
          onChangeText={(text) => setPassword(text)}
        ></TextInput>
      </View>
      <Pressable
        title="login-btn"
        style={styles.login_btn}
        onPress={() => {
          if (email != "" && password != "") {
            if (!email.includes("@uci.edu")) {
              Alert.alert("Please enter a valid UCI email.");
            } else {
              login_info.email = email;
              login_info.password = password;
              fetch("http://127.0.0.1:5000/process_data", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(login_info),
              })
                .then((response) => {
                  return response.json();
                })
                .then((data) => {
                  console.log(data);
                  if (data["status"] == "new login") {
                    navigation.navigate("CourseAdd", { login_info });
                  } else if (data["status"] == "correct login") {
                    navigation.navigate("Homepage", { data });
                  } else {
                    Alert.alert("Incorrect password for the given email.");
                  }
                })
                .catch((error) => {
                  console.error(error);
                });
            }
          }
        }}
      >
        <Text style={styles.login_text}>Login</Text>
      </Pressable>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  logo: {
    marginTop: -240,
    width: 400,
    height: 200,
  },

  container: {
    fontWeight: "bold",
    text: 60,
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },

  title_text: {
    fontSize: 60,
    //fontFamily: "Comfortaa-Regular",
    marginTop: 20,
    marginBottom: 40,
  },

  email_entry: {
    width: 229,
    height: 40,
    borderRadius: 10,
    backgroundColor: "#D9D9D9",
    paddingLeft: 5,
  },

  password_entry: {
    marginTop: 10,
    width: 229,
    height: 40,
    borderRadius: 10,
    backgroundColor: "#D9D9D9",
    paddingLeft: 5,
  },

  login_btn: {
    textAlign: "center",
    marginTop: 40,
    color: "black",
    width: 229,
    height: 40,
    borderRadius: 10,
    backgroundColor: "#D9D9D9",
  },

  login_text: {
    textAlign: "center",
    fontSize: 15,
    marginTop: 10,
  },
});