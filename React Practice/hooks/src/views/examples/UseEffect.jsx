import React, { useEffect, useState } from "react";
import PageTitle from "../../components/layout/PageTitle";
import SectionTitle from "../../components/layout/SectionTitle";

function calcFactorial(num) {
  const n = parseInt(num);
  if (n < 0) return -1;
  if (n === 0) return 1;
  return calcFactorial(n - 1) * n;
}

function calcParity(num) {
  const n = parseInt(num);
  if (n % 2 === 0) return "Even";
  return "Odd";
}

const UseEffect = (props) => {
  const [number, setNumber] = useState(1);
  const [factorial, setFactorial] = useState(1);

  const [parityNumber, setParityNumber] = useState(1);
  const [parity, setParity] = useState("Odd");

  useEffect(
    function () {
      setFactorial(calcFactorial(number));
    },
    [number]
  );

  useEffect(
    function () {
      setParity(calcParity(parityNumber));
    },
    [parityNumber]
  );

  return (
    <div className="UseEffect">
      <PageTitle
        title="Hook UseEffect"
        subtitle="Permite executar efeitos colaterais em componentes funcionais!"
      />

      <SectionTitle title="Exercicio #01" />
      <div className="center">
        <div>
          <span className="text">Fatorial: </span>
          <span className="text red">{factorial}</span>
        </div>
        <input
          type="number"
          className="input"
          value={number}
          onChange={(e) => setNumber(+e.target.value)}
        />
      </div>

      <SectionTitle title="Exercicio #02" />
      <div className="center">
        <div>
          <span className="text">Stato: </span>
          <span className="text red">{parity}</span>
        </div>
        <input
          type="number"
          className="input"
          value={parityNumber}
          onChange={(e) => setParityNumber(+e.target.value)}
        />
      </div>
    </div>
  );
};

export default UseEffect;
