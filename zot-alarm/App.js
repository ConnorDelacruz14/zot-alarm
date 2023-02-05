import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Homepage from "./components/Homepage";
import Loginpage from "./components/Loginpage";
import Alarms from "./components/Alarms";
import Friends from "./components/Friends";
import Graphs from "./components/Graphs";

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Zot Alarm!">
        <Stack.Screen name="Zot Alarm!" component={Loginpage} />
        <Stack.Screen
          name="Homepage"
          component={Homepage}
          options={() => ({
            // headerBackVisible: false,
          })}
        />
        <Stack.Screen name="Alarms" component={Alarms}></Stack.Screen>
        <Stack.Screen name="Friends" component={Friends}></Stack.Screen>
        <Stack.Screen name="Graphs" component={Graphs}></Stack.Screen>
      </Stack.Navigator>
    </NavigationContainer>
  );
}
