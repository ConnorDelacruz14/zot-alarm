import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Homepage from "./Homepage";
import Loginpage from "./Loginpage";

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
      </Stack.Navigator>
    </NavigationContainer>
  );
}
