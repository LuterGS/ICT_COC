import React from 'react';
import { StyleSheet, SafeAreaView } from 'react-native';
import TabList from './Component/TabList';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import News from './Component/News';

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
                component = {News}
                 />
                <Stack.Screen name = "Dobong"             
                component = {News}
                 />
                <Stack.Screen name = "Seocho"             
                component = {News}
                 />
                 <Stack.Screen name = "Dongdaemun"             
                component = {News}
                 />
                <Stack.Screen name = "Seodaemun"             
                component = {News}
                 />
                <Stack.Screen name = "Songpa"             
                component = {News}
                 />
                 <Stack.Screen name = "Yangchun"             
                component = {News}
                 />
                <Stack.Screen name = "Dongjak"             
                component = {News}
                 />
                <Stack.Screen name = "Gangdong"             
                component = {News}
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
    justifyContent: 'center',
    marginTop : 20,
  },
});
