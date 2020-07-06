var express = require("express");
var app = express();

//set view engine : ejs
app.set("view engine","ejs");
app.use(express.static('public'));



// express route
app.get("/",function(req,res){
    var tasksDB = ["100DaysOfCode","Study Research Paper","Develope Reinforcement Algorithm","Sequence Prediction research","Book: Master Algorithm"];
    res.render(`index`,{tasks:tasksDB});
});


app.get("*",function(req,res){
    res.send("<h1>Invalid route</h1>");
});


// server listening port

app.listen(3000,function(){
    console.log("server started on port 3000");
});