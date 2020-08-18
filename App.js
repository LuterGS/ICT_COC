import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';
import TabList from './Component/TabList';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Gwanak from './Component/Gwanak';
import Dobong from './Component/Dobong';
import Seocho from './Component/Seocho';
const Stack = createStackNavigator();

class Navi extends React.Component{
  render(){
    return(
      
      <NavigationContainer>
            <Stack.Navigator initialRouteName = "Gwanak" screenOptions={{headerShown : false}}>
              <Stack.Screen name = "Tab"
                component = {TabList}
                 /> 
                <Stack.Screen name = "Gwanak"             
                component = {Gwanak}
                 />
                 <Stack.Screen name = "Dobong"             
                component = {Dobong}
                 />
                 <Stack.Screen name = "Seocho"             
                component = {Seocho}
                 />

            </Stack.Navigator>
      </NavigationContainer>

  )
  }
}
export default class App extends React.Component{
  render(){
    return (
      <SafeAreaView style={styles.container}>
          <Navi></Navi>
      </SafeAreaView>
    );
  }
  
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f0',
    //alignItems: 'center',
    justifyContent: 'center',
    marginTop : 20,
  },
});
