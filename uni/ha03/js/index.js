
// Aufgabe 3.1.1
function notGoodGrades(grades) {
  return grades.filter(note => parseFloat((note.grade).replace(",", ".")) >= 3.0)
}

function overviewObject(student, grades){
  return {"student" : student, "grades" : grades.filter(g => (g.matrikelnummer == student.matrikelnummer))}
}

// Aufgabe 3.1.2
function gradeOverview(students, grades) {
  return students.map(s =>  overviewObject(s, grades))
    // TODO: implement me
}

function duplicateObject(matrikel, students){
  //console.log(matrikel);
  return  {"matrikelnummer": matrikel, "students": students.filter(s => matrikel == s.matrikelnummer)}
}

function boolDuplicates(student, students){
  return (students.filter(c => c.matrikelnummer == student.matrikelnummer).length > 1)
}

// Aufgabe 3.1.3
function duplicateStudents(students) {
  var result = students.reduce((acc, s) => {
      if (boolDuplicates(s, students)) {
        let cache = duplicateObject(s.matrikelnummer, students);
          return [...acc, cache]
      } else {
        return acc
      }
      }, []);
      console.log(order(result, 2))
      return result
}

// Aufgabe 3.1.4
function invalidGrades(grades) {
  return grades
    .map((s) => {
      // TODO: implement me

      return {
        matrikelnummer: -1 /* TODO: replace */,
        grades: [] /* TODO: replace */,
      };
    })
    .filter((e) => e.grades.length > 0)
}