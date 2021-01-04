import React from "react";

import Aleatorio from "./components/basicos/Aleatorio";
import Card from "./components/layout/Card";

const App = (props) => {
  return (
    <div id="app">
      <h1>Fundamentos React</h1>

      <Card titulo="Exemplo de Card"></Card>
      <Aleatorio min={1} max={10} />
    </div>
  );
};

export default App;
