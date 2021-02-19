import React from "react";
import Card from "./Card";

import { connect } from "react-redux";

const Soma = (props) => {
  const { min, max } = props;

  return (
    <Card title="Soma dos Numeros" blue>
      <span>
        Resultado: <strong>{min + max}</strong>
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

export default connect(mapStateToProps)(Soma);
