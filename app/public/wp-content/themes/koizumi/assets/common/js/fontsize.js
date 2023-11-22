var os,ua;

ua = navigator.userAgent;

if(ua.indexOf("Mac", 0) >= 0){
os = "mac_";
}
else if(ua.match(/Win(dows )?(NT 6¥.0|V)/)){
os = "winVista_";
}
else if(ua.indexOf("Win", 0) >= 0){
os = "win_";
}
else{
os = "other_";
}



if(ua.indexOf("Opera", 0) >= 0){
os += "opera";
}

else if(ua.indexOf("MSIE 7", 0) >= 0){
os += "msie7";
}

else if(ua.indexOf("MSIE 6", 0) >= 0){
os += "msie";
}

else if(ua.indexOf("MSIE 5", 0) >= 0){
os += "msie5";
}

else if(ua.indexOf("Mozilla/4.0", 0) >= 0){
os += "msie";
}

else if(ua.indexOf("Mozilla/4", 0) >= 0){
os += "ns4";
}

else if(ua.indexOf("Safari", 0) >= 0){
os += "safari";
}

else{
os += "other";
}


if(os == "mac_msie5"){
document.write("<link rel=stylesheet href=css/default_msiemac5.css />");
}

else if(os == "mac_ns4"){
document.write("");
}

else if(os == "mac_safari"){
document.write("<link rel=stylesheet href=css/default_safari.css />");
}

else if(os == "mac_opera"){
document.write("<link rel=stylesheet href=css/default_operamac.css />");
}

else if(os == "mac_other"){
document.write("<link rel=stylesheet href=css/default_geckomac.css />");
}

else if(os == "winVista_msie7"){
document.write("<link rel=stylesheet href=css/default_msie7v.css />");
}

else if(os == "win_msie7"){
document.write("<link rel=stylesheet href=css/default_msie7x.css />");
}

else if(os == "win_msie"){
document.write("<link rel=stylesheet href=css/default_msie.css />");
}

else if(os == "win_msie5"){
document.write("<link rel=stylesheet href=css/default_msie5.css />");
}

else if(os == "win_ns4"){
document.write("");
}

else if(os == "win_opera"){
document.write("<link rel=stylesheet href=css/default_opera.css />");
}

else if(os == "win_other"){
document.write("<link rel=stylesheet href=css/default_gecko.css />");
}

else if(os == "other_msie"){
document.write("<link rel=stylesheet href=css/default_msie.css />");
}

else if(os == "other_ns4"){
document.write("");
}

else if(os == "other_opera"){
document.write("<link rel=stylesheet href=css/default_opera.css />");
}

else if(os == "other_other"){
document.write("<link rel=stylesheet href=css/default_gecko.css />");
}

else{
document.write("<link rel=stylesheet href=css/default_gecko.css />");
}
