import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Homepage from "./pages/Homepage";
import Loginpage from "./pages/Loginpage";
import CourseAdd from "./pages/CourseAdd";
import Friends from "./pages/Friends";
import Graphs from "./pages/Graphs";

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
            headerBackVisible: false,
          })}
        />
        <Stack.Screen
          name="CourseAdd"
          component={CourseAdd}
          options={() => ({
            headerBackVisible: false,
          })}
        />
        <Stack.Screen name="Friends" component={Friends}></Stack.Screen>
        <Stack.Screen name="Graphs" component={Graphs}></Stack.Screen>
      </Stack.Navigator>
    </NavigationContainer>
  );
}
