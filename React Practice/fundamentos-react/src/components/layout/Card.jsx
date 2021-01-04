import React from "react";

const Card = (props) => {
  return (
    <div>
      <div>Conteudo</div>
      <div>{props.titulo}</div>
    </div>
  );
};

export default Card;
