import React from "react";
import Card from "./Card";

import { connect } from "react-redux";

const Sorteio = (props) => {
  const { min, max } = props;
  const aleatorio = parseInt(Math.random() * (max - min) + min);

  return (
    <Card title="Sorteio de um Numero" purple>
      <span>
        <strong>Resultato: </strong> {aleatorio}
      </span>
    </Card>
  );
};

function mapStateToProps(state) {
  return {
    min: state.numeros.min,
    max: state.numeros.max,
  };
}

export default connect(mapStateToProps)(Sorteio);
