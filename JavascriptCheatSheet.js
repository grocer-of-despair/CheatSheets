var x = 10, y = 20;
return eval("x * y"); // Evaluates an equation

// Try and Catch Error handling
try {
  adddlert('Welcome')
}
catch(err) {
  document.getElementById("demo").innerHTML = err.name + "<br>" + err.message;
}
