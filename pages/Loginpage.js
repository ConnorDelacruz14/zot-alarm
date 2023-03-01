import { StatusBar } from "expo-status-bar";
import { useState, useEffect } from "react";
import {
  Image,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
  Alert,
} from "react-native";
import * as Location from "expo-location";

export default function Loginpage({ navigation }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [location, setLocation] = useState(null);

  let login_info = {
    email: "",
    password: "",
    location: null,
  };

  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== "granted") {
        Alert.alert(
          "Permission to access location was denied, you must enable location to use this app!"
        );
        return;
      }

      let location = await Location.getCurrentPositionAsync({});
      login_info.location = location;
      setLocation(location);
    })();
  }, []);

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
      {location ? (
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
                login_info.location = location;
                fetch("http://10.8.20.229:5000/process_data", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify({
                    login_info: login_info,
                    request: "login",
                  }),
                })
                  .then((response) => {
                    return response.json();
                  })
                  .then((data) => {
                    if (data["status"] == "new_account") {
                      navigation.navigate("CourseAdd", {
                        login_info: login_info,
                      });
                    } else if (data["status"] == "correct_login") {
                      navigation.navigate("Homepage", {
                        from: "LoginPage",
                        request: "load_global",
                        login_info: login_info,
                      });
                    } else if (data["status"] == "incorrect_login") {
                      Alert.alert("Incorrect password for the given email.");
                    } else if (data["status"] == "error") {
                      Alert.alert(
                        "There was an error logging in. Try again later."
                      );
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
      ) : (
        <View style={styles.location_error}>
          <Image
            source={{
              uri: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Exclamation_Circle_Red.svg/16px-Exclamation_Circle_Red.svg.png",
            }}
            style={styles.location_icon}
          />
          <Text style={styles.location_error_text}>
            Please enable location to continue.
          </Text>
        </View>
      )}
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

  location_error: {
    flexDirection: "row",
    alignItems: "center",
    color: "red",
    marginTop: 10,
  },

  location_icon: {
    width: 20,
    height: 20,
    marginRight: 5,
    color: "red",
  },
  location_error_text: {
    color: "red",
    fontSize: 16,
    fontWeight: "bold",
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
