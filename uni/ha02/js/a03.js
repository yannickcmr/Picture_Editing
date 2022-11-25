let object = {
  a: "hund", b: "katze", c: "maus", d: "elefant", e: "schlange", f: "stachelschwein", g: "affe", h: "giraffe"
}

function createKey(key){
  if (key.length== 1){
    return [key, "_1"].join("")
  }
  else{
    let char_array = key.split("_")
    char_array[1] = parseInt(char_array[1] )+ 1;
    return char_array.join("_")
  };
}

function addObjectElement(key, value) {
  let objectCopy = Object.assign({}, object)
  while (key in objectCopy){
    key = createKey(key);
  }
  objectCopy[key] = value;
  return objectCopy;
}

function getObjectElements(keys) {
  let result = [];
  for (let i = 0; i < keys.length; i++){
    if (keys[i] in object){
      result.push(object[keys[i]]);
    } else {
      result.push("not found");
    };
  }
  return result;
}

function deleteObjectElements(keys) {
  let objectCopy = Object.assign({}, object)
  for (let i=0; i < keys.length; i++){
    if (keys[i] in objectCopy){
      delete objectCopy[keys[i]];
    }
  }
  return objectCopy;
}