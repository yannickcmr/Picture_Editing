let array = ["hund", "katze", "maus", "elefant", "schlange", "stachelschwein", "affe", "giraffe"];

function addArrayElement(element) {
  let arrayCopy = [...array];
  if (!arrayCopy.includes(element)){
    arrayCopy.push(element);
  };
  return arrayCopy;
}

function getArrayElements(number, startIndex) {
  let result = [];
  let len = array.length
  let offset = startIndex % len;
  if ((number + offset -1) > len){
    number = len - offset
  };
  for (let i = 0; i < (number); i++){
    result.push(array[i + offset])
  };
  return result;
}


// fehler
function deleteArrayElements(number, startIndex, everyIth) {
  let arrayCopy = [...array];
  let removedItems = [];
  let len = array.length
  let offset = startIndex % len;
  if ((number + offset -1) > len){
    number = len - offset
  };
  if (everyIth > len){
    everyIth = everyIth % len;
  };
  for (let i = 0; i < number; i+=everyIth){
    removedItems.push(arrayCopy[i + offset] )
    arrayCopy[i + offset] = null
  };
  return {
    newResult: arrayCopy,
    removedItems: removedItems
  };  
}