import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Linking, RefreshControl ,ScrollView, Button} from 'react-native';
import axios from 'axios';
import Icon from 'react-native-vector-icons/Octicons';

class Header extends React.Component{
    

    render(){
        
        return(
                <View style = {{flex : 0.06, alignItems : 'flex-start', justifyContent : 'center'}}>
                    <View style = {{flex : 1, flexDirection : 'row'}}>
                        <Text style = {{flex : 5,paddingHorizontal : 15, fontWeight :'bold', fontSize : 25}}>도봉구 새소식</Text>
                        <View style = {{flex : 1,alignItems :'flex-end', alignItems : 'center',paddingTop : 5}}>
                        <Icon
                         name="three-bars"
                         size={35}
                         color='black'
                         
                             onPress={() => this.props.navigation.navigate("Tab")}
                        />
                        </View>
                    </View>
                    
                </View>
        )
    }
}
class List extends React.Component{
    render(){
        const content =  this.props.content;
        return(
            
                <View style = {styles.List}>
                    <View style = {{backgroundColor : '#ffa2a2', flex : 0.1}}></View>
                    <View style = {{flex: 10}}>
                        <View style = {styles.Title}><Text style = {{fontWeight :'bold', fontSize : 17}}>○ {this.props.title}</Text></View>
                        <View style = {styles.Article}><Text style = {{fontSize : 15}}>{content}</Text></View>
                        <View style = {styles.Link}>
                            
                            <View style = {{flex : 4,alignItems : 'flex-start' ,justifyContent : 'center'}}><Text style = {{textDecorationLine: 'underline',color : 'blue', paddingLeft : 10,fontSize  : 17}}>{this.props.hash}</Text></View>
                            <Text  style = {{flex : 1,fontSize : 14, alignItems : 'flex-end'}}onPress={() =>Linking.openURL(this.props.url)}>원문 보기</Text>
                        </View>
                    </View>
                </View>
            
        );
    }
}
export default class News extends React.Component{
    constructor(props){
        super(props);
    }
    state = {
        title : {
            title1 : '1',
            title2 : '2',
            title3 : '3',
            title4 : '4',
            title5 : '5',
            title6 : '6',
            title7 : '7',
            title8 : '8',
            title9 : '9',
            title10 : '10',
            
        },
        url : {
            url1 : '',
            url2 : '',
            url3 : '',
            url4 : '',
            url5 : '',
            url6 : '',
            url7 : '',
            url8 : '',
            url9 : '',
            url10 : '',
        },

        content : {

            content1 : '',
            content2 : '',
            content3 : '',
            content4 : '',
            content5 : '',
            content6 : '',
            content7 : '',
            content8 : '',
            content9 : '',
            content10 : '',


        },

        hash :{
            hash1 : '',
            hash2 : '',
            hash3 : '',
            hash4 : '',
            hash5 : '',
            hash6 : '',
            hash7 : '',
            hash8 : '',
            hash9 : '',
            hash10 : '',

        },
        refreshing : false,
    }

    _onRefresh = () =>{
        this.setState({refreshing : true});
        this.getArticle();
        this.setState({refreshing : false});
        console.log('refresh');
    }

    
    getArticle = () =>{

       
            
            var options = {
                url : 'http://175.193.68.230/sendData',
                method : 'POST',
                data : {'city' : '도봉구'}
            };
     
        

        axios(options).then(
            (response) =>{
                this.setState({
                    title:{
                        title1 : response.data[0].title,
                        title2 : response.data[1].title,
                        title3 : response.data[2].title,
                        title4 : response.data[3].title,
                        title5 : response.data[4].title,
                        title6 : response.data[5].title,
                        title7 : response.data[6].title,
                        title8 : response.data[7].title,
                        title9 : response.data[8].title,
                        title10 : response.data[9].title,
                    },
                    url:{
                        url1 : response.data[0].url,
                        url2 : response.data[1].url,
                        url3 : response.data[2].url,
                        url4 : response.data[3].url,
                        url5 : response.data[4].url,
                        url6 : response.data[5].url,
                        url7 : response.data[6].url,
                        url8 : response.data[7].url,
                        url9 : response.data[8].url,
                        url10 : response.data[9].url,
                    },

                    content : {

                        content1 : response.data[0].content,
                        content2 : response.data[1].content,
                        content3 : response.data[2].content,
                        content4 : response.data[3].content,
                        content5 : response.data[4].content,
                        content6 : response.data[5].content,
                        content7 : response.data[6].content,
                        content8 : response.data[7].content,
                        content9 : response.data[8].content,
                        content10 : response.data[9].content,
            
            
                    },

                    hash : {

                        hash1 : response.data[0].hash,
                        hash2 : response.data[1].hash,
                        hash3 : response.data[2].hash,
                        hash4 : response.data[3].hash,
                        hash5 : response.data[4].hash,
                        hash6 : response.data[5].hash,
                        hash7 : response.data[6].hash,
                        hash8 : response.data[7].hash,
                        hash9 : response.data[8].hash,
                        hash10 : response.data[9].hash,
                       
                    }


                });
            }
        )
    }
 
    componentDidMount(){
        this.getArticle();
    }
    render(){
       
        var HeaderTitle = '도봉구 새소식';
        
        return(
            <View style = {{flex : 1}}>
            
                <Header navigation = {this.props.navigation} HeaderTitle = {HeaderTitle}></Header>
                <ScrollView
                style = {styles.container}
                refreshControl={
                    <RefreshControl
                    refreshing={this.state.refreshing}
                    onRefresh={this._onRefresh}/>
                }
                >
                    <View style = {{backgroundColor:'#f0f0f0'}}>
                        <List title = {this.state.title.title1} url = {this.state.url.url1} content = {this.state.content.content1} hash = {this.state.hash.hash1}></List>
                        <List title = {this.state.title.title2} url = {this.state.url.url2} content = {this.state.content.content2} hash = {this.state.hash.hash2}></List>
                        <List title = {this.state.title.title3} url = {this.state.url.url3} content = {this.state.content.content3} hash = {this.state.hash.hash3}></List>
                        <List title = {this.state.title.title4} url = {this.state.url.url4} content = {this.state.content.content4} hash = {this.state.hash.hash4}></List>
                        <List title = {this.state.title.title5} url = {this.state.url.url5} content = {this.state.content.content5} hash = {this.state.hash.hash5}></List>
                        <List title = {this.state.title.title6} url = {this.state.url.url6} content = {this.state.content.content6} hash = {this.state.hash.hash6}></List>
                        <List title = {this.state.title.title7} url = {this.state.url.url7} content = {this.state.content.content7} hash = {this.state.hash.hash7}></List>
                        <List title = {this.state.title.title8} url = {this.state.url.url8} content = {this.state.content.content8} hash = {this.state.hash.hash8}></List>
                        <List title = {this.state.title.title9} url = {this.state.url.url9} content = {this.state.content.content9} hash = {this.state.hash.hash9}></List>
                        <List title = {this.state.title.title10} url = {this.state.url.url10} content = {this.state.content.content10} hash = {this.state.hash.hash10}></List>
                    </View>
                </ScrollView>
            </View>
            
        )
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#f0f0f0',
    },
    List : {
        flex: 1,
        borderWidth :2,
        backgroundColor: '#ffffff',
        borderColor : '#f0f0f0',
        borderRadius:-1,
        flexDirection:"row",
        marginVertical : 2,
        marginHorizontal : 10,
        paddingVertical : 5
    },

    Title : {
        flex : 1,
        paddingTop : 10,
        paddingHorizontal : 10,
        fontWeight : 'bold',
        fontSize :20,
        paddingVertical : 5
        
    },
    Article :{
        flex : 2,
        paddingVertical : 10,
        paddingHorizontal : 10,
    },

    Link : {
        flex:1,
        flexDirection : 'row',
        paddingRight : 5,
        paddingBottom : 5
    }
  });