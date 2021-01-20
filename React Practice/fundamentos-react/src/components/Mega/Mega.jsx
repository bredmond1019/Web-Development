import React, { useState } from "react";

import "./Mega.css";

const Mega = (props) => {
  function gerarNumeroNaoContido(min, max, array) {
    const aleatorio = parseInt(Math.random() * (max - min)) + min;
    return array.includes(aleatorio)
      ? gerarNumeroNaoContido(min, max, array)
      : aleatorio;
  }

  function gerarNumeros(qtde) {
    const numeros = Array(qtde)
      .fill(0)
      .reduce((nums) => {
        const novoNumero = gerarNumeroNaoContido(1, 60, nums);
        return [...nums, novoNumero];
      }, [])
      .sort((n1, n2) => n1 - n2);

    return numeros;
  }

  const [qtde, setQtde] = useState(props.qtde || 6);
  const numerosInicias = gerarNumeros(qtde);
  const [numeros, setNumeros] = useState(numerosInicias);

  return (
    <div className="Mega">
      <h2>Mega</h2>
      <h3>{numeros.join(" ")}</h3>
      <div>
        <label>Qtde de Numeros</label>
        <input
          min="6"
          max="10"
          type="number"
          value={qtde}
          onChange={(e) => setQtde(+e.target.value)}
        />
      </div>
      <button onClick={(_) => setNumeros(gerarNumeros(qtde))}>
        Gerar Numeros
      </button>
    </div>
  );
};

export default Mega;

/* 

NOTE:   For the input, we can make it so when we change the quanity 
the numbers will be re-generated:

onChange={(e) => {
    setQtde(+e.target.value)
    setNumeros(gerarNumeros(+e.target.value))
    }

*/
