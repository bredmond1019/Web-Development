import React from "react";

import Aleatorio from "./components/basicos/Aleatorio";

export default (props) => {
  return (
    <div id="app">
      <h1>Fundamentos React</h1>
      <Aleatorio min={1} max={10} />
    </div>
  );
};
