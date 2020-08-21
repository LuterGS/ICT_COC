import React from 'react';
import { StyleSheet, Text, View} from 'react-native';
import Icon from 'react-native-vector-icons/Octicons';
class Header extends React.Component{
    render(){
        return(
                <View style = {{flex : 0.06, paddingVertical : 10}}>
                    <View style = {styles.header}>
                        <View style = {{flex : 1}}>
                            <Icon
                            style = {{flex : 1, marginLeft:20,paddingTop : 7}}
                            name="chevron-left"
                            size={30}
                            color='black'
                            onPress={() => this.props.navigation.goBack()}
                            />
                        </View>
                        <View style = {{ flex : 4,alignItems : 'center',borderWidth :2,
                                        borderColor : '#f0f0f0',
                                        borderBottomColor : 'black',
                                        borderRadius:-1,}}>
                            <Text style = {{flex : 5, paddingHorizontal : 15, fontWeight :'bold', fontSize : 25}}>목록</Text>
                        </View>
                        <View style = {{flex : 1}}>
                        </View>
                    </View>           
                </View>
        )
    }
}

class Body extends React.Component{
    
    render(){
        return(
            <View style= {styles.body}>
                


                <Text 
                style = {styles.list}
                onPress={() => this.props.navigation.navigate("Gwanak",{city : '관악구'})}
                >관악구
                </Text>

                <Text 
                style = {styles.list}
                onPress={() => this.props.navigation.navigate("Dobong",{city : '도봉구'})}
                >도봉구
                </Text>

                <Text 
                style = {styles.list}
                onPress={() => this.props.navigation.navigate("Seocho",{city : '서초구'})}
                >서초구
                </Text>



            </View>
        )
    }
}
export default class TabList extends React.Component{
    render(){
        return(
            <View style = {{flex : 1}}>
                <Header navigation = {this.props.navigation}></Header>
                <Body navigation = {this.props.navigation}></Body>
            </View>
        )
    }
}

const styles = StyleSheet.create({

    header : {
        flex : 1,
         flexDirection : 'row', 
         alignItems : 'center'
    },
    body : {
        flex: 1, 
        alignItems : 'center', 
        justifyContent : 'flex-start',
         paddingTop : 20, 
    },

    list : {
        fontSize : 20, 
        paddingVertical : 20
    }
})