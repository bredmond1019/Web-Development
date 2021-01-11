import React from "react";

const IndiretaFilho = (props) => {
  const cb = props.quandoClicar;

  return (
    <div>
      <div>Filho</div>
      <button onClick={(e) => cb("Brandon", 32, true)}>
        Fornecer Informacoes
      </button>
    </div>
  );
};

export default IndiretaFilho;
