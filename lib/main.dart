import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main()=> runApp(new MaterialApp(
    home: new HomePage()
));

class HomePage extends StatefulWidget {
  @override
  HomePageState createState() => new HomePageState();
}



class HomePageState extends State<HomePage> {

  final String url = "http://192.168.43.22:5000/ret";
  List data;
  Map _entries = new Map();

  Future<String> makeRequest() async {
    var response = await http
        .get(Uri.encodeFull(url), headers: {"Accept": "application/json"});
    setState(() => _entries = JSON.decode(response.body));
    print(response.body);
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      backgroundColor: Colors.white,
      body: new Center(
        child: new Container(
          padding: new EdgeInsets.all(32.0),
            child: new Center(
              child: new Column(
                children: <Widget>[
                  SizedBox(height: 200.0),
                  new Text("Welcome to Kenshi",style: TextStyle(fontSize: 30.0,fontWeight: FontWeight.bold,fontStyle: FontStyle.italic),),
                  new Text("Click on the button to see uploaded notes.",style: TextStyle(fontSize: 20.0,fontWeight: FontWeight.bold,fontStyle: FontStyle.italic)),
                  SizedBox(height: 80.0),
                  new RaisedButton(
                    color: Colors.orangeAccent,
                  child: new Text("Click me!",style: TextStyle(fontSize: 15.0,color: Colors.white),)
                    ,onPressed: makeRequest,),
                  SizedBox(height: 10.0),
                  new Expanded(child: new ListView.builder(
                    itemCount: _entries.length,
                    itemBuilder: (BuildContext context, int index){
                      String key = _entries.keys.elementAt(index);
                      return new Row(
                        children: <Widget>[
                          new Text('${key} : '),
                          new Text(_entries[key])],
                    );
                  },
                ))
              ],
            ),
          )
        ),
      )
    );
  }
}