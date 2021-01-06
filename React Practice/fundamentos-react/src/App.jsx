import "./App.css";
import React from "react";

import TabelaProdutos from "./components/repeticao/TabelaProdutos";
import ListaAlunos from "./components/repeticao/ListaAlunos";
import FamiliaMembro from "./components/basicos/FamiliaMembro";
import Familia from "./components/basicos/Familia";
import Aleatorio from "./components/basicos/Aleatorio";
import Card from "./components/layout/Card";

const App = (props) => {
  return (
    <div className="App">
      <h1>Fundamentos React</h1>

      <div className="Cards">
        <Card titulo="Repeticao" color="#FF4C65">
          <TabelaProdutos></TabelaProdutos>
        </Card>

        <Card titulo="Repeticao" color="#FF4C65">
          <ListaAlunos></ListaAlunos>
        </Card>

        <Card titulo="Componente com Filhos" color="#00C8F8">
          <Familia lastname="Redmond">
            <FamiliaMembro name="Brandon" />
            <FamiliaMembro name="Felipe" />
            <FamiliaMembro name="Bella" />
          </Familia>
        </Card>

        <Card titulo="Desafio Aleatorio" color="#080">
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
