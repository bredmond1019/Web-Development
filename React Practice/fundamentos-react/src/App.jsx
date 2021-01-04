import "./App.css";
import React from "react";

import Aleatorio from "./components/basicos/Aleatorio";
import Card from "./components/layout/Card";

const App = (props) => {
  return (
    <div className="App">
      <h1>Fundamentos React</h1>

      <div className="Cards">
        <Card titulo="Desafio Aleatorio" color="#080">
          <Aleatorio min={1} max={10} />
        </Card>

        <Card titulo="Desafio Aleatorio">
          <Aleatorio min={1} max={10} />
        </Card>

        <Card titulo="Desafio Aleatorio">
          <Aleatorio min={1} max={10} />
        </Card>
      </div>
    </div>
  );
};

export default App;
