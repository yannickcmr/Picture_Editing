function multiply(number1, number2) {
  console.log(arguments);
  if (arguments.length == 1 ){
    number2 = 1
  };
  number1 *= number2;
  return number1;
}


function multiplyAll() {
    let result = 1;
    for (let i = 0; i < arguments.length; i++){
      result *= arguments[i];
    };
  return result;
}
