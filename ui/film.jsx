import React from "react";
import { createRoot } from "react-dom/client";

async function main() {
  //const filmsResponse = await fetch("/api/v1/films");
  //const films = await filmsResponse.json();

  const rootElt = document.getElementById("app");
  const root = createRoot(rootElt);
  
  const filmResponse = await fetch("/api/v1" +  window.location.pathname)
  const film = await filmResponse.json();

  var props = "";

  for(var key in film){
     props = props + key + ": " + film[key];
  }


  return  root.render(
    Object.entries(film).map(([k,v]) => (
      <ul>
        <li>
           {k}: {v}
        </li>
      </ul>
    )),
  );
}


window.onload=main
