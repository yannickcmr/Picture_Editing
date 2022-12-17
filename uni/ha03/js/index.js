
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

function countDubs(student, students){
  if (students.filter(m => student == m.matrikelnummer).length > 1){
    //console.log(student, students.filter(m => student == m.matrikelnummer));
    return duplicateObject(student, students);
  }
}

// Aufgabe 3.1.3
function duplicateStudents(students) {
  return (students.filter(m =>  students.filter(s => s.matrikelnummer == m.matrikelnummer).length > 1)).map(s => duplicateObject(s.matrikelnummer, students))
}

function gradesDubs(grade, grades){
  return grades.filter(m => (m.matrikelnummer == grade.matrikelnummer) && (m.course == grade.course));
}

function gradesMap(grade, grades){
  return {"matrikelnummer": grade.matrikelnummer, "grades": grades.filter(g => (g.matrikelnummer == grade.matrikelnummer) && (g.course == grade.course))}
}

// Aufgabe 3.1.4
function invalidGrades(grades) {
  console.log("-->", grades.filter(g => gradesDubs(g, grades).length > 1).map(g => gradesMap(g, grades)));
  return grades.filter(g => gradesDubs(g, grades).length > 1).map(g => gradesMap(g, grades))
}