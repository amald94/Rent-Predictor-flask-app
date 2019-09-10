var select = document.getElementById("selectRegion"); 
var options = {'barrie': 0,
'belleville': 1,
'brantford': 2,
'brockville': 3,
'cambridge': 4,
'chatham kent': 5,
'city of toronto': 6,
'cornwall on': 7,
'gatineau': 8,
'guelph': 9,
'hamilton': 10,
'kapuskasing': 11,
'kawartha lakes': 12,
'kingston on': 13,
'kitchener waterloo': 14,
'leamington': 15,
'london': 16,
'markham york': 17,
'mississauga peel': 18,
'muskoka': 19,
'napanee': 20,
'norfolk county': 21,
'north bay': 22,
'oakville halton': 23,
'oshawa durham': 24,
'ottawa': 25,
'owen sound': 26,
'peterborough': 27,
'sarnia': 28,
'sault ste marie': 29,
'st catharines': 30,
'stratford on': 31,
'sudbury': 32,
'thunder bay': 33,
'timmins': 34,
'trenton on': 35,
'windsor area on': 36,
'woodstock on': 37}; 


  Object.entries(options).forEach(([key, value]) => {
    //console.log(key, value);
    var el = document.createElement("option");
    el.textContent = key;
    el.value = value;
    select.appendChild(el);
 });