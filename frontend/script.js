const btn = document.querySelector("#btn");

btn.addEventListener("click", analyser);

function couleurScore(score) {
  if (score < 70) {
    return "#ef1717";
  }
  if (score < 90) {
    return "#ffae00";
  }
  return "#04b876";
}

function appreciation(score) {
  if (score < 70) {
    return "Peu inclusif";
  }
  if (score < 90) {
    return "A améliorer";
  }
  return "Excellent";
}

async function analyser() {
  const texte = document.querySelector("#offre").value.toLowerCase();

  const response = await fetch("http://127.0.0.1:8000/analyse", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ texte }),
  });

  const data = await response.json();
  console.log(data);

  document.querySelector("#resultat").innerHTML = `
  <p>
    <div class="container-score">
    <div>
    <strong>Inclusivité :</strong> 
    </div>
    <span class="appreciation" style="color: ${couleurScore(data.score)};">
    ${appreciation(data.score)}
    </span>
    <strong>Score :</strong>
    <div class="score">
    ${data.score}/100 
      </div>
    </div>
    <br>
    <div class="status-bar">
      <span style="width:${data.score}%;
      background-color: ${couleurScore(data.score)};" class="status">
      </span>
    </div>
  </p>
<div class="criteres">
  <p>
  🛑 <strong>Risques d'exclusion détectés :</strong> 
</p>
  <ol>
  
  ${data.problemes
    .map(
      (
        p,
        index,
      ) => `<li><span style="background-color: none; color: red; padding: 0.2em 0.4em; border-radius: 5px;">
    ${data.criteres[index]}</span> : ${p}</li>`,
    )
    .join("")}
  </ol>
</div>
<br>
<div class="suggestions">
<p>
 💡 <strong>Recommandations :</strong>
</p>
  <ol>
    ${data.suggestions.map((s) => `<li>${s}</li>`).join("")}
  </ol>
</div>
  `;
}

// Nous recherchons un développeur disponible immédiatement pour rejoindre notre jeune équipe dynamique.
// Le candidat doit être capable de travailler sous pression et de respecter des délais serrés.
